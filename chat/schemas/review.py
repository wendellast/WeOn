from pydantic import BaseModel
from datetime import datetime

class ReviewBase(BaseModel):
    text: str

class ReviewCreate(ReviewBase):
    pass

class ReviewResponse(ReviewBase):
    id: int
    sentiment: str
    created_at: datetime

    class Config:
        orm_mode = True
