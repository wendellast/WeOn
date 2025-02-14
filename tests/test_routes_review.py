import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from testcontainers.postgres import PostgresContainer

from database.database import get_db
from main import app
from models.review import table_registry
from routers.reviews import router

app.include_router(router)


@pytest.fixture(scope="session")
def engine():
    with PostgresContainer("postgres:17", driver="psycopg") as postgres:
        _engine = create_engine(postgres.get_connection_url())
        with _engine.begin():
            yield _engine


@pytest.fixture
def session(engine):
    table_registry.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    yield session
    session.rollback()
    table_registry.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def get_db_override():
        return session

    app.dependency_overrides[get_db] = get_db_override
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()


def test_create_review(client):
    """
    Teste a criação de uma nova avaliação.

    Args:
        client (TestClient): Cliente de teste para simular requisições HTTP.

    Verifica:
        - Se o status da resposta é 201 (Criado).
        - Se o texto da avaliação na resposta é igual ao texto enviado.
    """
    review_data = {"text": "This is a test review"}
    response = client.post("/reviews/", json=review_data)
    assert response.status_code == 201
    assert response.json()["text"] == review_data["text"]


def test_get_reviews(client):
    """
    Testa a rota GET /reviews/.

    Args:
        client: O cliente de teste.

    Asserts:
        - O status da resposta deve ser 200.
        - A resposta deve ser uma lista.
    """
    response = client.get("/reviews/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_review(client):
    """
    Teste a rota de obtenção de uma revisão.

    Este teste cria uma nova revisão usando a rota de POST e, em seguida,
    recupera a revisão criada usando a rota de GET. Verifica se o status
    da resposta é 200 (OK) e se o ID da revisão retornada corresponde ao
    ID da revisão criada.

    Parâmetros:
    client (TestClient): Cliente de teste para simular requisições HTTP.

    Asserções:
    - O status da resposta deve ser 200.
    - O ID da revisão retornada deve ser igual ao ID da revisão criada.
    """
    review_data = {"text": "This is a test review"}
    post_response = client.post("/reviews/", json=review_data)
    review_id = post_response.json()["id"]
    response = client.get(f"/reviews/id/{review_id}")
    assert response.status_code == 200
    assert response.json()["id"] == review_id


def test_get_review_report(client):
    """
    Teste a rota de relatório de avaliações.

    Este teste verifica se a rota de relatório de avaliações retorna um status
    code 200 e se a resposta JSON contém as chaves esperadas: "serviço",
    "produto" e "suporte".

    Parâmetros:
    - client: Cliente de teste para simular requisições HTTP.

    Passos:
    1. Define as datas de início e fim para o relatório.
    2. Faz uma requisição GET para a rota de relatório de avaliações com as datas definidas.
    3. Verifica se o status code da resposta é 200.
    4. Verifica se a resposta JSON contém as chaves "serviço", "produto" e "suporte".
    """
    start_date = "2025-01-01"
    end_date = "2025-12-20"
    response = client.get(
        f"/reviews/report?start_date={start_date}&end_date={end_date}"
    )
    assert response.status_code == 200
    assert "serviço" in response.json()
    assert "produto" in response.json()
    assert "suporte" in response.json()
