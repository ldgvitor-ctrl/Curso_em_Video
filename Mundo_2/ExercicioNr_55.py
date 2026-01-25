# ============================================================
# DESAFIO 055 - MAIOR E MENOR DA SEQUÊNCIA
# Objetivo: Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.
# ============================================================

pesos = []  # Lista para armazenar todos os pesos digitados

for c in range(1,6):
    peso = float(input(f"Qual e o peso da {c}ª pessoa? "))
    pesos.append(peso) # Adiciona o peso ao final da lista
# Organização e Análise dos Dados
pesos.sort()
# Exibição dos resultados usando índices da lista
# [0] pega o primeiro elemento (menor) e [-1] o último (maior)
print(f"O menor peso foi de {pesos[0]}Kg")
print(f"O maior peso foi de {pesos[-1]}Kg")