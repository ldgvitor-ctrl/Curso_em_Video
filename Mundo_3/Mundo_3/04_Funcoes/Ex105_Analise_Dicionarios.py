# ==============================================================================
# Desafio: 105
# Tema: Analisando e gerando Dicionários
# Enunciado: Faça um programa que tenha uma função notas() que pode receber 
#            várias notas de alunos e vai retornar um dicionário com as 
#            seguintes informações:
#            - Quantidade de notas
#            - A maior nota
#            - A menor nota
#            - A média da turma
#            - A situação (opcional)
# ==============================================================================
def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r ['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >=7:
            r['situação'] = "Boa!"
        elif r['média'] >=5 :
            r["situação"] = "Razoavel, melhore"
        else:
            r['situação'] = 'Ruim'
    
    return r


entrada = input("Digite as notas separadas por espaço: ").split()
notas_lista = [float(nota) for nota in entrada]

resp = notas(*notas_lista, sit=True)
print(resp)