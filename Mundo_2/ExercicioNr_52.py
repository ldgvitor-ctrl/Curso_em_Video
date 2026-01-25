# ============================================================
# DESAFIO 052 - NÚMEROS PRIMOS
# Objetivo: Faça um programa que leia um número inteiro e 
# diga se ele é ou não um número primo.
# Diferencial: Colorir os números divisíveis e contar as ocorrências.
# ============================================================
numero = int(input("Digite um número inteiro: "))
total = 0
for c in range(1, numero+ 1 ): # Laço que testa a divisibilidade de 1 até o próprio número
    if numero % c == 0:
        print("\033[33m", end=" ") # Amarelo: divisores encontrado
        total+=1
    else:
        print("\033[31m", end=" ") # Vermelho: não é divisor
    print(c, end=" ")

print(f"\n\033[mO número foi divisivel{numero} por {total} vezes")
if total == 2: # Verificação se é ou não primo
    print(f"E por isso ele É PRIMO!")
else:
    print(f"E por isso ele NÂO É PRIMO!")