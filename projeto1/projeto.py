alunos_turma = []


def adicionar_aluno():
    nome_aluno = input("Qual o nome do aluno? ")
    idade_aluno = int(input("Quantos anos o aluno tem? "))
    nota_aluno = int(input("Qual foi a nota desse aluno? "))

    id_aluno = len(alunos_turma) + 1

    alunos_turma.append(
        {
            "id": id_aluno,
            "nome": nome_aluno,
            "idade": idade_aluno,
            "nota_aluno": nota_aluno,
        }
    )

    print(f"Aluno Adicionado | ID: {id_aluno}")


def listar_alunos():

    if len(alunos_turma) == 0:
        print("Nenhum aluno adicionado.")
    else:
        print("Listando todos os alunos.")
        for aluno in alunos_turma:
            print(
                f"{aluno["nome"]} - {aluno["idade"]} anos | Nota: {aluno["nota_aluno"]}"
            )
            print("")


def buscar_aluno():
    busca = input("Qual aluno deseja buscar? ")
    for aluno in alunos_turma:
        if aluno["nome"] == busca:
            print(
                f"{aluno["nome"]} - {aluno["idade"]} anos | Nota: {aluno["nota_aluno"]}"
            )
        else:
            print("Aluno não encontrado")


def remover_aluno():
    aluno_removido = input("Qual aluno deseja remover?")

    for aluno in alunos_turma:
        if aluno["nome"] == aluno_removido:
            alunos_turma.remove(aluno)


def verificar_media():
    notas = 0
    for aluno in alunos_turma:
        notas += aluno["nota_aluno"]

    media = notas / len(alunos_turma)
    print(f"A média da sua turma é {media}")


while True:
    funcionalidade_escolhida = int(
        input(
            "O que vamos fazer hoje? \n"
            "1 - Adicionar aluno \n"
            "2 - Listar alunos \n"
            "3 - Buscar alunos \n"
            "4 - Remover aluno \n"
            "5 - Verificar média \n"
            "6 - Sair \n"
        )
    )

    # Pular linha
    print("")

    match funcionalidade_escolhida:
        case 1:
            adicionar_aluno()
        case 2:
            listar_alunos()
        case 3:
            buscar_aluno()
        case 4:
            remover_aluno()
        case 5:
            verificar_media()
        case 6:
            print("Encerrando sistema. Até a próxima 👋")
            break
