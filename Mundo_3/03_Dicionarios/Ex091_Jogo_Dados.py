# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 091
# Tema: Jogo de Dados em Python
# Enunciado: Crie um programa onde 4 jogadores joguem um dado (1 a 6) e 
#            tenham resultados aleatórios. Guarde esses resultados em um 
#            dicionário. No final, coloque esse dicionário em ordem, 
#            sabendo que o vencedor tirou o maior número no dado.
# ==============================================================================
from random import randint
from operator import itemgetter
jogador = {}

print("Valores sorte ados: ")
for numeracao in range(1,5):
    nome_jogador = f"O {numeracao}° jogador"
    dado = randint(1,6)
    jogador[nome_jogador] = dado
    print(f"{nome_jogador} tirou {dado}")

ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
print(f'{"== RANKING DOS JOGADORES ==":^30}')

for numeracao, posicao in enumerate(ranking):
    print(f" {numeracao+1}° lugar:{posicao[0]} com {posicao[1]} ")