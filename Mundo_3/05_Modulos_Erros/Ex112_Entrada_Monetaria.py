# ==============================================================================
# Desafio: 112
# Tema: Entrada de dados monetários
# Enunciado: Dentro do pacote utilidadesCeV que você criou no desafio 111, 
#            tem um módulo chamado dado. Crie uma função chamada leiaDinheiro() 
#            que seja capaz de funcionar como a função input(), mas com uma 
#            validação de dados para aceitar apenas valores que sejam monetários.
# ==============================================================================
from utilidadesCeV import moeda, dado
p = dado.leiaDinheiro("Digite o preço: R$ ")
moeda.resumo(p, 35, 22)