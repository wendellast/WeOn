from datetime import datetime
from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from controler import review as crud_review
from database.database import get_db
from schemas.review import (
    ReviewCreate,
    ReviewReport,
    ReviewResponse,
    SentimentCount,
)

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.post("/", status_code=HTTPStatus.CREATED, response_model=ReviewResponse)
def create_review(
    review: ReviewCreate, db: Session = Depends(get_db)
) -> ReviewResponse:
    """
    Cria uma nova review com classificação de sentimento.

    Args:
        review (ReviewCreate): Dados da review a ser criada.
        db (Session): Sessão do banco de dados (dependência).

    Returns:
        ReviewResponse: A review criada com a classificação de sentimento.
    """

    db_review: ReviewResponse = crud_review.create_review(db=db, review=review)
    return db_review


@router.get("/", response_model=List[ReviewResponse])
def get_reviews(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db),
) -> List[ReviewResponse]:
    """
    Retorna uma lista de reviews com paginação.

    Args:
        skip (int): Número de reviews a pular (padrão: 0).
        limit (int): Número máximo de reviews a retornar (padrão: 10).
        db (Session): Sessão do banco de dados (dependência).

    Returns:
        List[ReviewResponse]: Lista de reviews.
    """
    reviews: List[ReviewResponse] = crud_review.get_reviews(
        db=db, skip=skip, limit=limit
    )
    return reviews


@router.get("/id/{id}", response_model=ReviewResponse)
def get_review(id: str, db: Session = Depends(get_db)) -> ReviewResponse:
    """
    Retorna uma review pelo seu ID.

    Args:
        id (str): ID da review.
        db (Session): Sessão do banco de dados (dependência).

    Raises:
        HTTPException: Se a review não for encontrada, retorna 404.

    Returns:
        ReviewResponse: A review correspondente ao ID fornecido.
    """
    review: ReviewResponse = crud_review.get_review(db=db, review_id=id)
    if not review:
        raise HTTPException(status_code=404, detail="Review não encontrada")
    return review


@router.get("/report", response_model=ReviewReport)
def get_review_report(
    start_date: str = Query(..., description="Data inicial no formato YYYY-MM-DD"),
    end_date: str = Query(..., description="Data final no formato YYYY-MM-DD"),
    db: Session = Depends(get_db),
) -> ReviewReport:
    """
    Retorna um relatório detalhado das avaliações em um período específico, incluindo a contagem
    por categoria (serviço, produto, suporte) e a classificação por sentimento (positiva, negativa, neutra).

    Args:
        start_date (str): Data inicial no formato YYYY-MM-DD.
        end_date (str): Data final no formato YYYY-MM-DD.
        db (Session): Sessão do banco de dados.

    Returns:
        ReviewReport: Relatório contendo a contagem de avaliações por categoria e sentimento.
    """
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Formato de data inválido. Use YYYY-MM-DD.",
        )

    report_data = crud_review.get_review_report(db=db, start_date=start, end_date=end)

    report = ReviewReport(
        serviço=SentimentCount(**report_data["serviço"]),
        produto=SentimentCount(**report_data["produto"]),
        suporte=SentimentCount(**report_data["suporte"]),
    )

    return report
