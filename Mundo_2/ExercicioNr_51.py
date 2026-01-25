# ============================================================
# DESAFIO 051 - PROGRESSÃO ARITMÉTICA
# Objetivo: Desenvolver um programa que leia o primeiro termo 
# e a razão de uma PA. No final, mostre os 10 primeiros termos 
# dessa progressão.
# ============================================================
print("="*20)
print(" 10 TERMOS DE UMA PA ")
print("="*20)

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

# Fórmula matemática para descobrir o 10º termo
# decimo = primeiro + (quantidade_de_termos - 1) * razao
decimo_termo = primeiro_termo + ( 10 - 1) * razao

# O range vai do 'primeiro' até o 'decimo', pulando de 'razao' em 'razao'
# Somamos +razao no final do range porque o Python sempre para um número antes
for c in range(primeiro_termo, decimo_termo + razao, razao):
    print(f"{c}", end=" -> ")
print("ACABOU")