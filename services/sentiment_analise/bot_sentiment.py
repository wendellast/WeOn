from gradio_client import Client

client = Client("wendellast/WeOn")


def analise_sentiment(message: str) -> str:
    """
    Envia uma mensagem para o cliente e retorna a resposta.

    Args:
        message (str): A mensagem a ser enviada.

    Returns:
        str: A resposta do cliente.
    """
    result = client.predict(
        message=message,
        system_message="",
        max_tokens=20,
        temperature=0.7,
        top_p=0.95,
        api_name="/chat",
    )
    return result
