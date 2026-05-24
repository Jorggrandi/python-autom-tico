print("MEIO DE TRANSPORTE")

veiculo = input("Digite seu principal meio de transporte. ")

match veiculo:
    case "Carro"| "Moto":
        print("Seu veículo é terrestre.")
    case "Avião" | "Helicóptero":
        print("Carai mané tu sabe voar!")
    case "Submarino" | "Navio":
        print("Concorrente do aquaman")
    case __:
        print("Opção não identificada.")