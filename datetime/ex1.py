from datetime import datetime

agora = datetime.now()

if agora.hour < 12:
    print("Bom dia!")

elif agora.hour < 18:
    print("Boa tarde!")

else:
    print("Boa noite!")
