from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID, uuid4  

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=101)  

BOOKS = []  

app = FastAPI()

@app.get("/")
def read_api():
    return BOOKS

@app.post("/")
def create_book(book: Book):
    book.id = uuid4()  
    BOOKS.append(book)
    return book    

@app.put("/{book_id}")
def update_book(book_id: UUID, book: Book):
    for idx, x in enumerate(BOOKS):
        if x.id == book_id:
            BOOKS[idx] = book  
            return BOOKS[idx]
    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id} does not exist"
    )

@app.delete("/{book_id}")
def delete_book(book_id: UUID):
    for idx, x in enumerate(BOOKS):
        if x.id == book_id:
            del BOOKS[idx]
            return {"message": f"ID: {book_id} deleted"}
    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id} does not exist"
    )
