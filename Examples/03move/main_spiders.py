from scrapy.cmdline import execute
import os,sys

sys.path.append(os.path.dirname(os.path.basename(__file__)))
 #注意，SyncMovieSpider是爬虫名，不是项目名,
execute(['scrapy','crawl','SyncMovieSpider'])