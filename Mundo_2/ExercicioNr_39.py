# ==========================================
# DESAFIO 039 - Alistamento Militar
# Objetivo: Ler o ano de nascimento de um jovem e informar sua 
# situação de acordo com sua idade:
# - Se ainda vai se alistar (exibindo o tempo que falta).
# - Se é a hora exata de se alistar (aos 18 anos).
# - Se já passou do tempo (exibindo o tempo atrasado).
# ==========================================
from datetime import datetime #Importar a data atual
esse_ano = datetime.now() # Pegar o mês e o ano atual.

data_nascimento =int(input("Em qual ano você nasceu: "))

maior_de_18 = esse_ano.year - data_nascimento # Fazer a conta se a pessoa é maior de 18 anos

if maior_de_18 > 18: # Se a pessoa tiver mais que 18 anos ela já passou do prazo
    print(f"Você tem {maior_de_18} e deveria ter se alistado em {data_nascimento + 18} está {(data_nascimento + 18) - esse_ano.year} atrasado ")
elif maior_de_18 == 18: # Caso tenha 18 esse ano , ela deverá se alistar esse ano
    print("Você deveria se alistar esse ano! ")
else: # Caso ainda seja menor de idade deverá esperar chegar na maior idade
    print(f"Você tem {maior_de_18} e deverá se alistar em  {data_nascimento + 18}")