def colorir(msg, cor_nome):
    codigos = {
        'limpa': '\033[m',
        'preto': '\033[1;30m',
        'vermelho': '\033[1;31m',
        'verde': '\033[1;32m',
        'amarelo': '\033[1;33m',
        'azul': '\033[1;34m',
        'roxo': '\033[1;35m',
        'ciano': '\033[1;36m',
        'cinza': '\033[1;37m',
        'branco': '\033[1;97m',
        'inverso': '\033[7;30m'
    }
    return f"{codigos.get(cor_nome, codigos['limpa'])}{msg}{codigos['limpa']}"

# --- Funções de Atalho (Simplicidade Total) ---
def preto(m): return colorir(m, 'preto')
def vermelho(m): return colorir(m, 'vermelho')
def verde(m): return colorir(m, 'verde')
def amarelo(m): return colorir(m, 'amarelo')
def azul(m): return colorir(m, 'azul')
def roxo(m): return colorir(m, 'roxo')
def ciano(m): return colorir(m, 'ciano')
def cinza(m): return colorir(m, 'cinza')
def branco(m): return colorir(m, 'branco')
def inverso(m): return colorir(m, 'inverso')

# O SEGREDO: O '*' só funciona se os nomes estiverem nesta lista:
__all__ = [
    'preto', 'vermelho', 'verde', 'amarelo', 
    'azul', 'roxo', 'ciano', 'cinza', 'branco', 'inverso'
]
