from fastapi import Request, HTTPException, Depends, status
from jose import jwt, JWTError
from app.config import settings
from datetime import datetime
from app.users.dao import UserDAO
from .models import Users
from app.exeptions import *

def get_token(request: Request):
    token = request.cookies.get("access_tk")

    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token

async def get_current_user(token: str = Depends(get_token)):

    try:
        payload = jwt.decode(
            token, settings.key, settings.crypt
        )
    except JWTError:
        raise TokenAbsentExeption

    expire: str = payload.get("exp")

    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredExeption
    
    user_id = payload.get('sub')

    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    user = await UserDAO.find_by_id(int(user_id))

    if not user:
        raise UserIsNotExeption
    
    return user


async def get_current_admin_user(user: Users = Depends(get_current_user)):
    return user



