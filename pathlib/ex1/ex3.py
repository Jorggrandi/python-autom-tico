from pathlib import Path

entrada_pasta = Path("dados/entrada")

for arquivo in entrada_pasta.glob("*.txt"):
    print(arquivo.stem)

# MAPEAMOS ARQUIVOS DENTRO DA PASTA
