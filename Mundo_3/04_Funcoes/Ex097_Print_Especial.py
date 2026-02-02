# ==============================================================================
# Desafio: 097
# Tema: Um print especial
# Enunciado: Faça um programa que tenha uma função chamada escreva(), que receba 
#            um texto qualquer como parâmetro e mostre uma mensagem com tamanho 
#            adaptável.
#
# Exemplo:
# escreva('Olá, Mundo!') 
# Saída:
# ~~~~~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~~~~~
# ==============================================================================
def escreva(txt):
    tamanho = len(txt) + 4
    print("="* tamanho)
    print(f'  {txt}')
    print('='*tamanho)

escreva("Meu nome é Vitor")
escreva("Foco nos estudos")
escreva("Python é foda")