frase = input("Digite qualquer frase: ").strip().upper()
print(f"A Letra A aprece {frase.count("A")} em sua frase! ") # Contador de letra A
print(f"A primeira posição que a letra A apareceu foi na {frase.find("A") + 1}° posição ")
# Ver a posição no qual ela apareceu  # Utilizar o +1 pois ele irá contar  o 0 
print(f"A última posição que a letra A apareceu foi na {frase.rfind("A") + 1}° posiçã ")
