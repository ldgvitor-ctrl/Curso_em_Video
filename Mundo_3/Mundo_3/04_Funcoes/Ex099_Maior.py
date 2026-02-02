# ==============================================================================
# Desafio: 099
# Tema: Função que descobre o maior
# Enunciado: Faça um programa que tenha uma função chamada maior(), que 
#            receba vários parâmetros com valores inteiros. 
#            Seu programa tem que analisar todos os valores e dizer qual 
#            deles é o maior.
# ==============================================================================
from time import sleep

def maior(* num):
    cont = maior_valor = 0
    print('\nAnalisando os valores passados...')
    
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior_valor = valor
        else:
            if valor > maior_valor:
                maior_valor = valor
        cont += 1
        
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior_valor}.')
    print('-' * 30)

maior(5, 9, 4, 5, 7, 8)
maior(4, 10, 0)
maior(1, 2)
maior(6)
maior()
