from services.filter_messagens.filter_messagens import sanitize_sentiment
from services.sentiment_analise.bot_sentiment import analisar_sentimento

messagem_positiva = """
Fui muito bem atendido desde o início, e o problema foi resolvido sem nenhuma complicação. O  serviço foi prático, eficiente e me surpreendeu pela rapidez com que conseguiram resolver tudo. A comunicação também foi excelente, me mantendo informado a cada passo. Um atendimento realmente de qualidade.
"""

messagem_negativa= """
Não tive uma boa experiência. Precisei contatar o suporte diversas vezes até que uma solução adequada fosse finalmente apresentada. A falta de consistência nas respostas e a demora entre os contatos me deixaram bastante insatisfeito.  Era um problema simples de configuração, mas o processo todo acabou tomando muito mais tempo do que o necessário. """

messagem_neutra = """O sistema que utilizo tem funcionado bem, mas o suporte não foi tão eficiente quanto eu esperava. Tive que esperar bastante tempo por uma resposta e, quando ela finalmente veio, não era clara o suficiente para que eu pudesse seguir as instruções por conta própria. A
experiência foi mediana, espero que melhorem essa parte do serviço"""


def test_setiment_anlise():
    analise_positive = analisar_sentimento(messagem_positiva)
    analise_negative = analisar_sentimento(messagem_negativa)
    analise_neutra = analisar_sentimento(messagem_neutra)

    assert sanitize_sentiment(analise_positive) == "positiva"
    assert sanitize_sentiment(analise_negative) == "negativa"
    assert sanitize_sentiment(analise_neutra) == "neutra"

