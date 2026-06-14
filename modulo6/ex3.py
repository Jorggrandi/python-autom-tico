num_input = float(input("Digite um número: "))

def par(numero):
    return numero % 2

if par(num_input) == 0:
    print(f"Sim! O algarismo {num_input} é par!")
else:
    print(f"Não, o dígito {num_input} não é par!")
