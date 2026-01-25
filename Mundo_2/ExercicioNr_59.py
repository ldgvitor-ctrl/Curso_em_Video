# ============================================================
# DESAFIO 059 - CRIANDO UM MENU DE OPÇÕES
# Objetivo: Crie um programa que leia dois valores e mostre 
# um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
# ============================================================

n1 = int(input("Escolha o primeiro número: "))
n2 = int(input("Escolha o segundo número: "))
while True:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    # Validação da opção escolhida
    while True:
        try:
            opcao = int(input("Digite qual opção deseja"))
            if opcao < 1 or opcao > 5:
                print("Opção inválida, por favor selecione as opções de 1 a 5")
                continue
            break
        except ValueError:
            print("Por favor, selecione apenas os  números que apresentam no menu")
    # Processamento das opções do Menu
    if opcao == 1:
        # Realiza a soma
        print(f"A soma dos número {n1} + {n2} = {n1 + n2}")
    elif opcao == 2:
        # Realiza a multiplicação
        print(f"A multiplicação dos números {n1} x {n2} = {n1 * n2}")
    elif  opcao == 3:
        # Verifica qual valor é maior
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"O maior número entre {n1} e {n2} {maior}")
    elif opcao == 4:
        # Reinicia a entrada de dados
        print("Informe os números novamente:")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    else:
        # Encerra o laço principal
        print("Obrigado por utilizar nossos produtos!! Até a proxima! ")
        break