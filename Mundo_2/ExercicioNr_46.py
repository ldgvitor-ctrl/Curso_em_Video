# ============================================================
# DESAFIO 046 - CONTAGEM REGRESSIVA
# Objetivo: Faça um programa que mostre na tela uma contagem 
# regressiva para o estouro de fogos de artifício, indo de 
# 10 até 0, com uma pausa de 1 segundo entre eles.
# ============================================================
import time
# O range(início, fim, passo) - vai de 10 até 0 subtraindo 1
for contagem in range(10, -1, -1):
    print(contagem)
    time.sleep(1) # Pausa a execução por 1 segundo a cada iteração
print("BUM! BUM! POOOW! ")