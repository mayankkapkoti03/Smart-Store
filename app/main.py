from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import product
import os
from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv
from authlib.integrations.starlette_client import OAuth
from app.routers import auth
import os


# load_dotenv()   # 👈 LOAD HERE (very top)

# oauth = OAuth()

# oauth.register(
#     name="google",
#     client_id=os.getenv("CLIENT_ID"),
#     client_secret=os.getenv("CLIENT_SECRET"),
#     server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
#     client_kwargs={
#         "scope": "openid email profile"
#     }
# # )

# CLIENT_ID = os.getenv("CLIENT_ID")
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Store")
app.include_router(auth.router)
app.include_router(product.router)
app.add_middleware(SessionMiddleware, secret_key="supersecretkey")