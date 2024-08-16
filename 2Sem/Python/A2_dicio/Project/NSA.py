from os import system
from time import sleep
system("cls")

# Functions
def VerifyThis(NewData):
    if isinstance(NewData, str):
        return NewData
    if isinstance(NewData, int):
        return NewData
    
    return "invalid"
    

# Dicts / Variables
notas = {}

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
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("1 - Adicionar novo Aluno | Nota")
            print("Lembre-se o limite é de 10 alunos")
            print("\n")
            sleep(1)
            system("pause")
            system("cls")
            # Temp Variables
            while True:
                NewName = VerifyThis(input("Aluno: "))
                if NewName == "invalid":
                    continue
                NewGrade = VerifyThis(input("Nota: "))
                if NewGrade == "invalid":
                    continue
                print("Aluno: {NewGrade} \n Nota: {NewName}")
                while True:
                    confirm = str(input("Confirm? (S/N) "))
                    match confirm:
                        case "S":
                            notas = {
                                {NewGrade} : {NewName}
                            }
                            info = 200
                            break
                        case "N":
                            break
                        case _:
                            print("Digite uma opção válida...")
                    break
                while True:
                    if info != 200:
                        opt = str(input("Tentar Novamente? (S/N) "))
                        if opt == "S":
                            retry = True
                            break
                        elif opt == "N":
                            retry = False
                            break
                        else:
                            print("Digite uma opção válida..")
                    break
                if retry == True:
                    print("Voltando..")
                    sleep(1)
                    print("\n")
                    system("pause")
                    system("cls")
                    continue
                    
                


        case 2:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("2 - Editar Aluno | Nota")
            print("\n")
            sleep(1)
            system("pause")


        case _:
            print("DIgite uma opção válida")
