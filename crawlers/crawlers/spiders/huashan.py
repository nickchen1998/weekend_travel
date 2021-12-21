import scrapy
from bs4 import BeautifulSoup
from crawlers.items import ExhibitionItem


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
            exhibition["location"] = None

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

            print(exhibition)
            yield exhibition

        next_page = soup.find("div", class_="pagination").find_all("li")[-1]

        if next_page.text == "下一頁":
            url = next_page.find("a").get("href")
            url = f"https://www.huashan1914.com{url}"

            yield scrapy.Request(url=url, callback=self.parse)
