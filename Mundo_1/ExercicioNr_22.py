nome = input("Digite seu nome: ").strip() # strip serve para retirar os espaço do inicio e do final
sem_espaço = nome.replace(" ", "") # Retirar os espaços
print((f"Seu nome em letras minúsculo é {nome} ").lower()) # Deixar tudo em minúsculo 
print((f"Seu nome em letras maiúsculas é {nome}").upper()) # Deixar em caixa alta
print(f"Seu nome tem ao todo {len(sem_espaço)} letras") # Contar as Letras sem contar o espaço
print(f"Seu primeiro nome tem {nome.find(" ")}") # Ele vai contar até o primeiro espaço
