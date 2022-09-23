import random
import shutil
import string

from fastapi import APIRouter, Depends, \
    UploadFile, File
from sqlalchemy.orm import Session

from db import article_service
from db.database import get_db
from schema.article_schemas import ArticleBase, \
    ArticleDisplay

router = APIRouter(
    prefix='/article',
    tags=['article']
)


@router.post('/create', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return article_service.create_article(db=db, obj_in=request)


@router.get('/all')
def get_all_articles(db: Session = Depends(get_db)):
    return article_service.get_all_articles(db=db)


@router.get('/detail/{id}', response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
    return article_service.get_article(db=db, id=id)


@router.delete('/delete/{id}')
def delete_article(id: int, db: Session = Depends(get_db)):
    return article_service.delete_article(db=db, id=id)


@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'

    with open(path, "a+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename': path}
