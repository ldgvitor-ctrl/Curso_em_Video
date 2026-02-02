# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 089
# Tema: Boletim com listas compostas
# Enunciado: Crie um programa que leia nome e duas notas de vários alunos 
#            e guarde tudo em uma lista composta. No final, mostre um 
#            boletim contendo a média de cada um e permita que o usuário 
#            possa mostrar as notas de cada aluno individualmente.
# ==============================================================================
ficha = list()

while True:
    nome = str(input("Nome: ")).strip()
    # Loop para validar as notas
    while True:
        try:
            nota1 = float(input("Nota 1: "))
            nota2 = float(input("Nota 2: "))
            if nota1 < 0 or nota2 < 0:
                print("ERRO: As notas não podem ser negativas!")
                continue
            break # Sai do loop das notas se estiver tudo OK
        except ValueError:
            print("ERRO: Digite apenas números para as notas!")

    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    # Loop para validar a continuação
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    
    if resp == 'N':
        break

# --- EXIBIÇÃO DO BOLETIM ---
print('-=' * 15)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

# --- CONSULTA INDIVIDUAL ---
while True:
    print('-' * 35)
    try:
        opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        if opc == 999:
            break
        if opc >= len(ficha) or opc < 0:
            print(f"ERRO: Aluno com índice {opc} não existe!")
        else:
            print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    except ValueError:
        print("ERRO: Digite um número inteiro válido!")

print('<<< VOLTE SEMPRE >>>')