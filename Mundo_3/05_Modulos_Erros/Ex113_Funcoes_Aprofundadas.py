# ==============================================================================
# Desafio: 113
# Tema: Tratamento de Erros e Exceções
# Enunciado: Reescreva a função leiaInt() que fizemos no desafio 104, 
#            incluindo agora a possibilidade da digitação de um número de 
#            tipo inválido. Aproveite e crie também uma função leiaFloat() 
#            com a mesma funcionalidade.
# ==============================================================================
from modulos.cores import *

def leiaint(mensagem):
    while True:
        try:
            n = int(input(mensagem)) # Tenta converter direto
        except (ValueError, TypeError): # Se o usuário digitar "abc"
            print(f"{vermelho('ERRO: Digite um número inteiro')}, {verde("válido!")}")
            continue
        except KeyboardInterrupt: # Se o usuário interromper o programa
            print(f"\n{amarelo('Usuário preferiu não digitar esse número.')}")
            return 0
        else: # Se deu tudo certo
            return n

def leiafloat(mensagem):
    while True:
        try:
            n = float(input(mensagem).replace(',', '.')) # Aceita vírgula e tenta converter
        except (ValueError, TypeError):
            print(f"{vermelho('ERRO:')} Digite um número real válido!")
            continue
        except KeyboardInterrupt:
            print(f"\n{amarelo('Usuário preferiu não digitar esse número.')}")
            return 0
        else:
            return n

# Programa Principal
n1 = leiaint("Digite um Inteiro: ")
n2 = leiafloat("Digite um Real: ")
print(f"O valor inteiro foi {n1} e o real foi {n2}")