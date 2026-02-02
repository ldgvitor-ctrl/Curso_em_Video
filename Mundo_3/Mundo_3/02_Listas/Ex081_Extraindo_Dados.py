# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 081
# Tema: Listas (Parte 1)
# Enunciado: Crie um programa que vai ler vários números e colocar em uma lista. 
#            Depois disso, mostre:
#            A) Quantos números foram digitados.
#            B) A lista de valores, ordenada de forma decrescente.
#            C) Se o valor 5 foi digitado e está ou não na lista.
# ==============================================================================
lista = []
while True:
    while True:
        try:
            n = int(input("Digite um número: "))
            lista.append(n)
            break
        except ValueError:
            print("Digite apenas números inteiros! ")
    
    while True:
        resposta = input("Você deseja sair? [S/N] ").strip().upper()[0]
        if not resposta:
            print("Por favor digite Sim ou Não! ")
            continue
        if resposta in ("SN"):
            break
        else:
            print("Por favor digite apenas Sim ou Não! ")
    
    if resposta == "S":
        break
print("-="*30)
print(f"Você digitou {len(lista)} elementos ")
lista.sort(reverse=True)
print(f"Os valores em ordem decressente são {lista}")
if 5 in lista:
    print("O valor 5 faz parte da lista! ")
else:
    print("O valor 5 não faz parte da lista ")