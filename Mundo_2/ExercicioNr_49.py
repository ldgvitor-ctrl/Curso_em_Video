# ============================================================
# DESAFIO 049 - TABUADA V2.0
# Objetivo: Refazer o DESAFIO 009, mostrando a tabuada de um 
# número que o usuário escolher, só que agora utilizando 
# um laço for.
# ============================================================
print("="*10, "Bem-vindo a PYrabuada","="*10)

# Entrada do número base
numero = int(input("Digite o número que deseja saber a tabuda: "))

for n in range(1,11):# Laço de repetição de 1 a 10 (o 11 é exclusivo)
    # Cálculo e exibição formatada em tempo real
    print(f"{numero} x {n:2} = {numero*n}")