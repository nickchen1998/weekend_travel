import scrapy
from bs4 import BeautifulSoup
import json
from crawlers.items import ExhibitionItem
from pprint import pprint


class SongshanSpider(scrapy.Spider):
    name = 'songshan'
    allowed_domains = ['www.songshanculturalpark.org']
    start_urls = ['https://www.songshanculturalpark.org/ExhibitionList.aspx?kind=0&type=1&p=1&q=get']

    def parse(self, response, **kwargs):
        exhibition = ExhibitionItem()
        res = json.loads(response.text)["items"]
        i = 1
        for j in range(5):
            if res:
                # for item in res:
                #     print(item["Title"])
                i += 1
                url = self.start_urls[0].replace(f"p=1", f"p={i + 1}")
                print(url)
                yield scrapy.Request(url=url)
            else:
                break
