#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy
from SyncMovie.items import SyncmovieItem
import logging
import json

logging.basicConfig(
    filename="SyncMovie.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%Y/%m/%d %I:%M:%S %p",
)
logging.warning("warn message")
logging.error("error message")


class move(scrapy.Spider):
    name = "SyncMovieSpider"
    allowed_domains = ["maoyan.com"]
    start_urls = ["https://maoyan.com"]

    def start_requests(self):
        url = "https://maoyan.com/films"
        yield scrapy.Request(url, callback=self.get_movies_list)

    def get_movies_list(self, response):
        movies = response.css("dd")
        movies_list = [
            {
                "movieid": item.css(".movie-item-title a::attr(data-val)").extract_first(),
                "cover": item.xpath('//img[contains(@src, "https")]/@src').extract(),
                "name": item.css(".movie-item-title a::text").extract_first(),
                "url": item.css(".movie-item-title a::attr(href)").extract_first(),
            }
            for item in movies
        ]

        for v in movies_list:
            logging.debug(str(v["name"]))
            detail_url = "{}{}".format(self.start_urls[0], v["url"])
            yield scrapy.Request(detail_url, callback=self.parse,meta=v)

        # css选择器提取下一页链接

        next_page=list(set(response.xpath('//a[contains(@href, "offset")]/@href').extract()))
        # 判断是否存在下一页
        if next_page is not None:
            #next_page = response.urljoin(next_page)
            # 提交给parse继续抓取下一页
            next_url="https://maoyan.com/films%s" % next_page[0]
            del(next_page[0])
            yield scrapy.Request(next_url, callback=self.get_movies_list)

    def parse(self, response):
        item = SyncmovieItem()
        item["movieid"] = response.meta['movieid']
        item["cover"] = response.meta['cover'][0]
        item["name"] = response.meta['name']
        item["url"] = response.meta['url']
        print(type(response.meta))
        info=response.css('div.celeInfo-right')
        item["ename"]=info.css('.ename::text').extract_first()
        ul_info=info.css('li.ellipsis::text').extract()
        item["category"]=ul_info[0]
        item["area"] =str.strip(ul_info[1]).splitlines()[0]
        item["date"] = ul_info[2][:16]
		item["desc"] = response.css("div.tab-desc.tab-content").css("span.dra::text").extract_first()

        actors = response.css("li.celebrity.actor")
        movie_actors = []
        if any(actors):
            for actor in actors:
                actor_photo = actor.css("img")[0].attrib["data-src"]
                actor_name = actor.css(".name::text").extract_first()
                actor_role = actor.css(".role::text").extract_first()
                movie_actors.append(
                    {
                        "actor_photo": actor_photo,
                        "actor_name": actor_name,
                        "actor_role": actor_role,
                    }
                )
        item["actor"] = movie_actors
        """
        hxs.select('//dl[@class="clearfix"]//img/@src').extract()
        response.css('.product-list img::attr(src)').extract() # extract_first() to get only one
        """

        # 把取到的数据提交给pipline处理
        yield item
