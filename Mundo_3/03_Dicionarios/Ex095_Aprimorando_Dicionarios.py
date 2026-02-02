# ==============================================================================
# PROJECT: Team Performance Analytics System
# ==============================================================================
# Desafio: 095
# Tema: Aprimorando os Dicionários
# Enunciado: Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, 
#            incluindo um sistema de visualização de detalhes do aproveitamento 
#            de cada jogador.
#
# REQUISITOS TÉCNICOS:
#   1. Cadastro de múltiplos jogadores em uma lista.
#   2. Cada jogador deve ter: Nome, Partidas, Gols (lista) e Total.
#   3. Exibir uma tabela formatada com o resumo de todos os jogadores (cabeçalho).
#   4. Implementar um sistema de busca por índice: o usuário digita o código do
#      jogador e o programa exibe o detalhamento de cada partida dele.
#   5. O programa para quando o usuário digitar um código de saída (ex: 999).
# ==============================================================================


jogador = {}
valor = []
jogadores = []
while True:
    jogador.clear()
    valor.clear()
    jogador['nome'] = input("Nome do jogador:  ")
    partidas = int(input("Quantas partidas o jogador teve?  "))
    
    for c in range(0, partidas):
        gols = int(input(f"Quantos gols na partida  foram na {c+1}° partida?  "))
        valor.append(gols)
    jogador['gols'] = valor[:]
    jogador['total'] = sum(valor[:])
    jogadores.append(jogador.copy())
    
    while True:
        pergunta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if pergunta in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    
    if pergunta == "N":
        break

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)

for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}:')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)