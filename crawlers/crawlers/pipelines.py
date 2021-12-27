# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crawlers.orm_models import ExhibitionItem


class CrawlersPipeline:

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        session = self._get_session()

        result = session.query(ExhibitionItem).filter_by(name=item["name"]).all()
        if not result:
            if item.get("depth"):
                del item["depth"]
            if item.get("download_latency"):
                del item["download_latency"]
            if item.get("download_slot"):
                del item["download_slot"]
            if item.get("download_timeout"):
                del item["download_timeout"]

            session.add(ExhibitionItem(**item))

        session.commit()
        session.close()
        return item

    @staticmethod
    def _get_session():
        engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/traveler")
        Session = sessionmaker(bind=engine)
        session = Session()

        return session
