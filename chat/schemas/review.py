from datetime import datetime

from pydantic import BaseModel


class ReviewBase(BaseModel):
    text: str


class ReviewCreate(ReviewBase):
    pass


class ReviewResponse(ReviewBase):
    id: str
    sentiment: str
    created_at: datetime

    class Config:
        from_attributes = True


class ReviewReport(BaseModel):
    positive: int
    negative: int
    neutral: int

    class Config:
        alias_generator = lambda s: s.lower()
