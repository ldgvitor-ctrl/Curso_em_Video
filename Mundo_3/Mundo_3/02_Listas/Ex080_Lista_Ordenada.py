# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 080
# Tema: Listas (Parte 1)
# Enunciado: Crie um programa onde o usuário possa digitar cinco valores 
#            numéricos e cadastre-os em uma lista, já na posição correta 
#            de inserção (sem usar o sort()). No final, mostre a lista 
#            ordenada na tela.
# ==============================================================================
lista=[]
maior = menor = 0
for c in range(0, 5):
    n = (int(input("Digite números inteiros: ")))
    if c == 0:
        lista.append(n)
    elif n > lista[-1]:
        lista.append(n)
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                break
            posicao +=1

print(f"Os valores digitados em ordem foram: {lista}")
        