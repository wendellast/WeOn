import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from testcontainers.postgres import PostgresContainer

from database.database import get_db
from main import app
from models.review import Review, table_registry


@pytest.fixture(scope="session")
def engine():
    with PostgresContainer("postgres:17", driver="psycopg") as postgres:
        _engine = create_engine(postgres.get_connection_url())
        with _engine.begin():
            yield _engine


@pytest.fixture(scope="function")
def session(engine):
    """Cria uma nova sessão para cada teste usando PostgreSQL em container."""
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    table_registry.metadata.create_all(bind=engine)

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def client(session):
    def get_db_override():
        return session

    app.dependency_overrides[get_db] = get_db_override
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()


def test_create_review(session):
    """
    Testa a criação de uma nova avaliação no banco de dados.

    Este teste cria uma nova avaliação com o texto "Ótimo serviço!",
    sentimento "positive" e categoria "serviço". Em seguida, adiciona
    a avaliação à sessão e realiza o commit. Após isso, recupera a
    avaliação do banco de dados e verifica se os dados armazenados
    correspondem aos dados fornecidos.

    Args:
        session: Sessão do banco de dados utilizada para adicionar e
                 recuperar a avaliação.
    """
    new_review = Review(text="Ótimo serviço!", sentiment="positive", category="serviço")
    session.add(new_review)
    session.commit()

    review = session.scalar(select(Review).where(Review.text == "Ótimo serviço!"))

    assert {
        "id": review.id,
        "text": review.text,
        "sentiment": review.sentiment,
        "category": review.category,
        "created_at": review.created_at,
    } == {
        "id": review.id,
        "text": "Ótimo serviço!",
        "sentiment": "positive",
        "category": "serviço",
        "created_at": review.created_at,
    }
