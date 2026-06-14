pizza = 0
hamburguer = 0

while True:
    user_interact = input(
        "Selecione uma opção: \n" "1 - Pizza \n" "2 - Hamburguer\n" "3 - Sair\n"
    )

    match user_interact:
        case "1":
            pizza += 1
            print("Voto contabilizado com sucesso")
        case "2":
            hamburguer += 1
            print("Voto contabilizado com sucesso")
        case "3":
            break
        case __:
            print("Opção não encontrada campeão ;-;")

print(
    f"Votação encerrada! Os votos ficaram assim: Pizza -{pizza} & Hamburguer-{hamburguer}"
)
