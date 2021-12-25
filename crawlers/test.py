from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.crawler import CrawlerProcess
from crawlers.spiders.huashan import HuashanSpider
from scrapy.utils.project import get_project_settings
process = CrawlerProcess(get_project_settings())

process.crawl(HuashanSpider)
process.start()
