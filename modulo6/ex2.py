nome_user = input("Qual é seu nome ?")
idade_user = int(input("Quantos anos você tem? "))


def apresentar(nome, idade):
    apresentador = print(f"Nome : {nome} | Idade : {idade}")
    return apresentador


apresentar(nome_user, idade_user)
