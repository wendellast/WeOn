#!/bin/bash
set -e



# Executa as migrations
echo "Executando migrations..."
alembic upgrade head

# Inicia a aplicação
echo "Iniciando aplicação..."
exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload
