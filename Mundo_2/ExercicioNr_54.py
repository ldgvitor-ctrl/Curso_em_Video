# ============================================================
# DESAFIO 054 - GRUPO DA MAIORIDADE
# Objetivo: Crie um programa que leia o ano de nascimento de 
# sete pessoas. No final, mostre quantas pessoas ainda não 
# atingiram a maioridade e quantas já são maiores (Considerando 21 anos).
# ============================================================
from datetime import date
ano_atual = date.today().year # Importa o ano atual
tot_maior = tot_menor = 0
for pessoa in range(1,8):
    ano_nascimento = int(input(f"Em qual ano a {pessoa}° pessoa nasceu? "))
    maior_idade = ano_atual - ano_nascimento 
    if maior_idade >= 21:
        tot_maior+=1 # Conta quantas pessoas tem mais de 21 anos
    else:
        tot_menor+=1 # Conta quantas pessoas tem menos de 21 anos
print(f"Ao todo tivemos {tot_maior} pessoas maiores de idade.")
print(f"E também tivemos {tot_menor} pessoas menores de idade.")