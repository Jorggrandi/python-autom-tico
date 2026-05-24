import time

nomeUser = input("Como é seu nome? ")

print(f"Olá, {nomeUser}! Vamos calcular suas notas escolares.")
time.sleep(1.5)

print()


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a última nota: "))

operations = [nota1 ,nota2 , nota3]

result = sum(operations) / len(operations)

print()
print()

time.sleep(2)

if result <= 80:
    print(f"Sua média é de {result}, estude mais garoto!")
else:
    print(f"Sua média foi de {result}, continue assim garoto!")