# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 074
# Tema: Tuplas (Variáveis Compostas)
# Enunciado: Crie um programa que vai gerar cinco números aleatórios e colocar 
#            em uma tupla. Depois disso, mostre a listagem de números gerados 
#            e também indique o menor e o maior valor que estão na tupla.
# ==============================================================================
from random import randint
numero = tuple(randint(1, 5) for _ in range(5))
print(f"A lista dos números é {numero}")
print(f"O menor número é {min(numero)} e o maior é {max(numero)}")