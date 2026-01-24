altura = float(input("Digite a altura da parede em metros: "))
largura = float(input("Digite a largura da parede em metros: "))
area = altura * largura # Cálculo da área da parede
tinta_necessaria = area / 2 # Cálculo da quantidade de tinta necessária (1 litro para cada 2 m²)
print(f"Área da parede: {area:.2f} m²")
print(f"Tinta necessária: {tinta_necessaria:.2f} litros")# Este programa calcula a quantidade de tinta necessária para pintar uma parede
