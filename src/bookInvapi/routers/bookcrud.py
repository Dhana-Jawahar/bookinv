from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..log import log_function

from ..model import Book
from ..session import get_db

# Initialize the router. You can define a common prefix and tags here.
router = APIRouter(
    prefix="/Book",
    tags=["Books"]
)

@log_function
@router.get("/")
def get_books(db: Session = Depends(get_db)):
# ,user=Depends(authenticate_user)):
    return db.query(Book).all()

@log_function
@router.get("/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    # ,user=Depends(authenticate_user)):
    book = db.query(Book).filter(Book.bookid == book_id).first()
    if not book:
        raise HTTPException(
            status_code=404,
            detail=f"Book {book_id} not found",
            headers={"X-Error": "Book not found"},
        )
    return book