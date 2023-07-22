from pydantic import BaseModel
from datetime import date

class sBooking(BaseModel):
    id: int
    room_id: int
    user_id: int

    date_to: date
    date_from: date
    price_day: int

    total_cost: int
    total_days: int

    class Config:
        from_atribute = True