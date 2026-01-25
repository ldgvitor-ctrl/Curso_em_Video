# ============================================================
# DESAFIO 061 - PROGRESSÃO ARITMÉTICA V2.0
# Objetivo: Refaça o DESAFIO 051, lendo o primeiro termo e 
# a razão de uma PA, mostrando os 10 primeiros termos da 
# progressão usando a estrutura while.
# ============================================================
primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro_termo
count = 1 
# O laço vai rodar até mostrar 10 termos
while count <= 10:
    print(f"{termo} -> ", end="")
    termo += razao  # Calcula o próximo termo somando a razão
    count += 1 # Incrementa o contador para não travar o programa
print("FIM")

