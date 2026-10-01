from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..log import log_function
import bcrypt

from ..model import Book , UserDetail
from ..session import get_db

# Initialize the router. You can define a common prefix and tags here.
router = APIRouter(
    prefix="/User",
    tags=["User"]
)

@log_function
@router.get("/")
# CREATE USER
def create_user(username :str,userpwd:str,userrole :str , db: Session = Depends(get_db)):
    # 1. Check if the username already exists (since it's UNIQUE)
    existing_user = db.query(UserDetail).filter(UserDetail.username == username).first()
    if existing_user:
        raise HTTPException(
            status_code=404,
            detail=f"username already Registered",
            headers={"X-Error": "Username already registered"},
        )
                    
    hashpwd = bcrypt.hashpw(userpwd.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    new_user = UserDetail(username=username, userpwd= hashpwd, role=userrole)

    # 3. Save to database
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        db.rollback()
        print("DATABASE ERROR:", repr(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error occurred"
        )
    return {
        "message": "User created successfully",
        "user_id": new_user.userid,
        "username": new_user.username
    }