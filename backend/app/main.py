from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.database import engine
from app import models
import os
from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv
from authlib.integrations.starlette_client import OAuth
from app.routers import auth, product, cart, order
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")



models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Store")

app.include_router(auth.router)
app.include_router(product.router)
app.include_router(cart.router)
app.include_router(order.router)
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)