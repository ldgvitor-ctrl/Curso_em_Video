salario_funcionario = float(input("Qual é o valor que o funcionário recebe R$ "))
if salario_funcionario > 1250:
    aumento = salario_funcionario * 0.1 # Cauculando o aumento
else:
    aumento = salario_funcionario * 0.15 # Cauculando o aumento
novo_salario = aumento + salario_funcionario
print(f"O salário de R${salario_funcionario:.2f} foi para R${novo_salario:.2f} com o aumento de R${aumento:.2f}")