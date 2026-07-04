from datetime import datetime

evento = input("Quando é seu evento? (YYYY/MM/DD) ")
agora = datetime.now()

formatar_evento = datetime.strptime(evento, "%Y/%m/%d")

if formatar_evento.day == agora.day and formatar_evento.month == agora.month:
    print("Não esqueça do seu evento!!!")
elif formatar_evento < agora:
    print("Sinto muito, você esqueceu seu evento")
else:
    print("Callmaa, tem tempo ainda")
