# ============================================================
# DESAFIO 042 - ANALISANDO TRIÂNGULOS V2.0
# Objetivo: Ler três segmentos de reta e calcular:
# 1. Se eles podem formar um triângulo.
# 2. Se formarem, classificar em: EQUILÁTERO, ISÓSCELES ou ESCALENO.
# Diferencial: Uso de IFs aninhados para otimizar a lógica.
# ============================================================
print("="*10,"Bem-vindo ao PYramide", "="*10 )
# l = lado
l1 = float(input("Primeiro segmento: "))
l2 = float(input("Segundo segmento: "))
l3 = float(input("Terceiro segmento: "))

# Verificando se é triângulo ou não
if l1 < l2 + l3 and l2 < l1 + l3  and l3 < l1 + l2:
    print("Com esss segmentos você consegue formar um triângulo ", end="")
    # Verifica o tipo (este IF está "dentro" do anterior)
    if l1 == l2 == l3:
        print("e esse triângulo é Equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("e esse triângulo é Isóceles")
    else:
        print("e esse triângulo é Escaleno")
else:
    print("Os segmentos informados não podem formar triângulos")