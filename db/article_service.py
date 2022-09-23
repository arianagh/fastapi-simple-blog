from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from db.models import Article
from schema.article_schemas import ArticleBase


def create_article(db: Session, obj_in: ArticleBase):
    new_article = Article(
        title=obj_in.title,
        content=obj_in.content,
        creator=obj_in.creator,
        image_url=obj_in.image_url
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_all_articles(db: Session):
    articles = db.query(Article).all()
    return articles


def get_article(db: Session, id: int):
    article = db.query(Article).filter(Article.id == id).first()
    return article


def delete_article(db: Session, id: int):
    article = db.query(Article).filter(Article.id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id {id} not found')
    db.delete(article)
    db.commit()
    return
