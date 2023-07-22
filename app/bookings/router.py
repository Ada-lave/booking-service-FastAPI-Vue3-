from fastapi import APIRouter, Request, Depends
from sqlalchemy import select
from app.database import async_session_maker
from .models import Bookings
from app.users.models import Users
from .dao import BookingDAO
from .schemas import *
from app.users.dependencies import *


router = APIRouter(prefix="/bookings",
                   tags=['booking'])


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[sBooking]:
    return await BookingDAO.find_all(user_id=user.id)

@router.post("")
async def add_bookings(date_from: date, date_to: date, room_id: int,
                        user: Users = Depends(get_current_user)):
   booking =  await BookingDAO.add(user.id, room_id, date_from, date_to)

   if booking is None:
       raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='rooms is left')