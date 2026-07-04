from pacote.formatador import upperText, lowerText
from pacote.par_impar import par_ou_impar

while True:
    option = int(
        input(
            "Olá, o que vamos fazer?  \n"
            "1 - Formatar texto para upper case  \n"
            "2 - Par ou impar \n"
            "3 - Formatar texto para lower case  \n"
        )
    )

    match option:
        case 1:
            texto = input("Digite seu texto para ser formatado: ")  
        case 2:
            num = int(input("Qual número deseja avaliar? "))
            par_ou_impar(num)
        case 3:
            texto = input("Digite seu texto para ser formatado: ")
            print(lowerText(texto))
        case __:
            print("Escolha uma opção válida bobão!")
