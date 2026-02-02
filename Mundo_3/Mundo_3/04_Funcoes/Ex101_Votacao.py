# ==============================================================================
# Desafio: 101
# Tema: Funções para votação
# Enunciado: Crie um programa que tenha uma função chamada voto(), que vai 
#            receber como parâmetro o ano de nascimento de uma pessoa, 
#            RETORNANDO um valor literal indicando se uma pessoa tem voto 
#            NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
# ==============================================================================
def voto(ano):
    from datetime import date
    idade = date.today().year - ano 

    if idade < 16:
        return f"Você não poderá votar com a idade de {idade}"
    elif 16 <= idade < 18 or idade > 65:
        return f"Você vota se quiser com a idade de {idade}"
    else:
        return f"Você é obrigado a votar! com a idade de {idade}"
ano = int(input("Qual ano você nasceu? "))
print(voto(ano))

