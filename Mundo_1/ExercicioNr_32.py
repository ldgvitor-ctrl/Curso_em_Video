from datetime import date
from time import sleep
ano = int(input("Que ano você quer analizar? coloque 0 para saber do ano atual ")) # Analizador de ano BISSEXTO
print("Analizando....")
sleep(1)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} é bissexto")
else:
    print(f"O ano de {ano} não é um ano bissexto")
# Ano % 4 == 0: Primeiro ele checa se o ano é divisível por 4.
# and ano % 100 != 0: Ele garante que o ano não pode ser centenário (tipo 1900, 2100).
# or ano % 400 == 0: Mas, se ele for divisível por 400 (tipo 2000), ele volta a ser bissexto, "atropelando" a regra anterior.