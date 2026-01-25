# ============================================================
# DESAFIO 056 - ANALISADOR COMPLETO
# Objetivo: Desenvolva um programa que leia o nome, idade e 
# sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.
# ============================================================
# Inicialização das variáveis (Os "baldes")
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher_20 = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    soma_idade += idade # Acumula a idade para a média
    
    # Lógica do Homem mais velho
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
        
    # Lógica das Mulheres menores de 20
    if sexo in 'Ff' and idade < 20:
        tot_mulher_20 += 1

media_idade = soma_idade / 4

print(f'A média de idade do grupo é de {media_idade} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.')
print(f'Ao todo são {tot_mulher_20} mulheres com menos de 20 anos.')
    