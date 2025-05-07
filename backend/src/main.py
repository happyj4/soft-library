from fastapi import FastAPI
from views import book

app = FastAPI()

app.include_router(book.router)