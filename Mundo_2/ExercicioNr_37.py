# ==========================================
# DESAFIO 037 - Conversor de Bases Numéricas
# Objetivo: Ler um número inteiro e permitir a conversão para:
# 1. Binário (Base 2): Linguagem de baixo nível da máquina.
# 2. Octal (Base 8): Comum em sistemas de permissão (ex: Unix).
# 3. Hexadecimal (Base 16): Usado em cores (HTML) e endereços MAC.
# ==========================================

numero = int(input("Digite um número inteiro: "))

# Exibição de um menu de opções para o usuário
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
[ 0 ] Sair do programa ''')

opcao = int(input("Sua opção:" ))

# Estrutura condicional para processar a escolha
if opcao == 1:
    # bin() gera o prefixo '0b', por isso usamos fatiamento [2:]
    print(f"{numero} em Binário é {bin(numero)[2:]}")
elif opcao == 2:
    # oct() gera o prefixo '0o', fatiamos [2:] para remover
    print(f"{numero} em Octal é {oct(numero)[2:]}")
elif opcao == 3:
    # hex() gera o prefixo '0x', fatiamos [2:] para remover
    print(f"{numero} em Hexadecimal é {hex(numero)[2:]}")
elif opcao == 0:
    # Caso o usuário queira sair do programa
    print("Obrigado por utilizar nosso programa! Volte sempre! ")
else:
    # Caso o usuário digite um número fora do menu
    print("Opção inválida! ")
