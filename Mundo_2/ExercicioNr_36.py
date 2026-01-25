# ==========================================
# DESAFIO 036 - APROVAÇÃO DE EMPRÉSTIMO
# Objetivo: Calcular prestação bancária e validar margem de 30% do salário.
# ==========================================

print("="*10, "BANCO PYTHONISTA", "="*10)

# Entrada de dados com conversão de tipos
casa = float(input("Valor do imóvel: R$"))
salario = float(input("Salário mensal: R$"))

# Cálculo de anos para meses diretamente na entrada
meses = float(input("Anos de financiamento: ")) * 12

# Fórmulas de decisão
prestacao = casa / meses
minimo = salario * 0.3  # Representa 30% do salário

print(f"Para pagar uma casa de R${casa:.2f} em {meses/12:.0f} anos,", end=' ')
print(f"a prestação será de R${prestacao:.2f}")

if prestacao <= minimo:
    print("\033[32mEmpréstimo pode ser CONCEDIDO!\033[m")
elif prestacao <= salario * 0.5:
    # Caso a prestação esteja entre 30% e 50%
    print("\033[33mEmpréstimo em ANÁLISE (Compromete mais de 30%)\033[m")
else:
    print("\033[31mEmpréstimo NEGADO!\033[m")