from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from .schemas import UserPost
from .models import User
from ..db.database import get_db


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserPost, db: Session = Depends(get_db)):
    user = User(password=user_data.password)
    db.add(user)
    return {
        "message": "User created",
    }
