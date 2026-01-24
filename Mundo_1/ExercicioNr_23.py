numero  = int(input("Digite um número inteiro: "))
milhar = numero // 1000 % 10 # Pega o resto da divisão por 1000
centena = numero // 100 % 10 # Pega o resto da divisão por 100
dezena = numero // 10 % 10 # Pega o resto da divisão por 10
unidade = numero // 1 % 10 # Pega o resto da divisão por 1
print(f"O número {numero} contém: \nUnidade: {unidade} \nDezena:{dezena} \nCentena: {centena} \nMilhar: {milhar}")
