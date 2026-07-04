import message
import matematica

user = input("Qual é seu nome? ")

message.welcome(user)

num = int(input(f"{user}, me fale um número: "))

print(
    f"{user}, a metade de {num} é {matematica.metade(num)}. E o dobro é {matematica.dobro(num)}"
)
