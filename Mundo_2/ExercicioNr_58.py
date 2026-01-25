# ============================================================
# DESAFIO 058 - JOGO DA ADIVINHAÇÃO V2.0
# Objetivo: Melhore o jogo do DESAFIO 028 onde o computador 
# "pensa" em um número entre 0 e 10. Só que agora o jogador 
# vai tentar adivinhar até acertar, mostrando no final 
# quantos palpites foram necessários para vencer.
# ============================================================
from random import randint
computador = randint(0,10)
palpites = 0
while True:
    # Validação da entrada do usuário
    while True:
        try:
            numero = int(input("Digite um número: "))
            if numero < 0:
                print("O Número digitado não pode ser menor que 0 ")
                continue
            break
        except ValueError:
            print("Por favor digite um número inteiro válido")
    # Verificação do palpite
    palpites+=1
    if numero > computador:
        print(f"Seu número {numero} é maior que o do computador")
    elif numero < computador:
        print(f"Seu número {numero} é menor que o do computador")
    else:
        print(f"Você ganhou parabéns! você acertou com {palpites} tentativas! impressionante! ")
        break