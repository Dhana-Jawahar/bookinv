
from pydantic import BaseModel, Field, ConfigDict

class BookBase(BaseModel):
    title: str = Field(..., max_length=255)
    author: str = Field(...,min_length=2, max_length=255)
    isbn: str = Field(..., max_length=20)
    price: Decimal = Field(..., max_digits=10, decimal_places=2)
    quantity: int = Field(default=0, ge=0)


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=255)
    author: Optional[str] = Field(None, max_length=255)
    isbn: Optional[str] = Field(None, max_length=20)
    price: Optional[Decimal] = Field(None, max_digits=10, decimal_places=2)
    quantity: Optional[int] = Field(None, ge=0)


class BookResponse(BookBase):
    bookid: int

    # Allows Pydantic to read data directly from SQLAlchemy objects
    model_config = ConfigDict(from_attributes=True)



class Book(BookBase):
    bookid:int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    """Schema for registering a new user."""
    username: str = Field(..., max_length=150, description="Unique login username")
    userpwd: str = Field(..., max_length=255, )
    role: Literal["user", "admin"] = Field(default="user")

class UserCreate(BaseModel):
    """Schema for registering a new user."""
    username: str = Field(..., max_length=150, description="Unique login username")
    userpwd: str = Field(..., max_length=255, )
    role: Literal["user", "admin"] = Field(default="user")

class UserDetail(UserBase):
    """Schema for registering a new user."""
    username: str = Field(..., max_length=150, description="Unique login username")
    userpwd: str = Field(..., max_length=255, )
    role: Literal["user", "admin"] = Field(default="user")



