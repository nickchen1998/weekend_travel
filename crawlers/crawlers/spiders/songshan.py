import scrapy
from bs4 import BeautifulSoup
from crawlers.items import ExhibitionItem
from pprint import pprint


class SongshanSpider(scrapy.Spider):
    name = 'songshan'
    allowed_domains = ['www.songshanculturalpark.org']
    start_urls = ['http://www.songshanculturalpark.org/exhibitionlist.aspx']

    def parse(self, response, **kwargs):
        exhibition = ExhibitionItem()

        print(response.text)
