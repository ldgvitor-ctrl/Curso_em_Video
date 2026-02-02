# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 088 (Adaptado do 089 para seguir a numeração da sua lista)
# Tema: Palpites para a Mega Sena (ou Boletim, dependendo da sua versão)
# Enunciado: Crie um programa que ajude um jogador da MEGA SENA a criar 
#            palpites. O programa vai perguntar quantos jogos serão gerados 
#            e vai sortear 6 números entre 1 e 60 para cada jogo, 
#            cadastrando tudo em uma lista composta.
# ==============================================================================
from random import randint
lista = []
jogos = []
total = 1
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
quantidade = int(input("Quantos jogos você quer? "))

while total <= quantidade:
    contar = 0
    while True:
        numeros = randint(1,60)
        if numeros not in (jogos):
            jogos.append(numeros)
            contar+=1
        if contar >= 6:
            break
    jogos.sort()
    lista.append(jogos[:])
    jogos.clear()
    total+=1

print('-=' * 3, f' SORTEANDO {quantidade} JOGOS ', '-=' * 3)
for i, c in enumerate(lista):
    print(f'Jogo {i+1}: {c}')
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
