# ==============================================================================
# Desafio: 107
# Tema: Exercitando Módulos em Python
# Enunciado: Crie um módulo chamado moeda.py que tenha as funções incorporadas 
#            aumentar(), diminuir(), dobro() e metade(). Faça também um 
#            programa que importe esse módulo e use algumas dessas funções.
# ==============================================================================
from modulos.cores import *
from modulos import moeda107

n = int(input("Quanto foi o produto? "))
dob = moeda107.dobro(n)
met = moeda107.metade(n)
dimi= moeda107.diminuir(n)
aum = moeda107.aumentar(n)
print(f"O dobro de {n} é {verde(moeda107.dobro(n))}")
print(f"A metade de {n} é {vermelho(moeda107.metade(n))}")
print(f'O aumento de 10$ foi de {verde(moeda107.aumentar(n))}  ')
print(f'Diminuindo por 10 é {vermelho(moeda107.diminuir(n))}')