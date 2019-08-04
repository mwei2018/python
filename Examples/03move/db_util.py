# -*- coding:utf-8 -*-

import gflags
import logging
import pymongo
from functools import wraps

gflags.DEFINE_string(
    "move_mongodb_server_address",
    "ds016058.mlab.com",
    "address of the Mongo database caching.",
)
gflags.DEFINE_string(
    "move_mongodb_server_user", "mwei", "address of the Mongo database caching."
)
gflags.DEFINE_string(
    "move_mongodb_server_pwd", "1qaz!QAZ", "address of the Mongo database caching."
)
gflags.DEFINE_string(
    "move_mongodb_server_port", "16058", "address of the Mongo database caching."
)
gflags.DEFINE_string(
    "move_mongodb_database_name", "app_db", "database name containing."
)
gflags.DEFINE_integer(
    "mongodb_connection_timeout",
    1,
    "seconds before assuming the mongodb connection timeouts.",
)
gflags.DEFINE_boolean(
    "disable_mongodb_exception", False, "disable MongoDB exception propagation."
)
gflags.DEFINE_integer(
    "mongodb_connection_retry", 10, "maximum connection attempts to the mongo database."
)

Flags = gflags.FLAGS


def _silent_connection_failure(func):
    """修饰符用于避免在数据库超时时引发异常
    Parameters:
        func: 装饰函数
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """封装函数以捕获超时异常。
        """
        if not Flags.disable_mongodb_exception:
            return func(*args, **kwargs)

        try:
            result = func(*args, **kwargs)
        except pymongo.errors.ServerSelectionTimeoutError as e:
            logging.error("不能连接服务器: %s", e)
            return None
        return result

    return wrapper


class MongoDBManager:
    """MongoDB 操作公共类"""

    address = None

    def __init__(self, lazy_connection=False):
        """构造初始化
        Parameters:
            lazy_connection: 是否延迟连接
        """

        account_info = {
            "user": Flags.move_mongodb_server_user,
            "password": Flags.move_mongodb_server_pwd,
            "host": Flags.move_mongodb_server_address,
            "port": Flags.move_mongodb_server_port,
            "auth_db": Flags.move_mongodb_database_name,
        }

        if self.address is None:
            self.address = (
                "mongodb://{user}:{password}@{host}:{port}/{auth_db}"
            ).format(**account_info)

        for _ in range(Flags.mongodb_connection_retry):
            self.client = self._connect(self.address, lazy_connection)
            if self.client is not None:
                self.db = self.client["app_db"]
                break
        else:
            logging.critical("无法连接到MongoDB 服务器")

    def _connect(self, address, lazy_connection=False):
        """连接 MongoDB server.
        Parameters:
            address: MongoDB server 服务器地址.
            lazy_connection: 延迟连接
        """
        client = pymongo.MongoClient(
            address,
            connect=False,
            serverSelectionTimeoutMS=Flags.mongodb_connection_timeout,
        )
        if lazy_connection:
            return client

        # 测试服务器连接是否成功
        try:
            client.server_info()
        except pymongo.errors.ServerSelectionTimeoutError as e:
            logging.error("无法连接到MongoDB 服务器： %s.", address)
            client = None

        return client

    @_silent_connection_failure
    def find_match(self, collection_name: str, query: str):
        """查询
        Parameters:
            collection_name:查询文档名称（类似table）
            query: 查询表达式请求
        Returns:
            返回查询结果，没有匹配则返回None
        """
        query_data = []
        try:
            query_data = self.db.collection_name.find(query)
        except pymongo.errors.OperationFailure as err:
            print("PyMongo ERROR:", err, "\n")

        # table = self.client.collection_name.matches
        # return table.find()
        return query_data

    @_silent_connection_failure
    def save_match(self, collection_name: str, record_data):
        """保存数据到db中
        Parameters:
            match_data: 保存的数据.
        """
        matches = self.client.collection_name.matches
        id = matches.insert_one(record_data).inserted_id
        logging.info("Record inserted - id: " + str(id))

    @_silent_connection_failure
    def dataframe_to_mongo(self, collection, df):
        """保存dataframe数据到db中
               Parameters:
                   df: 保存的数据.
               """
        records = df.to_dict("records")
        result = self.client.collection.insert_many(records)
        return result

    def close_db(self):
        self.db.close()
