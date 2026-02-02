# ==============================================================================
# Desafio: 100
# Tema: Funções para sortear e somar
# Enunciado: Faça um programa que tenha uma lista chamada números e duas 
#            funções chamadas sorteia() e somaPar(). 
#            - sorteia(): sorteia 5 números e os coloca dentro da lista.
#            - somaPar(): mostra a soma entre todos os valores PARES 
#                         sorteados pela função anterior.
# ==============================================================================
from random import randint
from time import sleep

def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end="", flush=True)
    for cont in range(0, 5):
        n = randint(1, 10) 
        lista.append(n)    
        print(f"{n} ", end="", flush=True)
        sleep(0.3)
    print("PRONTO!")

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0: 
            soma += valor
    print(f'Somando os valores pares de {lista}, temos o total de: {soma}')

numeros = list() 
sorteia(numeros) 
somapar(numeros) 