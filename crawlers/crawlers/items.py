# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from datetime import datetime


class CrawlersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ExhibitionItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(serializer=str)
    category = scrapy.Field(serializer=str)
    location = scrapy.Field(serializer=str)
    start_time = scrapy.Field(serializer=datetime)
    end_time = scrapy.Field(serializer=datetime)
    url = scrapy.Field(serializer=str)
    image_url = scrapy.Field(serializer=str)
