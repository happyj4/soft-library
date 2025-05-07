from fastapi import APIRouter, status, Depends
from db import database
from sqlalchemy.orm import Session
from repos import book_rep
from schemas.book_schemas import ShowAllBooks


get_db = database.get_db

router = APIRouter(prefix="/books", tags=['Books 📚'])

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ShowAllBooks])
def get_all(db: Session = Depends(get_db)):
  return book_rep.get_all(db)
