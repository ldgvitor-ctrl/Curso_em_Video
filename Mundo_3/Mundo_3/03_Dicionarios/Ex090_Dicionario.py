# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 090
# Tema: Dicionário em Python
# Enunciado: Faça um programa que leia nome e média de um aluno, 
#            guardando também a situação em um dicionário. 
#            No final, mostre o conteúdo da estrutura na tela.
#            (Situação: Média >= 7 "Aprovado", senão "Reprovado")
# ==============================================================================
lista = []
aluno = {}
while True:
    aluno['nome'] = str(input('Nome: ')).strip()
    aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
    if aluno['média'] >= 7:
        aluno['situação'] = 'aprovado'
    else:
        aluno['situação'] = 'reprovado'
    lista.append(aluno.copy())
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break

for aluno in lista:
    print(f"O aluno {aluno['nome']} teve a média {aluno['média']} e foi {aluno["situação"]}")