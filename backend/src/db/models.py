from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint, Enum
from database import Base
from sqlalchemy.orm import relationship
import enum


class BookStatus(enum.Enum):
    READ = 'read'
    UNREAD = 'unread'
    PLANNED = 'planned'

class Author(Base):
    __tablename__ = 'Author'

    author_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    books = relationship('Book', back_populates='author', cascade='all, delete-orphan')
    
    # Таблиця книг
class Book(Base):
    __tablename__ = 'Book'

    book_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('Author.author_id', ondelete='SET NULL'), nullable=True)
    status = Column(Enum(BookStatus, name='book_status', create_type=False)) 
    rating = Column(Integer)

    __table_args__ = (
        CheckConstraint('rating BETWEEN 0 AND 5', name='rating_between_0_and_5'),
    )

    author = relationship('Author', back_populates='books')