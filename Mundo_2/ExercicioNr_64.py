# ============================================================
# DESAFIO 064 - TRATANDO VÁRIOS VALORES V1.0
# Objetivo: Crie um programa que leia vários números inteiros 
# pelo teclado. O programa só vai parar quando o usuário 
# digitar o valor 999, que é a condição de parada. No final, 
# mostre quantos números foram digitados e qual foi a soma 
# entre eles (desconsiderando o flag 999).
# ============================================================
# Inicialização dos acumuladores e do flag
contar = soma = numero = 0
# O laço roda enquanto o número digitado não for o flag de parada
while numero != 999:
    numero = int(input("Digite um número [999 para parar]: "))
   # Condição para não contabilizar o 999 na soma e no contador
    if numero != 999:
        soma+=numero
        contar+=1
   
    # Exibição dos resultados finais
print(f"Você digitou {contar} vezes e a soma dos números digitados é {soma} ")