# ============================================================
# DESAFIO 071 - SIMULADOR DE CAIXA ELETRÔNICO
# Objetivo: Crie um programa que simule o funcionamento de um 
# caixa eletrônico. No início, pergunte ao usuário qual será 
# o valor a ser sacado (número inteiro) e o programa vai 
# informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, 
# R$10 e R$1.
# ============================================================

while True:
    while True:
        try:
            valor_sacado = int(input("Qual é o valor que deseja sacar? "))
            if valor_sacado < 1:
                print("O valor  digitado e inválido para sacar! ")
                continue
            break
        except ValueError:
            print("Por favor digite apenas números inteiros!! ")
    notas50 = valor_sacado // 50
    sobra = valor_sacado % 50
    notas20 = sobra // 20
    sobra  = sobra % 20
    notas10 = sobra // 10
    sobra  =  sobra % 10
    notas1 = sobra // 1
    if notas50 >= 1:
        print(f"Você sacou {notas50} cédulas de R$50. ")
    if notas20 >=1:
        print(f"Você sacou {notas20} cédulas de R$20. ")
    if notas10 >=1:
        print(f"Você sacou {notas10} cédulas de R$10. ")
    if notas1 >=1:
        print(f"Você sacou {notas1} cédulas de R$1. ")
    break
print("="*30)
print("Obrigado por utlizar nosso banco")