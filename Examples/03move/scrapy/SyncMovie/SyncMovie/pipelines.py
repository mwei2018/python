# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class SyncmoviePipeline(object):
    def __init__(self):
        # 建立MongoDB数据库连接
        client = pymongo.MongoClient(
            "mongodb://mwei:*****@ds016058.mlab.com:16058/app_db", connect=False
        )
        # 连接所需数据库,ScrapyChina为数据库名
        self.db = client["app_db"]
        # 连接所用集合，也就是我们通常所说的表，movie为表名
        self.post = self.db["movie"]

    def process_item(self, item, spider):
        #利用item的名称作为表名
        name = item.__class__.__name__
        postItem = dict(item)  # 把item转化成字典形式
        # self.post.insert(postItem)  # 向数据库插入一条记录
        self.db[name].update_one(item, {"$set": postItem}, upsert=True)
        return item  # 会在控制台输出原item数据，可以选择不写
