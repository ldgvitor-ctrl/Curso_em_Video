# ============================================================
# DESAFIO 066 - VÁRIOS NÚMEROS COM FLAG
# Objetivo: Crie um programa que leia vários números inteiros. 
# O programa só vai parar quando o usuário digitar o valor 999. 
# No final, mostre quantos números foram digitados e qual 
# foi a soma entre eles (utilizando o comando break).
# ============================================================
soma = contador = 0 # Inicialização dos acumuladore
while True :
    valor = int(input("Digite um valor [999 para parar]: "))
    if valor == 999: # Adicionando o flag
        break
    soma+=valor
    contador+=1
# Exibição dos resultados finais
print(f"A soma dos {contador} é {soma}")