# ============================================================
# DESAFIO 068 - JOGO DO PAR OU ÍMPAR
# Objetivo: Faça um programa que jogue par ou ímpar com o 
# computador. O jogo só será interrompido quando o jogador 
# PERDER, mostrando o total de vitórias consecutivas que 
# ele conquistou no final do jogo. 
# ============================================================
from random import randint
vitorias = 0
while True:
    # Validação do número
    while True:
        try:
            valor = int(input("Digite um valor: "))
            if valor < 0:
                print("Por favor!, digite apenas números positivos")
                continue
            break
        except ValueError:
            print("Por favor! digite apenas números: ")
    escolha = " "
    while escolha not in "PI":
        escolha = input("Inválido escolha apenas Par ou Ímpar. [P/I]").strip().upper()[0]
    pc = randint(1,10)
    total = pc + valor
    resultado = "P" if total % 2 == 0 else "I"
    print(f"Você jogou {valor} e o PC {pc}. Total {total} ({'PAR' if resultado == 'P' else 'ÍMPAR'})")
    # Lógica de Vitória ou Derrota
    if escolha == resultado:
        print("Você VENCEU! Vamos jogar de novo...")
        vitorias += 1
    else:
        print("Você PERDEU!")
        break

print(f"GAME OVER! Você venceu {vitorias} vezes seguidas.")