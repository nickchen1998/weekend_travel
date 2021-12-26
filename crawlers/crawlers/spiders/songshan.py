import scrapy
from bs4 import BeautifulSoup
import json
from crawlers.items import ExhibitionItem
from pprint import pprint
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from crawlers.middlewares import sleep


class SongshanSpider(scrapy.Spider):
    name = 'songshan'
    allowed_domains = ['www.songshanculturalpark.org']
    # start_urls = ['https://www.songshanculturalpark.org/ExhibitionList.aspx']
    start_urls = ["https://www.songshanculturalpark.org/ExhibitionList.aspx?kind=0&type=1&p=1&q=get"]

    def parse(self, response, **kwargs):
        exhibition = ExhibitionItem()
        items = json.loads(response.text)["items"]

        for item in items:
            item_id = item["ID"]
            url = f"https://www.songshanculturalpark.org/Exhibition.aspx?q=get&ID={item_id}"
            exhibition["url"] = url.replace("q=get", "")
            yield scrapy.Request(url=url, meta=exhibition, callback=self.get_location)

        page = 1
        for i in range(10):
            url = self.start_urls[0].replace("p=1", f"p={page+1}")
            page += 1
            yield scrapy.Request(url=url, callback=self.parse)

    def get_location(self, response):
        exhibition = response.meta

        res = json.loads(response.text)["item"][0]
        # print(res)
        exhibition["name"] = res["Title"]
        exhibition["category"] = "展演資訊"

        date = res["ExDate"].split("~")
        exhibition["start_time"] = date[0].replace("/", "-")
        exhibition["end_time"] = date[1].replace("/", "-")

        exhibition["location"] = "松山文創園區"
        exhibition["location_detail"] = res["ExPlace"]
        print(exhibition)
        # yield exhibition
