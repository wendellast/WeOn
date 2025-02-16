from http import HTTPStatus

from fastapi import FastAPI

from routers import reviews
from schemas.review import Message

app = FastAPI(title="Sentiment Analysis API")

app.include_router(reviews.router)


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá, bom dia! Acesse a rota /docs para testar a API."}
