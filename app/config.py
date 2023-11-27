from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname : str = 'localhost'
    database_port : int = 5432
    database_password : str = 'mohamed'
    database_name : str = 'fastapi'
    database_username : str = 'postgres'
    secret_key : str = 'password123' 
    algorithm :str = 'HS256'
    access_token_expire_minutes :int = 60
#  "password123"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 60

    class Config:
        env_lile = ".env"

# SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
# 'postgresql://postgres:mohamed@localhost:5432/fastapi'

settings = Settings()