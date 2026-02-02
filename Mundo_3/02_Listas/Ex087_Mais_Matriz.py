# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 087
# Tema: Mais sobre Matriz em Python
# Enunciado: Aprimore o desafio anterior, mostrando no final:
#            A) A soma de todos os valores pares digitados.
#            B) A soma dos valores da terceira coluna.
#            C) O maior valor da segunda linha.
# ==============================================================================
soma_par = maior = soma_conula = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f"Digite um valor para [{i}, {c}]: "))

print("-=-" * 10)

for i in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[i][c]:^5}]", end="")
        if matriz[i][c] % 2 == 0:
            soma_par += matriz[i][c]
    print() 
print("-=-" * 10)
print(f"A Soma dos números pares é {soma_par}")
for i in range(0,3):
    soma_conula += matriz[i][2]
print(f"A soma das colunas é {soma_conula}")
for i in range(0,3):
    if c ==0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"O maior valor da segunda linha é {maior}")
 
