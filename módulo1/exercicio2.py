# CALCULADORA SIMPLES

operation = int(input("Selecione uma operação: \n" \
"1 - Soma \n" \
"2 - Subtração \n" \
"3 - Multiplicação \n" \
"4 - Divisão \n"))

if operation == 1:
    input1 = int(input("Digite um número: \n"))    
    input2 = int(input("Digite outro número: \n"))
    result = input1+input2
    print(f"A soma de {input1} e {input2} é: {result}")

if operation == 2:
    input1 = int(input("Digite um número: \n"))    
    input2 = int(input("Digite outro número: \n"))    
    result = input1-input2
    print(f"A subtração de {input1} e {input2} é: {result}")

if operation == 3:
    input1 = int(input("Digite um número: \n"))    
    input2 = int(input("Digite outro número: \n"))   
    result = input1*input2
    print(f"A multiplicação de {input1} e {input2} é: {result}")

if operation == 4:
    input1 = int(input("Digite um número: \n"))    
    input2 = int(input("Digite outro número: \n"))    
    result = input1/input2
    print(f"A divisão de {input1} e {input2} é: {result}")
