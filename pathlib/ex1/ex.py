from pathlib import Path

entrada = Path("dados/entrada")
saida = Path("dados/saída")
relatorios = Path("relatórios")

entrada.mkdir(exist_ok=True, parents=True)
saida.mkdir(exist_ok=True, parents=True)
relatorios.mkdir(exist_ok=True, parents=True)

### CRIAMOS PASTAS