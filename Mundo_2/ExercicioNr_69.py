# ============================================================
# DESAFIO 069 - ANÁLISE DE DADOS DO GRUPO
# Objetivo: Crie um programa que leia a idade e o sexo de 
# várias pessoas. A cada pessoa cadastrada, o programa deverá 
# perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
# ============================================================

# Contadores
maiores_de_18 = 0
total_homens = 0
mulheres_menos_de_20 = 0

print("Cadastro de pessoas - digite os dados solicitados\n")

while True:
    # Leitura da idade com validação
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade < 0:
                print("Idade não pode ser negativa. Tente novamente.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    # Leitura do sexo com validação
    sexo = ""
    while sexo not in ["M", "F"]:
        sexo = input("Digite o sexo [M/F]: ").strip().upper()
        if len(sexo) > 0:
            sexo = sexo[0]
        if sexo not in ["M", "F"]:
            print("Sexo inválido. Digite M ou F.")

    # Atualiza os contadores
    if idade >= 18:
        maiores_de_18 += 1

    if sexo == "M":
        total_homens += 1
    else:  # sexo == "F"
        if idade < 20:
            mulheres_menos_de_20 += 1

    # Pergunta se quer continuar
    continuar = ""
    while continuar not in ["S", "N"]:
        continuar = input("Quer continuar? [S/N]: ").strip().upper()
        if len(continuar) > 0:
            continuar = continuar[0]
        if continuar not in ["S", "N"]:
            print("Resposta inválida. Digite S ou N.")

    if continuar == "N":
        break

# Resultado final
print("\n" + "-" * 50)
print(f"Total de pessoas com mais de 18 anos:     {maiores_de_18}")
print(f"Total de homens cadastrados:              {total_homens}")
print(f"Total de mulheres com menos de 20 anos:   {mulheres_menos_de_20}")
print("-" * 50)