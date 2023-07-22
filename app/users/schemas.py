from pydantic import BaseModel, EmailStr

class sUserRegister(BaseModel):
    email: EmailStr
    password: str

class sUserAuth(BaseModel):
    email: EmailStr
    password: str