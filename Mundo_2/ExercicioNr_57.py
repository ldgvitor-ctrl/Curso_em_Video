# ============================================================
# DESAFIO 057 - VALIDAÇÃO DE DADOS
# Objetivo: Faça um programa que leia o sexo de uma pessoa, 
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado, 
# peça a digitação novamente até ter um valor correto.
# ============================================================
sexo = input("Qual é seu sexo? [M/F]").strip().upper()[0] # Deixa ela em maiúscula e pega somente a primeira
while sexo not in "MF": # Enquanto não estiver certo irá ficar em repetição
    sexo = input("Sexo inválido por favor escolha dentre as opções [M/F]: ").strip().upper()[0]
print("Sexo registrado com suscesso!! ")
