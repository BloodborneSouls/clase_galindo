from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import get_db
from jose import JWTError, jwt

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#Hola, estoy agregando un comentario de prueba para verificar el funcionamiento de Jenkins 




