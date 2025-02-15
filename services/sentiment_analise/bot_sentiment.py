from gradio_client import Client


def analisar_sentimento(texto: str) -> str:
    """
    Analisa o sentimento de um texto fornecido.

    Args:
        texto (str): O texto a ser analisado.

    Returns:
        str: O resultado da análise de sentimento.
    """
    client = Client("wendellast/WeOn")
    result = client.predict(
        message=texto,
        system_message="",
        max_tokens=512,
        temperature=0.7,
        top_p=0.95,
        api_name="/chat",
    )
    return result
