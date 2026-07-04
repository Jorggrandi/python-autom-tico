from datetime import datetime, timedelta

vencimento_input = input("Quando seu produto vence? (DD/MM/AAAA) ")
vencimento = datetime.strptime(vencimento_input, "%d/%m/%Y")

hoje = datetime.now()

# Vencimento limite = 180
diferenca = (vencimento - hoje).days

if diferenca == 0:
    print(
        vencimento.strftime(
            f"Seu produto com validade em %d/%m/%y vence hoje, fique atento!"
        )
    )

elif diferenca > 1:
    print(
        vencimento.strftime(
            f"Seu produto vence no dia %d de %B de %Y, portanto ainda restam {diferenca} dias para seu produto vencer"
        )
    )

else:
    print(
        vencimento.strftime(
            f"Seu produto com vencimento no dia %d de %B de %Y, portanto ainda está vencido {abs(diferenca)} dias"
        )
    )
