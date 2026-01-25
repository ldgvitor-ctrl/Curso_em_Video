# ============================================================
# DESAFIO 062 - SUPER PROGRESSÃO ARITMÉTICA V3.0
# Objetivo: Melhore o DESAFIO 061, perguntando para o usuário 
# se ele quer mostrar mais alguns termos. O programa encerra 
# quando ele disser que quer mostrar 0 termos.
# ============================================================
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
count = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while count <= total:
        print(f"{termo} -> ", end="")
        termo += razao
        count += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))

print(f"Progressão finalizada com {total} termos mostrados.")