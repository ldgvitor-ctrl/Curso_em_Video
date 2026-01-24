from random import choice # Importa a opção choice
aluno1 = str(input("Primeiro Aluno: "))
aluno2 = str(input("Segundo Aluno: "))
aluno3 = str(input("Terciero Aluno: "))
aluno4 = str(input("Quarto Aluno: "))
aluno = [aluno1, aluno2, aluno3, aluno4]
sorteado = choice(aluno) # Escolhe um nome aleatoriamente da lista
print(f"O aluno sorteado foi: {sorteado}")
