# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 083
# Tema: Validando expressões matemáticas
# Enunciado: Crie um programa onde o usuário digite uma expressão qualquer que 
#            use parênteses. Seu aplicativo deverá analisar se a expressão 
#            passada está com os parênteses abertos e fechados na ordem correta.
# ==============================================================================
parentese = []

expressao = input("Digite a expressão que deseja analizar: ")

for caractere in expressao:
    if caractere == "(":
        parentese.append("(")
    elif caractere == ")":
        if len(parentese) > 0:
            parentese.pop()
        else:
            parentese.append(")")
            break
if len(parentese) == 0:
    print("Sua expressão é válida! ")
else:
    print("Sua expressão não é válida ")