# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 096
# Tema: Funções para calcular área
# Enunciado: Faça um programa que tenha uma função chamada area(), que receba 
#            as dimensões de um terreno retangular (largura e comprimento) 
#            e mostre a área do terreno.
# ==============================================================================

def área(largura, comprimento):
    a = largura * comprimento
    print(f"A aréa do terreno com {largura} x {comprimento} é {a}m²")

print(" Terreno")
print("-"*20)
larg = float(input("Qual é a largura (m)? "))
comprim = float(input("Qual é o comprimento (m)? "))
área(larg,comprim)