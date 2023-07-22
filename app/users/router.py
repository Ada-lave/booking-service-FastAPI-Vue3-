
from fastapi import APIRouter, Depends, HTTPException, Response, status
from .schemas import *
from .dao import UserDAO
from .auth import get_pass_hash, verify_pass, auntification_user, create_access_token
from .models import Users
from .dependencies import *
from app.exeptions import *

router = APIRouter(
    prefix='/auth',
    tags=["Auth & User"]
)

@router.post('/register')
async def register_user(user_data: sUserRegister):

    exist_user = await UserDAO.find_one_or_none(email=user_data.email)
    if exist_user:
        raise UserAlredyExistsExeption
    hashed_password = get_pass_hash(user_data.password)

    await UserDAO.add(email=user_data.email, hashed_password=hashed_password)
    


@router.post("/login")
async def login_user(user_data: sUserAuth, response: Response):
    user = await auntification_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordExeption
    access_token = create_access_token({"sub":str(user.id)})

    response.set_cookie("access_tk", access_token, httponly=True)

    return user

@router.post('/logout')
def logout_user(response: Response):
    response.delete_cookie('access_tk')
    return "user exit"

@router.get('/me')
def read_user(user: Users = Depends(get_current_user)):
    return user


@router.get('/all')
async def read_all_users(user: Users = Depends(get_current_admin_user)):
    return await UserDAO.find_all()
    


