from sqlalchemy import Column, Integer, String, DateTime, func
from chat.database.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    sentiment = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
