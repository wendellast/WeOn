from textblob import TextBlob


def classify_sentiment(text: str) -> str:
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0.1:
        return "Positiva"
    elif analysis.sentiment.polarity < -0.1:
        return "Negativa"
    else:
        return "Neutra"
