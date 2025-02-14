from datetime import datetime, timedelta
from typing import Dict, List, Optional

from models.review import Review
from schemas.review import ReviewCreate
from sqlalchemy import func
from sqlalchemy.orm import Session


def create_review(db: Session, review: ReviewCreate, sentiment: str) -> Review:
    """
    Cria uma nova avaliação no banco de dados.

    Args:
        db (Session): Sessão do banco de dados do SQLAlchemy.
        review (ReviewCreate): Dados necessários para criar uma nova avaliação.
        sentiment (str): Resultado da análise de sentimento para a avaliação.

    Returns:
        Review: O objeto da avaliação recém-criada.
    """

    sentiment = "negative"
    db_review = Review(text=review.text, sentiment=sentiment)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_review(db: Session, review_id: str) -> Optional[Review]:
    """
    Recupera uma avaliação pelo seu ID (shortuuid).

    Args:
        db (Session): Sessão do banco de dados do SQLAlchemy.
        review_id (str): ID da avaliação (shortuuid) a ser recuperada.

    Returns:
        Optional[Review]: O objeto da avaliação se encontrado, caso contrário None.
    """
    return db.query(Review).filter(Review.id == review_id).first()


def get_reviews(db: Session, skip: int = 0, limit: int = 10) -> List[Review]:
    """
    Recupera uma lista de avaliações com paginação opcional.

    Args:
        db (Session): Sessão do banco de dados do SQLAlchemy.
        skip (int): Número de registros a serem ignorados. O padrão é 0.
        limit (int): Número máximo de registros a serem recuperados. O padrão é 10.

    Returns:
        List[Review]: Lista de objetos de avaliação.
    """
    return db.query(Review).offset(skip).limit(limit).all()


def get_review_report(
    db: Session, start_date: datetime, end_date: datetime
) -> Dict[str, int]:
    """
    Retorna um relatório das avaliações realizadas em um período específico.

    Args:
        db (Session): Sessão do banco de dados.
        start_date (datetime): Data inicial.
        end_date (datetime): Data final.

    Returns:
        Dict[str, int]: Relatório contendo a contagem de avaliações por sentimento.
    """

    end_date = end_date + timedelta(days=1) - timedelta(seconds=1)

    report = (
        db.query(Review.sentiment, func.count(Review.sentiment).label("count"))
        .filter(Review.created_at >= start_date, Review.created_at <= end_date)
        .group_by(Review.sentiment)
        .all()
    )

    print("Report:", report)

    result = {sentiment: count for sentiment, count in report}
    for sentiment in ["positive", "negative", "neutral"]:
        result.setdefault(sentiment, 0)

    return result
