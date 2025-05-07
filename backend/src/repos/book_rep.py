from sqlalchemy.orm import Session
from db.models import Book


def get_all(db:Session):
  books = db.query(Book).all()
  return books