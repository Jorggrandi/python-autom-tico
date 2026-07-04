from datetime import datetime

nome_input = input("Qual é seu nome?")


def assine(nome):
    agora = datetime.now()
    mensagem = agora.strftime(
        f"Documento assinado por {nome} às %H:%M do dia %d de %B de %Y"
    )
    return print(mensagem)


assine(nome_input)
