from random import shuffle # Importa a opção shuffle
aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista) # Embaralha aleatoriamente a lista
print("Aordem de apresentação será! ")
print(lista)