# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 092
# Tema: Cadastro de Trabalhador em Python
# Enunciado: Crie um programa que leia nome, ano de nascimento e carteira de 
#            trabalho e cadastre-o (com idade) em um dicionário. Se por acaso 
#            a CTPS for diferente de ZERO, o dicionário receberá também o 
#            ano de contratação e o salário. Calcule e acrescente, além da 
#            idade, com quantos anos a pessoa vai se aposentar.
# ==============================================================================
from datetime import datetime
trabalhador = {}

trabalhador['nome'] = input("Nome: ")
ano_de_nascimento = int(input("Data de nascimento: "))
trabalhador['idade'] = datetime.now().year - ano_de_nascimento
trabalhador['Cpts'] = int(input("Digite sua carteira de trabalho [0] se não tiver: "))

if trabalhador['Cpts'] != 0:
    trabalhador['contratação'] = int(input("Quando foi sua contratação: "))
    trabalhador['Salário'] = float(input("Qual é o seu salário? "))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - datetime.now().year)

print('-=' * 20)
print(f'Nome: {trabalhador["nome"]}')
print(f'Idade: {trabalhador["idade"]}')
print(f'CTPS: {trabalhador["Cpts"]}')

if trabalhador['Cpts'] > 0:
    print(f'Salário: R$ {trabalhador["Salário"]:.2f}')
    print(f'Contratação: {trabalhador["contratação"]}')
    print(f'Aposentadoria: {trabalhador["aposentadoria"]} anos')

