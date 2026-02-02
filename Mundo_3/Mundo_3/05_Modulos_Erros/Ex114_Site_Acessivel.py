# ==============================================================================
# Desafio: 114
# Tema: Acessibilidade de sites
# Enunciado: Crie um código em Python que teste se o site Pudim (pudim.com.br) 
#            está acessível pelo computador usado.
# ==============================================================================
import urllib.request
from modulos.cores import *

def teste_site(url):
    try:
        # Tenta abrir o site
        site = urllib.request.urlopen(url)
    except Exception as erro:
        # Se der qualquer erro (sem internet, site fora do ar, etc)
        print(f"{vermelho('O site não está acessível no momento.')}")
        # print(f"Erro encontrado: {erro}") # Opcional para ver o erro real
    else:
        # Se ele conseguiu abrir sem erros
        print(f"{verde('Consegui acessar o site com sucesso!')}")
        # print(site.read()) # Isso aqui leria o código HTML do site!

# Testando o famoso site do Pudim
teste_site('http://www.pudim.com.br')