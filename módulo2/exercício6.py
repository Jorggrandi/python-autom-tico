print("Bem vindo ao nosso restaurante.")
print()

pedido = int(input("Faça seu pedido \n" \
"1 - Pizza \n" \
"2 - Feijoada \n" \
"3 - Sushi \n"))

match pedido: 
    case 1: 
        print("Sua pizza ficará pronta em 45 minutos")
    case 2: 
        print("Sua feijoada ficará pronta em 30 minutos")
    case 3: 
        print("Seu sushi saí em 50 minutos")
    case _:
        print("Escolha uma opção válida")



