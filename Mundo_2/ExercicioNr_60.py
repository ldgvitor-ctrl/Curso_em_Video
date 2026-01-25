# ============================================================
# DESAFIO 060 - CÁLCULO DO FATORIAL
# Objetivo: Faça um programa que leia um número qualquer e 
# mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
# ============================================================
numero = int(input("Digite um número: "))
c = numero # Contador começa com o próprio número
f = 1 # Variável que acumula o resultado da multiplicação
print(f"Calculando o fatorial de {numero}!")
# Laço para realizar a multiplicação regressiva
while c > 0:
    print(f"{c}", end=" ")
    # Formatação visual: coloca 'x' entre os números e '=' no final
    print(" x " if c > 1 else " = ", end= " ")
    f *= c # Fatorial recebe ele mesmo vezes o contador
    c -= 1 # Decrementa o contador para a próxima rodada
print(f"{f}")