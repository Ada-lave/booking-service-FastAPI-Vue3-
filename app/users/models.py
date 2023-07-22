from app.database import Base
from sqlalchemy import Column, Integer, Date, Computed, String, JSON, ForeignKey

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)