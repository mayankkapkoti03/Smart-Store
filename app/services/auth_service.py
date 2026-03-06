
from app.schemas import UserCreate
from sqlalchemy.orm import Session
from app import models

from app.auth.hashing import hash_password, verify_password



#Register Endpoint will use this function to create new user with hashed password and store it in database.
def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)

    db_user = models.UserDB(
        email=user.email,
        hashed_password=hashed_password,
        role=user.role
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# #Login Endpoint will use this function to authenticate user and generate token if credentials are correct.
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.UserDB).filter(models.UserDB.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user