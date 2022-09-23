from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ArticleBase(BaseModel):

    title: Optional[str] = None
    content: Optional[str] = None
    creator: Optional[str] = None
    image_url: Optional[str] = None


class ArticleDisplay(BaseModel):

    id: int
    title: str
    content: str
    creator: str
    image_url: str
    created_at: datetime

    class Config:
        orm_mode = True
