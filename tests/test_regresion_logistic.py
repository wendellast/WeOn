from services.regrecio_logisc.analite_category import classificar_mensagem

def test_classificar_mensagem():
    assert classificar_mensagem("O suporte resolveu meu problema rapidamente.") == "suporte"
    assert classificar_mensagem("A qualidade do produto é excelente.") == "produto"
    assert classificar_mensagem("O serviço foi muito rápido e eficiente.") == "serviço"
