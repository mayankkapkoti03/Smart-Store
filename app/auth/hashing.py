from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


#Password hashing and verification using passlib. We use bcrypt algorithm for hashing passwords. The hash_password function takes a plain password and returns the hashed version, while the verify_password function checks if a given plain password matches the hashed password stored in the database.

#Never store plain password in database, always store hashed password. 