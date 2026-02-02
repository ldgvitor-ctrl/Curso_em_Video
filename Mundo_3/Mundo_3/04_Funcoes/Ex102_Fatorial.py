# ==============================================================================
# Desafio: 102
# Tema: Função para Fatorial
# Enunciado: Crie um programa que tenha uma função fatorial() que receba dois 
#            parâmetros: o primeiro que indique o número a calcular e o 
#            outro chamado show, que será um valor lógico (opcional) 
#            indicando se será mostrado ou não na tela o processo de 
#            cálculo do fatorial.
# ==============================================================================
def fatorial(numero=1, show=False):
    f = 1 
    for c in range(numero, 0, -1):
        f *= c
        if show:
            print(f"{c}", end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
    return f
num = int(input("Digite um número: "))
resp = input("Você quer ver como foi o cálculo? [S/N]: ").strip().upper()

visualizacao = True if resp == 'S' else False


print(fatorial(num, show=visualizacao))