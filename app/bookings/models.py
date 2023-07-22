from app.database import Base
from sqlalchemy import Column, Integer, Date, Computed, String, JSON, ForeignKey

class Bookings(Base):
    __tablename__='bookings'

    id = Column(Integer, primary_key=True)
    room_id = Column(ForeignKey('rooms.id'))
    user_id = Column(ForeignKey('users.id'))

    date_to = Column(Date, nullable=False)
    date_from = Column(Date, nullable=False)
    price_day = Column(Integer, nullable=False)

    total_cost = Column(Integer, Computed("(date_to-date_from) * price_day"))
    total_days = Column(Integer, Computed("date_to-date_from"))