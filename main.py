from fastapi import FastAPI

from routers import reviews

app = FastAPI(title="Sentiment Analysis API")

app.include_router(reviews.router)
