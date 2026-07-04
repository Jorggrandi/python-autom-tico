# Pathlib

## Conceitos básicos
- `Path` representa um caminho de arquivo ou pasta.
- Caminho relativo: relativo ao diretório atual ou ao local de execução do script.
- Caminho absoluto: começa na raiz do sistema de arquivos.
- `Path.exists()` verifica se o arquivo ou pasta existe.

## Criar pastas
```python
from pathlib import Path

nova_pasta = Path("MINHAPASTA")
nova_pasta.mkdir(parents=True, exist_ok=True)
```
- `parents=True` cria pastas pai que ainda não existem.
- `exist_ok=True` não dá erro se a pasta já existir.

## Apagar pastas
```python
pasta = Path("MINHAPASTA")
pasta.rmdir()
```
- `rmdir()` só funciona se a pasta estiver vazia.
- Para apagar pastas com conteúdo use `shutil.rmtree()`.

## Apagar arquivos
```python
arquivo = Path("arquivo.txt")
arquivo.unlink()
```

## Ler arquivo com pathlib
```python
arquivo = Path("arquivo.txt")
texto = arquivo.read_text(encoding="utf-8")
```

## Escrever no arquivo
```python
arquivo.write_text("Olá, mundo!", encoding="utf-8")
```

## Listar arquivos em uma pasta
```python
pasta = Path(".")
for arquivo in pasta.iterdir():
    print(arquivo)
```
- Se usar `Path(".")`, lista o conteúdo da pasta atual.

## Filtrar arquivos
```python
for arquivo in pasta.glob("*.txt"):
    print(arquivo)
```
- `glob("*.txt")` lista arquivos com a extensão `.txt` na pasta atual.

## Propriedades de `Path`
- `path.name`: nome do arquivo ou pasta com extensão.
- `path.stem`: nome do arquivo sem extensão.
- `path.suffix`: extensão do arquivo.

## Criar arquivos
- `Path("arquivo.txt").touch()` cria um arquivo vazio se não existir.

## Listar arquivos em subpastas
```python
for arquivo in pasta.rglob("*"):
    print(arquivo)
```
- `rglob("*")` busca recursivamente em todas as subpastas.
