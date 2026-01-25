# ============================================================
# DESAFIO 067 - TABUADA V3.0
# Objetivo: Faça um programa que mostre a tabuada de vários 
# números, um de cada vez, para cada valor digitado pelo 
# usuário. O programa será interrompido quando o número 
# solicitado for negativo. 
# ============================================================
while True:
   print("-" * 35)
   numero = int(input("Quer ver a tabuada de qual valor? "))
   print("-" * 35)
   if numero < 0:
        break
   for n in range (1,11): # Laço de repetição de 1 a 10 (o 11 é exclusivo)
         # Cálculo e exibição formatada em tempo real
         print(f"{numero} x {n:2} = {numero*n}")
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")

