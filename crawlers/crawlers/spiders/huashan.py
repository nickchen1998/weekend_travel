import scrapy
from bs4 import BeautifulSoup
from crawlers.items import ExhibitionItem
from pprint import pprint


class HuashanSpider(scrapy.Spider):
    name = 'huashan'
    allowed_domains = ['www.huashan1914.com']
    start_urls = ["https://www.huashan1914.com/w/huashan1914/exhibition"]

    def parse(self, response, **kwargs):
        exhibition = ExhibitionItem()
        soup = BeautifulSoup(response.text, "lxml")

        for item in soup.find_all("li", class_="item-static"):
            # print(item.find("div", class_="card-text-name").text)
            exhibition["name"] = item.find("div", class_="card-text-name").text
            exhibition["category"] = item.find("div", class_="event-list-type").text.replace("\n", "")

            date = item.find("div", class_="event-date").text.split("-")
            start_time = date[0].replace(".", "-").replace("\n", "").replace(" ", "")
            exhibition["start_time"] = start_time
            if len(date) > 1:
                end_time = date[1].replace(".", "-").replace("\n", "").replace(" ", "")
                if len(end_time) == 10:  # ISO date format len
                    exhibition["end_time"] = end_time
                else:
                    exhibition["end_time"] = None
            else:
                exhibition["end_time"] = None

            exhibition["url"] = f"https://www.huashan1914.com{item.find('a').get('href')}"

            image_url = item.find("div", class_="card-img-content").get("style")
            image_url = image_url.replace("background-image:url('", "").replace("')", "")
            exhibition["image_url"] = image_url

            yield scrapy.Request(url=exhibition["url"], meta=exhibition, callback=self.get_location)

            # print(exhibition)
            # yield exhibition

        next_page = soup.find("div", class_="pagination").find_all("li")[-1]

        if next_page.text == "下一頁":
            url = next_page.find("a").get("href")
            url = f"https://www.huashan1914.com{url}"

            yield scrapy.Request(url=url, callback=self.parse)

    @staticmethod
    def get_location(response):
        exhibition = response.meta

        article_info = BeautifulSoup(response.text, "lxml").find("ul", class_="article-info-list")

        article_info = article_info.find_all("li")

        for info in article_info:
            if info.find("h6").text == "活動地點":
                exhibition["location"] = "華山"
                exhibition["location_detail"] = info.find("div", class_="address").text.replace("\n", "")
                pprint(exhibition)

        yield exhibition


if __name__ == '__main__':
    pass
