produto = float(input("Digite o preço do produto: R$ "))
desconto = produto * 0.05 # Calcula 5% de desconto
preco_final = produto - desconto
print(f"O preço final do produto de R$ {produto} com 5% de desconto é: R$ {preco_final:.2f}")