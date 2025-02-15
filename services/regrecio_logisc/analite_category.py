import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("dataset.csv")

frases = df["frase"].tolist()
acoes = df["acao"].tolist()

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(frases)
y = np.array(acoes)

test_size = 0.3
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Acurácia:", accuracy_score(y_test, y_pred))
print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred))

def classificar_mensagem(mensagem):
    X_novo = vectorizer.transform([mensagem])
    return model.predict(X_novo)[0]

nova_mensagem = """Essa equipe velha que nao sae de nada aff"""
print("Categoria prevista:", classificar_mensagem(nova_mensagem))
