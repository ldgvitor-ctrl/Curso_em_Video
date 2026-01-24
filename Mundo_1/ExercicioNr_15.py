Dias_alugado = int(input("Digite o número de dias que o carro foi alugado: "))
Km_percorridos = float(input("Digite o número de quilômetros percorridos: "))
Custo_fixo_dia = 60.00 # custo fixo por dia de aluguel
Custo_por_km = 0.15 # custo por quilômetro rodado
Custo_total = (Dias_alugado * Custo_fixo_dia) + (Km_percorridos * Custo_por_km) # calcular o custo total
print(f"O custo total do aluguel do carro é: R$ {Custo_total:.2f}")# 15. Escreva um programa que pergunte a quantidade de dias que um carro foi 