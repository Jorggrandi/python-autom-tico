livros = ["Python", "Java", "C++"]

livros.append("JavaScript")
livros.remove("Java")

livros[0] = "GO"

print(len(livros))

for livro in livros:
    print(livro)
