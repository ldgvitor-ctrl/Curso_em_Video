# ============================================================
# DESAFIO 043 - ÍNDICE DE MASSA CORPORAL (IMC)
# Objetivo: Ler o peso e a altura de uma pessoa e calcular seu 
# IMC, mostrando seu status, de acordo com a tabela:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
# ============================================================
print("="*10,"Descubra o seu Imc","="*10)
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m) - Ex: 1.75: "))
# Calculando o imc 
imc = peso / (altura**2)
estado = ""
# Classificação
if imc > 40:
    estado = "Obesidade mórbida"
elif imc > 30:
    estado = "Obesidade"
elif imc > 25:
    estado = "Sobre peso"
elif imc > 18.5:
    estado = "Peso ideal"
else:
    estado = "Abaixo do peso"    

print(f"Com a altura de {altura} e o peso de {peso} você está {estado} e seu imc é {imc:.1f}")