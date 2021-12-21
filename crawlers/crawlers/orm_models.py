from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine
from sqlalchemy import Integer, String, DATETIME, Text

Base = declarative_base()
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/traveler")


class ExhibitionItem(Base):
    __tablename__ = "exhibition"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    category = Column(String(50))
    location = Column(String(50))
    start_time = Column(DATETIME)
    end_time = Column(DATETIME)
    url = Column(Text)
    image_url = Column(Text)


def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    drop_table()
    create_table()
