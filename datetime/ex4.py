from datetime import datetime

agora = datetime.now()
ano_novo = datetime(2027, 1, 1)

faltam = (ano_novo - agora).days

print(f"Faltam {faltam} dias para 2027")

