from random import randint # Importando o aleatorizador de números
from time import sleep #Charme
pc = randint(1,5)
numero = int(input("Por favor, digite um número inteiro:"))
print("Pensando....")
sleep(1)
if numero == pc: # Se o número for igual o número do pc você advinhou
    print("Você ganhou")
else:
    print(f"Você perdeu o número da maquina foi {pc}") # Caso não , você perdeu