# ============================================================
# DESAFIO 048 - SOMA ÍMPARES MÚLTIPLOS DE TRÊS
# Objetivo: Calcular a soma entre todos os números que:
# 1. São ÍMPARES.
# 2. São MÚLTIPLOS DE TRÊS.
# 3. Estão no intervalo de 1 até 500.
# ============================================================
soma = 0  # Variável acumuladora
cont = 0  # Variável contadora (opcional, para saber quantos números foram somados)

# Percorrendo apenas os ímpares (pulo de 2 em 2)
for n in range(1, 501, 2):
    if n % 3 == 0: # Verificando se é múltiplo de 3
        soma += n
        cont += 1

print(f"A soma de todos os {cont} valores solicitados é {soma}.")