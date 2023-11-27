from jose import JWTError, jwt
from datetime import datetime,timedelta
from . import schemas, databases, models
from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2AuthorizationCodeBearer
from sqlalchemy.orm import Session
from .config import settings

oauth2_scheme = OAuth2AuthorizationCodeBearer(authorizationUrl='login',tokenUrl='token')
#oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl='login')#authorizationUrl='login', tokenUrl="token")

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schemas.tokenData(id=id)

    except JWTError:
        raise credentials_exception
    
    return token_data
    



def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(databases.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"could not valid credentials",headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    
    return user



# SECRET_KEY = "password123"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 60



# def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(databases.get_db)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         user_id: int = payload.get("user_id")
#         if user_id is None:
#             raise credentials_exception
#         user = get_user(db, user_id)
#         if user is None:
#             raise credentials_exception
#         return user
#     except jwt.ExpiredSignatureError:
#         raise credentials_exception
#     except jwt.JWTError:
        # raise credentials_exception