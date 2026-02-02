# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 073
# Tema: Tuplas (Variáveis Compostas)
# Enunciado: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela 
#            do Campeonato Brasileiro de Futebol, na ordem de colocação. 
#            Depois mostre:
#            A) Apenas os 5 primeiros colocados.
#            B) Os últimos 4 colocados da tabela.
#            C) Uma lista com os times em ordem alfabética.
#            D) Em que posição na tabela está o time da Chapecoense.
# ==============================================================================
time = (
    "Flamengo", "Palmeiras", "Cruzeiro", "Mirassol", "Fuminense", "Botafogo","Bahia", "São Paulo",
    "Grêmio", "RB Bragantino", "Atlético - MG", "Santos", "Corinthians", "Vasco", "Vitória", "Internacional",
    "Ceará", "Fortaleza", "Juventude", "Chapecoense"
    )
print("-"*30)
print("Times do Brasileirão 2026")
print("-"*30)

print(f"Os primeiros colocados são: {time[:5]}")
print(f"Os 4 últimos são: {time[-4:]}")
print(f"Os times em ordem alfabética: {sorted(time)}")
print(f"O time da  Chapecoense está na posição {time.index("Chapecoense") + 1 }ª posição ")