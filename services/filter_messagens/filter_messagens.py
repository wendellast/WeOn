import re


def sanitize_sentiment(word: str) -> str:
    """
    Sanitiza a palavra de entrada para corresponder a um sentimento válido.

    Esta função remove quaisquer caracteres não alfabéticos da palavra de entrada,
    converte-a para minúsculas e verifica se corresponde a um dos sentimentos válidos
    ("positiva", "negativa", "neutra"). Se corresponder, a palavra limpa é retornada;
    caso contrário, "neutra" é retornada.

    Args:
        word (str): A palavra de entrada a ser sanitizada.

    Returns:
        str: O sentimento sanitizado, que será um dos "positiva", "negativa" ou "neutra".
    """

    cleaned_word = re.sub(r"[^a-zA-Z]", "", word).lower()

    valid_sentiments = {"positiva", "negativa", "neutra"}

    return cleaned_word if cleaned_word in valid_sentiments else "neutra"
