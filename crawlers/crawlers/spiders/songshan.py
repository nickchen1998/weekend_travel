import scrapy
from bs4 import BeautifulSoup
import json
from crawlers.items import ExhibitionItem
from pprint import pprint
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By


class SongshanSpider(scrapy.Spider):
    name = 'songshan'
    allowed_domains = ['www.songshanculturalpark.org']
    start_urls = ['https://www.songshanculturalpark.org/ExhibitionList.aspx']

    def start_requests(self):
        url = "https://www.songshanculturalpark.org/ExhibitionList.aspx"
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        driver = response.request.meta["driver"]
        items = driver.find_element(By.TAG_NAME, "div#exhibition")
        # items = items.find_elements(By.TAG_NAME, "li")
        print(items.text)
        # print(response.text)

