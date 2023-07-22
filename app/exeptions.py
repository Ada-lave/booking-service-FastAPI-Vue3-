from fastapi import HTTPException, status

UserAlredyExistsExeption = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='user alredy exits'
)

IncorrectEmailOrPasswordExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='incorrect email or pass'
)

TokenExpiredExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='token is expired'
)

TokenAbsentExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='token is wrong'
)

UserIsNotExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED
    )