palavra = input("Digite uma palavra: ")
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

fatiamento = palavra[(num1-1):num2]

print(f"Seu fatiamento ficou assim {fatiamento}")