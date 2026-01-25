# ============================================================
# DESAFIO 070 - ESTATÍSTICAS EM PRODUTOS
# Objetivo: Crie um programa que leia o nome e o preço de 
# vários produtos. O programa deverá perguntar se o usuário 
# vai continuar. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$ 1000.
# C) qual é o nome do produto mais barato. 
# ============================================================,
print("=" * 30)
print(f"{'BANCO CEV':^30}")
print("=" * 30)

while True:
    try:
        valor = int(input("Que valor você quer sacar? R$ "))
        if valor <= 0:
            print("Valor inválido! Digite um valor positivo.")
            continue
        break
    except ValueError:
        print("Erro! Por favor, digite um número inteiro.")

total = valor
cedula = 50
total_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f"Total de {total_cedulas} cédulas de R${cedula}")
        
        # Lógica de troca de nota
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        
        total_cedulas = 0 # Reseta o contador para a próxima nota
        
        if total == 0:
            break

print("=" * 30)
print("Saque realizado com sucesso! Volte sempre.")