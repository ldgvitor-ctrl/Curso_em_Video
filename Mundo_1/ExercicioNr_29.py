velocidade = float(input("Qual é a velocidade que você estava? "))
if velocidade > 80:
    multa = 7 * (velocidade - 80) # Calculando a multa
    print(f"Você foi multado e sua multa ficará R${multa:.2f} ")
else:
    print("Você não foi multado")
