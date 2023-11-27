from __future__ import annotations
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, ClassVar
from pydantic.types import conint

class postbase(BaseModel):
    title: str
    content: str
    published: bool = True


class postcreate(postbase):
    pass

class userout(BaseModel):
    id : int
    email: EmailStr
    created_at: datetime

    class config:
        orm_mode = True

        
class post(postbase):
    id: int
    created_at: datetime
    owner_id: int
    owner : userout

    class config:
        orm_mode = True

class PostOut(BaseModel):
    Post: post
    votes: int
    
    class config:
        orm_mode = True

class usercreate(BaseModel):
    email: EmailStr
    password: str
        

class userlogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class tokenData(BaseModel):
    id: Optional[int] = None
    
class Vote(BaseModel):
    post_id : int
    dir: conint(le=1)

#from .schemas import userout
