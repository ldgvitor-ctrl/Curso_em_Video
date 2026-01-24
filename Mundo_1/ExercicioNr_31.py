viagem = float(input("Digite a distância da sua viagem: "))
if viagem <= 200: # Se for até 200 km custara 0.5 o km
    preco = viagem * 0.5 # Calculando
    print(f"Sua viagem de {viagem}Km custará R${preco:.2f}") 
else:
    preco = viagem * 0.45 # Calculando
    print(f"Sua viagem de {viagem}Km custará R$ {preco:.2f}")
