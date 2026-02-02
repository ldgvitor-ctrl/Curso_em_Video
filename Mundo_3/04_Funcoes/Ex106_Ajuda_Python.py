# ==============================================================================
# Desafio: 106
# Tema: Sistema interativo de ajuda em Python
# Enunciado: Faça um mini-sistema que utilize o Interactive Help do Python. 
#            O usuário vai digitar o comando (ex: 'print' ou 'len') e o 
#            manual vai aparecer. Quando o usuário digitar a palavra 'FIM', 
#            o programa se encerrará. Importante: use cores.
# ==============================================================================
from time import sleep

# Tupla com códigos de cores ANSI
c = ('\033[m',          # 0 - Sem cores
     '\033[0;30;41m',   # 1 - Vermelho
     '\033[0;30;42m',   # 2 - Verde
     '\033[0;30;44m',   # 3 - Azul
     '\033[7;30m'       # 4 - Branco (Inverso)
    )

def ajuda(com):
    """
    Chama o help() do Python com uma estética personalizada.
    """
    titulo(f'Acessando o manual do comando \'{com}\'', 3)
    sleep(1)
    print(c[4], end='') # Ativa o fundo branco para o manual
    help(com)
    print(c[0], end='') # Reseta a cor
    sleep(2)

def titulo(msg, cor=0):
    """
    Cria um cabeçalho adaptável com linhas e cores.
    """
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

# --- Programa Principal ---
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca (FIM para encerrar) > ")).strip()
    
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO!', 1)