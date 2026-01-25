# ============================================================
# DESAFIO 050 - SOMA DOS PARES
# Objetivo: Desenvolver um programa que leia seis números 
# inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.
# ============================================================
soma = contador = 0 # Inicialização das variáveis de controle
# Acumulador: vai somar os valores (ex: 2 + 4 + 8...)
# Contador: vai contar as unidades (ex: 1, 2, 3...)

for n in range(1,7):# Laço para ler 6 números inteiros
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0: # Estrutura condicional para filtrar apenas números PARES
        soma+=numero
        contador+=1
print(f"A soma de {contador} números pares foi {soma}") # Exibição dos resultados finais