print("Bem vindo ao mini NSA")
print( """
    1 - Adicionar novo Aluno | Nota (limite 10 alunos)
    2 - Editar Aluno | Nota
    3 - Listar os Alunos
    4 - Excluir um Aluno
    5 - Calcular a média da turma
    6 - Consultar um aluno
    7 - Apagar todos os alunos da sala
""")
key = 1
while key != 0:
    option = int(input("Digite sua Opção: "))
    match option:
        case 1:
            print("As vozes não param")
        case _:
            print("DIgite uma opção válida")
