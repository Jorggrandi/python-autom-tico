nome_input = input("Como é seu nome?")
idade_input = int(input("Quantos anos você tem?"))

registros = {
    "nome": nome_input,
    "idade": idade_input,
}

if registros["idade"] <= 18:
    print(f"Acesso negado para {registros['nome']}")
else:
    print(f"Acesso liberado para {registros['nome']}")
