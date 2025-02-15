from typing import List

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

df = pd.read_csv("dataset.csv")

frases: List[str] = df["frase"].tolist()
acoes: List[str] = df["acao"].tolist()

vectorizer: TfidfVectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(frases)
y: np.ndarray = np.array(acoes)

test_size: float = 0.3
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=42
)

model: LogisticRegression = LogisticRegression()
model.fit(X_train, y_train)

y_pred: np.ndarray = model.predict(X_test)
# print("Acurácia:", accuracy_score(y_test, y_pred))
# print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred))


def classificar_mensagem(mensagem: str) -> str:
    """
    Classifica uma mensagem de texto em uma categoria predefinida.

    Args:
        mensagem (str): A mensagem de texto a ser classificada.

    Returns:
        str: A categoria predita para a mensagem.
    """
    X_novo = vectorizer.transform([mensagem])
    return model.predict(X_novo)[0]
