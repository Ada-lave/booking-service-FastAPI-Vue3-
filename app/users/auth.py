from passlib.context import CryptContext
from pydantic import EmailStr
from fastapi import APIRouter, HTTPException
from .schemas import *
from .dao import UserDAO
from datetime import datetime, timedelta
from jose import jwt
from app.config import settings


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def get_pass_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_pass(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=1)
    to_encode.update({'exp':expire})
    encoded_jwt = jwt.encode(to_encode, settings.key, settings.crypt)

    return encoded_jwt


async def auntification_user(email: EmailStr, password: str):
    user = await UserDAO.find_one_or_none(email=email)


    if not user and not verify_pass(password, user.hashed_password):
        return None

    return user