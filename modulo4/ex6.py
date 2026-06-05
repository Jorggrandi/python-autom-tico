info_corretas = {
    "user": "Admin",
    "password": "ADMIN123",
}

user_add = input("Digite seu usuário: ")
password_add = input("Digite sua senha: ")

info_userAdd = {
    "user": user_add,
    "password": password_add,
}

if (
    info_userAdd["user"] == info_corretas["user"]
    and info_userAdd["password"] == info_corretas["password"]
):
    print("Acesso liberado! Chegue mais...")

else:
    print("Sai daqui coisa feia!")
