
# from passlib.context import CryptContext
# from datetime import datetime, timedelta
# from jose import jwt

# SECRET_KEY = "SECRET"
# ALGORITHM = "HS256"

# pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def hash_password(p): return pwd.hash(p)
# def verify_password(p, h): return pwd.verify(p, h)

# def create_token(data: dict):
#     to_encode = data.copy()
#     to_encode["exp"] = datetime.utcnow() + timedelta(hours=2)
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)



from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "SECRET_KEY_CHANGE_LATER"
ALGORITHM = "HS256"

pwd = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    return pwd.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd.verify(plain_password, hashed_password)

def create_token(data: dict):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(hours=2)
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

