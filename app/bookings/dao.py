from sqlalchemy import and_, insert, or_, select, func 
from app.database import async_session_maker
from .models import Bookings
from app.dao.base import BaseDAO
from datetime import date
from app.rooms.models import Rooms
from app.database import engine

class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(cls, user_id, room_id, date_from: date, date_to: date):
        '''
            
with booked_rooms as (
	select * from bookings
	where room_id = 1 and (date_from >= '2023-05-15' and date_from <='2023-06-20') or
	(date_from <= '2023-05-15' and date_to > '2023-05-15') 
)

select rooms.quantity - count(booked_rooms.room_id) from rooms
left join booked_rooms on booked_rooms.room_id = rooms.id
where rooms.id = 1
group by rooms.quantity, booked_rooms.room_id
        '''
        async with async_session_maker() as session:
            booked_rooms = select(Bookings).where(
                and_(
                    Bookings.room_id == 1, 
                    or_(
                        and_(
                            Bookings.date_from >= date_from,
                            Bookings.date_from <=date_to
                        ),
                        and_(
                            Bookings.date_from >= date_from,
                            Bookings.date_to >= date_from
                        ),

                    )
                )).cte("booked_rooms")
            
            rooms_left = select(
                                Rooms.quantity - func.count(booked_rooms.c.room_id)
                                ).select_from(Rooms).join(
                                    booked_rooms, booked_rooms.c.room_id == Rooms.id 
                                ).where(Rooms.id == room_id).group_by(
                                    Rooms.quantity, booked_rooms.c.room_id
                                )
            
            
            print(rooms_left.compile(engine, compile_kwargs={"literal_bind":True}))
            rooms_left = await session.execute(rooms_left)
            rooms_left = rooms_left.scalar()
            print(rooms_left)
            if rooms_left > 0:
                get_price = select(Rooms.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price: int = price.scalar()
                
                add_booking = insert(Bookings).values(
                    room_id = room_id,
                    user_id=user_id,
                    date_from=date_from,
                    date_to=date_to,
                    price_day=price
                ).returning(Bookings)
                
                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.scalar()
            else:
                return None
