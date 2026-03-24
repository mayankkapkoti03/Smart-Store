from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.order_service import place_order
from app.auth.dependencies import get_current_user

router = APIRouter(prefix = "/orders", tags = ["Orders"])

@router.post("/")
def create_order(db : Session = Depends(get_db), user = Depends(get_current_user)):
    return place_order(db, user.id)

@router.get("/")
def get_order(db : Session = Depends(get_db), user = Depends(get_current_user)):
    return get_order(db, user.id)
