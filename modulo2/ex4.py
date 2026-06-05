print("Exercício Filme")

nota = int(input("Qual foi sua nota para esse filme?"))

if nota >= 9:
    print("Você achou esse filme excelente!")
elif nota == 8 or nota == 7:
    print("Vocẽ achou esse filme mediano")
elif nota == 6 or nota == 5:
    print("Você achou esse filme regular")
elif nota <5:
    print("Você achou esse filme ruim")