from math import sqrt #importa a função sqrt da biblioteca math
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = sqrt(cateto_oposto**2 + cateto_adjacente**2) #calcula o comprimento da hipotenusa usando o teorema de Pitágoras
hipotenusa_1 = (cateto_oposto**2 + cateto_adjacente**2)**0.5 #calcula o comprimento da hipotenusa usando a raiz quadrada
print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")