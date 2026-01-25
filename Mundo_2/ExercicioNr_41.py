# ============================================================
# DESAFIO 041 - CLASSIFICANDO ATLETAS
# Objetivo: Ler o ano de nascimento de um atleta e mostrar sua 
# categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25: MASTER
# ============================================================
# Coleta e trata o nome (remove espaços e pega apenas o primeiro)
nome = input("Qual é o seu nome? ").upper().split()[0]
# Coleta a idade do atleta
idade = int(input((f"Bem-Vindo {nome} por favor digite sua idade para que possa competir \nIdade: ")))
categoria = ""
# Estrutura condicional para classificar a categoria
# A ordem começa do maior para o menor para evitar conflitos de faixa
if idade > 25:
    categoria = "Master"
elif idade > 19:
    categoria = "Sênior"
elif idade > 14:
    categoria = "Junior"
elif idade > 9:
    categoria = "Infantil"
else:
    categoria = "Mirim"
print(f"\nO atleta {nome} tem {idade} anos. ")
print(f"Categoria: {categoria}")
    
