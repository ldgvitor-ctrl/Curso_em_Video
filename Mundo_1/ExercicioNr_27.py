from time import sleep # Para dar um charme
nome = input("Digite seu nome completo por favor! : ").strip().split() # Fatiamos o nome em uma lista de palavras
print("Analizando....")
sleep(1)
print(f"Seu primeiro nome é {nome[0]} ")
print(f"E seu último nome é {nome[-1]} ")
