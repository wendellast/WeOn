from datetime import datetime

from pydantic import BaseModel


class ReviewBase(BaseModel):
    text: str


class ReviewCreate(ReviewBase):
    pass


class ReviewResponse(ReviewBase):
    id: str
    sentiment: str
    category: str
    created_at: datetime

    class Config:
        from_attributes = True


class SentimentCount(BaseModel):
    positive: int
    negative: int
    neutral: int

    class Config:
        alias_generator = lambda s: s.lower()
        allow_population_by_field_name = True


class ReviewReport(BaseModel):
    serviço: SentimentCount
    produto: SentimentCount
    suporte: SentimentCount

    class Config:
        alias_generator = lambda s: s.lower()
        allow_population_by_field_name = True
