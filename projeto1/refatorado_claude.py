alunos_turma = []


def ler_inteiro(mensagem):
    """Pede um número ao usuário até que ele digite algo válido."""
    while True:
        valor = input(mensagem)
        if valor.isdigit():
            return int(valor)
        print("Por favor, digite um número válido.\n")


def exibir_aluno(aluno):
    """Mostra os dados de um aluno em um formato padrão."""
    print(f"{aluno['nome']} - {aluno['idade']} anos | Nota: {aluno['nota_aluno']}")


def adicionar_aluno():
    nome_aluno = input("Qual o nome do aluno? ")
    idade_aluno = ler_inteiro("Quantos anos o aluno tem? ")
    nota_aluno = ler_inteiro("Qual foi a nota desse aluno? ")

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
    if not alunos_turma:
        print("Nenhum aluno adicionado.")
        return

    print("Listando todos os alunos.")
    for aluno in alunos_turma:
        exibir_aluno(aluno)
        print("")


def buscar_aluno():
    busca = input("Qual aluno deseja buscar? ")

    for aluno in alunos_turma:
        if aluno["nome"] == busca:
            exibir_aluno(aluno)
            return

    print("Aluno não encontrado.")


def remover_aluno():
    nome_busca = input("Qual aluno deseja remover? ")

    for aluno in alunos_turma:
        if aluno["nome"] == nome_busca:
            alunos_turma.remove(aluno)
            print(f"Aluno {nome_busca} removido com sucesso.")
            return

    print("Aluno não encontrado.")


def verificar_media():
    if not alunos_turma:
        print("Não há alunos cadastrados para calcular a média.")
        return

    notas = sum(aluno["nota_aluno"] for aluno in alunos_turma)
    media = notas / len(alunos_turma)
    print(f"A média da sua turma é {media:.2f}")


while True:
    funcionalidade_escolhida = ler_inteiro(
        "O que vamos fazer hoje? \n"
        "1 - Adicionar aluno \n"
        "2 - Listar alunos \n"
        "3 - Buscar alunos \n"
        "4 - Remover aluno \n"
        "5 - Verificar média \n"
        "6 - Sair \n"
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
        case _:
            print("Opção inválida! Escolha um número entre 1 e 6.\n")
