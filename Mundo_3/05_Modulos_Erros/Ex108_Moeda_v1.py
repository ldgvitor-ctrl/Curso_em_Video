# ==============================================================================
# Desafio: 108
# Tema: Formatando Moedas em Python
# Enunciado: Adapte o código do desafio 107, criando uma função adicional 
#            chamada moeda() que consiga mostrar os números como um valor 
#            monetário formatado (Ex: R$10,00).
# ==============================================================================
from modulos import moeda108

p = float(input("Digite o preço: R$ "))
print(f"A metade de {moeda108.moeda(p)} é {moeda108.metade(p)}")
print(f"O dobro  de {p} é {moeda108.dobro(p)} ")
print(f"O Aumentando 10% , temos {moeda108.aumentar(p, 10)}")