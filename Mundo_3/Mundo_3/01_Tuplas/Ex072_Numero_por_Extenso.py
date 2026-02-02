# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 072
# Tema: Tuplas (Variáveis Compostas)
# Enunciado: Crie um programa que tenha uma tupla totalmente preenchida com uma 
#            contagem por extenso, de zero até vinte. Seu programa deverá ler 
#            um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# ==============================================================================

contagem = (
    "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", 
    "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", 
    "Dezessete", "Dezoito", "Dezenove", "Vinte"
)

while True:
    try: # Validação
        escolha = int(input("Escolha um número de 0 até 20: "))
        if escolha < 0 or escolha > 20:
            print("O número escolhido deve ser de 0 até 20! ")
            continue
        else:
            break
    except ValueError:
        print("Digite apenas números inteiros!")

print(f"Você digitou o número {contagem[escolha]}")