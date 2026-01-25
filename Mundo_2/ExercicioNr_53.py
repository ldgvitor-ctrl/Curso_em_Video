# ============================================================
# DESAFIO 053 - DETECTOR DE PALÍNDROMO
# Objetivo: Crie um programa que leia uma frase qualquer e 
# diga se ela é um palíndromo, desconsiderando os espaços.
# ============================================================

frase = str(input("Digite uma frase: ")).strip().lower()
limpa = frase.replace(" ","")
inverso = limpa[::-1]
print(f"O inverso de {frase} é {inverso}")
if limpa == inverso:
    print(f"A frase {frase} é um palíndromo! ")
else:
    print(f"A frase {frase} não é um palíndromo")