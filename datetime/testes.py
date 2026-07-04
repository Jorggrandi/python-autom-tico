from datetime import datetime

artificial = "25/05/26 15:17"

formatado = datetime.strptime(artificial, "%d/%m/%y %H:%M")

print(formatado)


artificial = datetime(30, 9, 28, 21, 40, 55)

print(artificial)
