import datetime

from sqlalchemy import Column, Integer, \
    String, DateTime

from db.database import Base


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    image_url = Column(String)
    creator = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
