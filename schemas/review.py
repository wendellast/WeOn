from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ReviewBase(BaseModel):
    text: str


class ReviewCreate(ReviewBase):
    pass


class ReviewResponse(ReviewBase):
    id: str
    sentiment: str
    category: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SentimentCount(BaseModel):
    positive: int
    negative: int
    neutral: int

    model_config = ConfigDict(
        alias_generator=lambda s: s.lower(), populate_by_name=True
    )


class ReviewReport(BaseModel):
    serviço: SentimentCount
    produto: SentimentCount
    suporte: SentimentCount

    model_config = ConfigDict(
        alias_generator=lambda s: s.lower(), populate_by_name=True
    )
