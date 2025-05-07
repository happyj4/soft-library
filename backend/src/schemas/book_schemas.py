from pydantic import BaseModel
from typing import Text
from schemas.author import Author

class ShowAllBooks(BaseModel):
  book_id:int
  title:str
  status: Text
  rating:int
  author: Author
    
  class Config():
      orm_mode = True
  
