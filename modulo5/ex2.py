numeros = []
# Armazena os itens


for n in range(1, 6):
    numero = int(input("Digite um valor: "))
    numeros.append(numero)

# Executa 6x o input de valores e os adiciona na lista numeros

resultado = 0
# Cria e define como 0 o resultado da expressão

for num in numeros:
    resultado += num
# Para cada numero em numeros some o resultado com o número da vez 

print(resultado)
# Printa o resultado da expressão