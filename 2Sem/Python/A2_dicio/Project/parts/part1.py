from os import system
from time import sleep

# Functions - For tests
def VerifyThis(newData, type):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '1234567890'
    special = ',.'
    if type == str:
        for i in range(len(newData)):
            if newData[i].lower() not in letters:
                newData = False
                break
        return newData
    if type == int:
        for i in range(len(newData)):
            if newData[i] not in numbers:
                if newData[i] not in special:
                    newData = False
                    break
                if newData[i] == ',':
                    system("cls")
                    print(f"Favor use . ao invés de ,")
                    sleep(1)
                    print(f"{newData} foi alterado para {newData.replace(',', '.')} \n")
                    system("pause")
                    newData = newData.replace(',', '.')
        return float(newData)
    return False

# Dicts / Variables
notas = {
    'lara': 1.0,
    'lara': 1.0,
    'lara': 1.0,
    'lara': 1.0,
    'lara': 1.0,
    'lara': 1.0,
    'lara': 1.0,
    'lara': 1.0,
    'lara': 1.0
}



while True:
    system("cls")
    newAluno = VerifyThis(input("Aluno: "), str)
    if newAluno == False:
        print(f"Inválido \n")
        system("pause")
        continue
    newNota = VerifyThis(input("Nota: "), int)
    if newNota == False:
        print(f"Inválido \n")
        system("pause")
        continue
    while True: 
        system("cls")
        print(f"Aluno: {newAluno} \nNota: {newNota}")
        confirm = input("Confirma? (S/N): ")
        match confirm.upper():
            case 'S':
                notas[newAluno] = newNota
                print(f'Adicionado! \n')
                system("pause")
                system("cls")
                break
            case 'N':
                break
            case _:
                print("Digite um valor válido.")
        break
    if len(notas) < 10:
        while True:
            retry = input("Adicionar outro? (S/N): ")
            match confirm.upper():
                case 'S':
                    break
                case 'N':
                    retry == False
                    break
                case _:
                    print("Digite um valor válido.")
            break
        if retry == False:
            break
        else:
            continue
    print("Limite de 10 Aluno excedido.")
    break
    
            

