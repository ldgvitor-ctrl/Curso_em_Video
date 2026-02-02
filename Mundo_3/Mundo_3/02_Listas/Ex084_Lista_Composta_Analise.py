# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 084
# Tema: Lista composta e análise de dados
# Enunciado: Faça um programa que leia nome e peso de várias pessoas,
#            guardando tudo em uma lista. No final, mostre:
#            A) Quantas pessoas foram cadastradas.
#            B) Uma listagem com as pessoas mais pesadas.
#            C) Uma listagem com as pessoas mais leves.
# ==============================================================================
dados = []
maior = menor = 0
while True:
    nome = str(input("Nome: ")).strip()
    peso = float(input("Peso: "))
    
    if len(dados) == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor: 
            menor = peso
    dados.append([nome,peso])
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Você quer continuar? [S/N]")).strip().upper()[0]
    if resposta == "N":
        break
print("-_-" * 10)
print(f"Ao todo, você cadrastrou {len(dados)} pessoas!. ")
print(f"O maior peso de {maior}Kg. Peso de: ", end="")
for p in dados:
    if p[1] == maior:
        print(f"[{p[0]}]", end="")
print(f"O menor peso foi de {menor}Kg. Peso de: ", end="")
for p in dados:
    if p[1] == menor:
        print(f"[{p[0]}]", end="")
