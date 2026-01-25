# ============================================================
# DESAFIO 045 - GAME: PEDRA, PAPEL E TESOURA
# Objetivo: Criar um jogo de Jokenpô onde o computador escolhe 
# uma opção aleatória e o jogador tenta vencer.
# Diferencial: Uso da biblioteca random e estruturas de controle.
# ============================================================
from random import randint

# 1. Preparação
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

# 2. Interface
print("="*10, " JOKENPÔ ", "="*10)
print('''Escolha sua jogada:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual a sua jogada? "))

# 3. Exibição rápida
print("-" * 25)
print(f"Computador jogou: {itens[computador]}")
print(f"Você jogou: {itens[jogador]}")
print("-" * 25)

# 4. Lógica de Vitória
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("VOCÊ VENCEU!")
    elif jogador == 2:
        print("COMPUTADOR VENCEU!")
        
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCEU!!")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("VOCÊ VENCEU!")
else: # Computador jogou TESOURA
    if jogador == 0:
        print("VOCÊ VENCEU")
    elif jogador == 1:
        print("COMPUTADOR VENCEU!")
    elif jogador == 2:
        print("EMPATE!")
