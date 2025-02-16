## Requirements
- Python 3.13
- Docker

## Setup Instructions

1. **Create a Virtual Environment**
   ```sh
   python -m venv venv
   ```

2. **Activate the Virtual Environment**
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run Docker**
   ```sh
   docker compose up --build -d
   ```

5. **Apply Migrations**
   ```sh
   alembic upgrade head
   ```

6. **Access the API**
   - Open `http://127.0.0.1:8000` in your browser.
   - Visit `http://127.0.0.1:8000/docs` to test requests using Swagger.

## Routes
- **POST** `/reviews/` → Create a review
- **GET** `/reviews/` → List reviews
- **GET** `/reviews/id/{id}` → Get review by ID
- **GET** `/reviews/report` → Get review report


## Tasks
use o comando `task` no terminal para usa um dos atalhos abaixo:

- **Lint**: `task lint` (Check code formatting)
- **Fix Formatting**: `task correct` (Auto-format code)
- **Run Tests**: `task test` (Run tests with coverage)
- **Generate Coverage Report**: `task post_test` (Create HTML coverage report)

## Análise de Mensagens

Para a análise de sentimentos, o projeto está usando `llm` com `Llama-3.2-3B` hospedado no `Hugging Face`. Abaixo está o link do projeto:

- [hunface-llm](https://huggingface.co/collections/wendellast/weon-67afffa463fee231f49ac1b8)

Para a análise da categoria das mensagens, o projeto está usando uma `regressão logística`.
