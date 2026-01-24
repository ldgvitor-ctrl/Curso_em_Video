import math # Importa a biblioteca matemática
angulo = int(input("Digite o valor do ângulo em graus: "))
angulo_rad = math.radians(angulo) # Converte graus para radianos
seno = math.sin(angulo_rad) # Calcula o seno
cosseno = math.cos(angulo_rad) # Calcula o cosseno
tangente = math.tan(angulo_rad) # Calcula a tangente
print(f"O seno de {angulo} graus é: {seno:.2f}")
print(f"O cosseno de {angulo} graus é: {cosseno:.2f}")
print(f"A tangente de {angulo} graus é: {tangente:.2f}")