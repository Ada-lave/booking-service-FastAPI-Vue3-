from fastapi import FastAPI, Query, Depends
import requests
from typing import Optional
from datetime import date
from pydantic import BaseModel
from app.bookings.router import router as router_booking
from app.users.router import router as router_user

app = FastAPI()
app.include_router(router_user)
app.include_router(router_booking)


class HotelsSearchArgs:
    def __init__(self,
                date_from: date, 
               date_to: date, 
               location: str, 
               starts: Optional[int] = Query(None, ge=1, le=5)
               ) -> None:
        self.date_from = date_from
        self.date_to = date_to
        self.location = location
        self.starts = starts 
        

class sHotels(BaseModel):
    address: str
    name: str
    stars: int


class sBooking(BaseModel):
    room_id: int
    count_room: int
    date_to: date
    date_from: date

@app.get("/hotels")
def get_hotels(search_args: HotelsSearchArgs = Depends()): 
    
    
    return search_args


