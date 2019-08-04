# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SyncmovieItem(scrapy.Item):
    # define the fields for your item here like:
    movieid = scrapy.Field()  # 电影ID
    cover = scrapy.Field()  # 电影封面
    score = scrapy.Field()  # 电影得分
    name = scrapy.Field()  # 电影名称
    ename = scrapy.Field()  # 电影En名称
    url = scrapy.Field()  # 电影详情页面url
    count = scrapy.Field()  # 累计票房
    area = scrapy.Field()  # 电影所属区域
    date = scrapy.Field()  # 电影上映时间
    actor = scrapy.Field()  # 演职人员
    desc = scrapy.Field()  # 剧情简介
    category = scrapy.Field()  # 分类

    pass
