## Requisitos
- Python 3.13
- Docker

## Pode acessar o deploy de teste aqui abaixo

- [Deploy Teste do Projeto](https://hublast.com/weon/docs)

## Instruções de Configuração

1. **Crie um Ambiente Virtual**
    ```sh
    python -m venv venv
    ```

2. **Ative o Ambiente Virtual**
    - No Windows:
      ```sh
      venv\Scripts\activate
      ```
    - No macOS/Linux:
      ```sh
      source venv/bin/activate
      ```

3. **Instale as Dependências**
    ```sh
    pip install -r requirements.txt
    ```

4. **Execute o Docker**
    ```sh
    docker compose up --build -d
    ```

5. **Aplique as Migrações**
    ```sh
    alembic upgrade head
    ```

6. **Acesse a API**
    - Abra `http://127.0.0.1:8000` no seu navegador.
    - Visite `http://127.0.0.1:8000/docs` para testar requisições usando Swagger.

## Rotas
- **POST** `/reviews/` → Criar uma avaliação
- **GET** `/reviews/` → Listar avaliações
- **GET** `/reviews/id/{id}` → Obter avaliação por ID
- **GET** `/reviews/report` → Obter relatório de avaliações
- **GET** `/docs` → Testar API com Swagger

## Tarefas
Use o comando `task` no terminal para usar um dos atalhos abaixo:

- **Lint**: `task lint` (Verificar formatação do código)
- **Corrigir Formatação**: `task correct` (Auto-formatar código)
- **Executar Testes**: `task test` (Executar testes com cobertura)
- **Gerar Relatório de Cobertura**: `task post_test` (Criar relatório de cobertura em HTML)

## Análise de Mensagens

Para a análise de sentimentos, o projeto está usando `llm` com `Llama-3.2-3B` hospedado no `Hugging Face`. Abaixo está o link do projeto:

- [hunface-llm](https://huggingface.co/collections/wendellast/weon-67afffa463fee231f49ac1b8)

Para a análise da categoria das mensagens, o projeto está usando uma `regressão logística`.
