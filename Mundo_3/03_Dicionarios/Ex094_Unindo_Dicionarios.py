# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 094
# Tema: Unindo dicionários e listas
# Enunciado: Crie um programa que leia nome, sexo e idade de várias pessoas, 
#            guardando os dados de cada pessoa em um dicionário e todos os 
#            dicionários em uma lista. No final, mostre: 
#            A) Quantas pessoas foram cadastradas.
#            B) A média de idade do grupo.
#            C) Uma lista com todas as mulheres.
#            D) Uma lista com todas as pessoas com idade acima da média.
#            Obs: O programa deve validar a entrada de sexo (M/F) e a 
#            continuidade (S/N) a cada cadastro.
# ==============================================================================
pessoas = {}
geral = []
soma = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input("Nome: ")).strip()
    
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoas['sexo'] in "MF":
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    
    pessoas['idade'] = int(input("Idade: "))
    geral.append(pessoas.copy()) 
    
    while True:
        pergunta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if pergunta in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
        
    if pergunta == "N":
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(geral)} pessoas cadastradas.')

for p in geral:
    soma += p['idade']
media = soma / len(geral)
print(f'B) A média de idade é de {media:5.2f} anos.')

print('C) As mulheres cadastradas foram: ', end='')
for p in geral:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()

print('D) Lista das pessoas que estão acima da média: ')
for p in geral:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')