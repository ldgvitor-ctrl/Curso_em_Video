# ==========================================
# DESAFIO 038 - Comparando números
# Objetivo: Ler dois números inteiros e comparar qual é o maior 
# ou se ambos possuem o mesmo valor.
# ==========================================
print("="*10,"ComPYrador","="*10)
numero1 = int(input("Primeiro Número: "))
numero2 = int(input("Segundo Número: "))
print("="*30)

if numero1 > numero2: # Comparando o primeiro valor com o segundo.
    print(f"O {numero1} é maior que o número {numero2} ")
elif numero2 > numero1: # Comparando o segundo valor com o primeiro.
    print(f"O número {numero2} é maior que o número {numero1}")
else: # Caso os dois forem iguais 
    print(f"O número {numero1} e o número {numero2} são igauis")