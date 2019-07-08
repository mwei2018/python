# -*- coding:utf-8 -*-
import pandas as pd
from pymongo import MongoClient


class MongoBase:
    def __init__(self, collection):
        self.collection = collection
        self.open_db()

    def open_db(self):
        user = '##'
        passwd = '###'
        host = '##'
        port = '##'
        auth_db = 'app_db'
        uri = "mongodb://" + user + ":" + passwd + \
            "@" + host + ":" + port + "/" + auth_db
        self.con = MongoClient(uri, connect=False)
        self.db = self.con['app_db']
        self.collection = self.db[self.collection]

    def dataframe_to_mongo(self, select_df):
        records = select_df.to_dict('records')
        result = self.collection.insert_many(records)
        return result

    def close_db(self):
        self.con.close()


if __name__ == '__main__':
    mongo = MongoBase('courses')
    course = {
        'course_name': 'python',
        'course_price': '25'
    }

    result1 = mongo.collection.insert_one(course)
    print(result1)
    print(result1.inserted_id)

    result = mongo.collection.find()
    mongo.close_db()
    data = list(result)
    print(type(result))
    print(result)

    df = pd.DataFrame(data)  # 读取整张表 (DataFrame)
    print(df)
