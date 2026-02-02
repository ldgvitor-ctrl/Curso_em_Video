# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 093
# Tema: Cadastro de Jogador de Futebol
# Enunciado: Crie um programa que gerencie o aproveitamento de um jogador de 
#            futebol. O programa vai ler o nome do jogador e quantas partidas 
#            ele jogou. Depois vai ler a quantidade de gols feitos em cada 
#            partida. No final, tudo isso será guardado em um dicionário, 
#            incluindo o total de gols feitos durante o campeonato.
# ==============================================================================
jogador = {}
valor = []
jogador['nome'] = input("Nome do jogador:  ")
partidas = int(input("Quantas partidas o jogador teve?  "))
for c in range(0, partidas):
    gols = int(input(f"Quantos gols na partida  foram na {c+1}° partida?  "))
    valor.append(gols)
jogador['gols'] = valor[:]
jogador['total'] = sum(valor[:])
print(("-=")*30)
print(f"{jogador['nome']}, {jogador['gols']}, {jogador['total']}")
print(("-=")*30)
for c,v in jogador.items():
    print(f"O campo {c} tem o valor {v}")
for i, g in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')