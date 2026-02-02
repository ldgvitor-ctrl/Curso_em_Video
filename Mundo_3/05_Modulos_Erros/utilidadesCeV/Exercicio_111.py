from utilidadesCeV import moeda, dado

# Agora usamos o dado.leiaDinheiro para garantir que o programa não quebre
p = dado.leiaDinheiro("Digite o preço: R$ ")
moeda.resumo(p, 35, 22)