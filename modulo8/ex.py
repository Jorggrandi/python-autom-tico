#### LET'S GO BABY
from random import randint

palpite_correto = randint(1, 10)

palpites = 0

while True:
    print("Bem vindo ao jogo da advinhação")

    palpite = int(input("Qual é seu palpite? "))

    if palpite == palpite_correto:
        print(f"Boa demais! Acertou - foram necessárias {(palpites)} tentativas ")
        break
    else:
        print("Iiiixeee, tá ruim demais.")
        palpites += 1

        if palpite < palpite_correto:
            print("Seu palpite foi muito abaixo homem.")
        if palpite > palpite_correto:
            print("Seu palpite foi muito acima homem.")
