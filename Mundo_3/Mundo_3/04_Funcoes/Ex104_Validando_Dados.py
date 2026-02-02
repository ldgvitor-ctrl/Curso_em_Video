# ==============================================================================
# Desafio: 104
# Tema: Validando entrada de dados em Python
# Enunciado: Crie um programa que tenha uma função chamada leiaInt(), que vai 
#            funcionar de forma semelhante à função input() do Python, só que 
#            fazendo a validação para aceitar apenas um valor numérico.
#            Ex: n = leiaInt('Digite um n: ')
# ==============================================================================
def leiaint(mensagem):
    certo = False
    valor = 0
    while True:
        n = str(input(mensagem))
        if n.isnumeric():
            valor = int(n)
            certo = True
        else:
            print("\033[0;31mERRO!! DIGITE UM NÚMERO INTEIRO VÁLIDO!! \033[m' ")
        if certo:
            break
    return valor


n = leiaint("Digite um número: ")
print(f"Você digitou o número {n}")
