from jose import jwt
from datetime import datetime, timedelta
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)



#JWT (JSON Web Tokens) are used for authentication. When a user logs in, we generate a JWT token that contains the user's information and an expiration time. This token is then sent back to the client, which can use it for subsequent requests to access protected endpoints. The server will verify the token on each request to ensure that the user is authenticated and authorized to access the requested resource.
