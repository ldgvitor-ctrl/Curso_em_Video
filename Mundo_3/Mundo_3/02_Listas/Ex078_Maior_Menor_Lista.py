# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 078
# Tema: Listas (Parte 1)
# Enunciado: Faça um programa que leia 5 valores numéricos e guarde-os em uma 
#            lista. No final, mostre qual foi o maior e o menor valor digitado 
#            e as suas respectivas posições na lista. 
# ==============================================================================

numero = list(int(input("Digite um valor: ")) for _ in range(5))
maior = max(numero)
menor = min(numero)
print(f"Você digitou os valores: {numero}")
print(f"O maior valor digitado foi {maior} nas posições ", end='')
for i, v in enumerate(numero):
    if v == maior:
        print(f"{i}... ", end='')

print(f"\nO menor valor digitado foi {menor} nas posições ", end='')
for i, v in enumerate(numero):
    if v == menor:
        print(f"{i}... ", end='')