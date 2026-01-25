# ============================================================
# DESAFIO 063 - SEQUÊNCIA DE FIBONACCI V1.0
# Objetivo: Escreva um programa que leia um número n inteiro 
# qualquer e mostre na tela os n primeiros elementos de uma 
# Sequência de Fibonacci. 
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
# ============================================================
print("-"*20)
print("Sequências de Fibonacci")
print("-"*20)
termos = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
count = 3
print(f"{t1} -> {t2} ->" , end=" ")
while count <= termos:
    t3 = t1 + t2
    print(f"{t3} - ", end=" ")
    t1 = t2 
    t2 = t3
    count+=1
print("FIM! ")