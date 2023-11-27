from fastapi import FastAPI
from . import models
from .databases import engine
from .routers import post, user,auth,vote
from .config import Settings
from fastapi.middleware.cors import CORSMiddleware


#models.Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = [
    "https://www.google.com",
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "welcome to my m,mmmmm"}