# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 085
# Tema: Listas com pares e ímpares
# Enunciado: Crie um programa onde o usuário possa digitar sete valores numéricos 
#            e cadastre-os em uma lista única que mantenha separados os valores 
#            pares e ímpares. No final, mostre os valores pares e ímpares 
#            em ordem crescente.
# ==============================================================================
dados = [[],[]]
for c in range(7):
    numero = int(input(f"Digite o {c + 1}° Número: "))
    if numero % 2 == 0:
        dados[0].append(numero)
    else:
        dados[1].append(numero)
print("-_-" * 10)
dados[0].sort()
dados[1].sort()
print(f"Os nomeros pares são {dados[0]}")

print(f"Os números {dados[1]} são ímpares")

    