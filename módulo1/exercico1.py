from datetime import date

print("Hello, World")

anoNascimento = int(input("Em que ano você nasceu? \n"))
anoHoje = int(date.today().year)

result = anoHoje - anoNascimento

print(f'Legal! Você tem {result} anos')

