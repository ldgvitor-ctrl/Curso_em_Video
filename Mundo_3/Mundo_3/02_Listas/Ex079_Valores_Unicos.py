# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 079
# Tema: Listas (Parte 1)
# Enunciado: Crie um programa onde o usuário possa digitar vários valores 
#            numéricos e cadastre-os em uma lista. Caso o número já exista 
#            lá dentro, ele não será adicionado. No final, serão exibidos 
#            todos os valores únicos digitados, em ordem crescente.
# ==============================================================================
lista = []
while True:
    try:
        numero = int(input("Digite um número [Digite 0 para sair]:  "))
        if numero == 0:
            print("Obrigado por utilizar nossos serviços! ")
            break
        if numero not in lista:
            lista.append(numero)
            print("Valor resgistrado com suscesso! ")
        else:
            print("Valor repetido! ")
    except ValueError:
        print("Digite apenas números inteiros")

lista.sort()
print(f"Os números digitados foram {lista}")