def aumentar(preço=0, taxa=0, format=False):
    res = preço + (preço * taxa/100)
    return res if not format else moeda(res)


def diminuir(preço=0, taxa=0, format=False):
    res = preço - (preço * taxa/100)
    return res if format is False else moeda(res)


def dobro(n=0, format=False):
    res = n * 2
    return res if format is False else moeda(res)

def metade(n=0, format=False):
    res = n / 2
    return res if not format else moeda(res)

def moeda(preço=0, moeda = "R$"):
    return f"{moeda}{preço:.2f}".replace('.',',')

def resumo(n=0, taxa_a=10, taxa_r=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{taxa_a}% de aumento: \t{aumentar(n, taxa_a, True)}')
    print(f'{taxa_r}% de redução: \t{diminuir(n, taxa_r, True)}')
    print('-' * 30)