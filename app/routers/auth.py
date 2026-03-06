
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas
import app.services.auth_service as auth_service
from app.auth.jwt_handler import create_access_token
from app.auth.dependencies import get_current_user
from app.logger import logger
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/me", response_model=schemas.UserResponse)
def read_current_user(current_user: schemas.UserCreate = Depends(get_current_user)):
    return current_user

#Register Endpoint for user registration. It accepts a UserCreate schema, which includes the user's email and password. The endpoint uses the create_user function from the auth_service to create a new user with a hashed password and store it in the database.
@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return auth_service.create_user(db, user)


#Login Endpoint for user authentication. It accepts a UserCreate schema, which includes the user's email and password. The endpoint uses the authenticate_user function from the auth_service to verify the user's credentials. If the credentials are valid, it generates a JWT token using the create_access_token function and returns it to the client. The client can then use this token for subsequent requests to access protected endpoints.
# @router.post("/login", response_model = schemas.Token)
# def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = auth_service.authenticate_user(db, user.email, user.password)

#     if not db_user:
#         raise HTTPException(status_code = 400, detail = "Invalid email or password")
    
#     access_token = auth_service.create_access_token(
#         data = {"sub" : db_user.email}
#     )

#     return {
#         "access_token": access_token,
#         "token_type" : "bearer"
#     }


from fastapi.security import OAuth2PasswordRequestForm


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    logger.info(f"Login attempt for user: {form_data.username}")
    user = auth_service.authenticate_user(db, form_data.username, form_data.password)

    if not user:
        logger.warning(f"Failed login attempt for user: {form_data.username}")
        raise HTTPException(status_code=401, detail="Invalid credentials")
    logger.info(f"User {form_data.username} authenticated successfully")

    access_token = create_access_token({"sub": user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }