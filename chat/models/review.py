import shortuuid
from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.orm import registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class Review:
    __tablename__ = "reviews"

    id = Column(String, primary_key=True, index=True, default=lambda: shortuuid.uuid())
    text = Column(String, nullable=False)
    sentiment = Column(String, nullable=False)
    category = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    def __init__(self, text, sentiment, category):
        self.text = text
        self.sentiment = sentiment
        self.category = category
