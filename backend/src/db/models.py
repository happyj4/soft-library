from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint, Enum
from db.database import Base
from sqlalchemy.orm import relationship


class Author(Base):
    __tablename__ = 'author'

    author_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    books = relationship('Book', back_populates='author', cascade='all, delete-orphan')
    
    # Таблиця книг
class Book(Base):
    __tablename__ = 'book'

    book_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('author.author_id', ondelete='SET NULL'), nullable=True)
    status = Column(String, nullable=False) 
    rating = Column(Integer)


    author = relationship('Author', back_populates='books')