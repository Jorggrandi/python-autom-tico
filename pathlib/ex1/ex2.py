from pathlib import Path

file1 = Path("dados/entrada/log1.txt").touch(exist_ok=True)
file2 = Path("dados/entrada/log2.txt").touch(exist_ok=True)
file3 = Path("dados/entrada/log3.txt").touch(exist_ok=True)


### CRIAMOS ARQUIVOS DENTRO DA PASTA ENTRADA