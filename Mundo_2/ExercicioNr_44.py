# ============================================================
# DESAFIO 044 - GERENCIADOR DE PAGAMENTOS
# Objetivo: Calcular o valor a ser pago por um produto, 
# considerando o seu preço normal e a condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto.
# - À vista no cartão: 5% de desconto.
# - Em até 2x no cartão: preço formal.
# - 3x ou mais no cartão: 20% de juros.
# ============================================================

print("="*10, " LOJA PY-STORE ", "="*10)
preco = float(input("Preço das compras: R$ "))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input("Qual é a opção? "))
# Processamento das condições de pagamento

if opcao == 1: # Cálculo para 10% de desconto
    desconto = preco * 0.1
    somat = preco - desconto
    print(f"Sua compra de R${preco:.2f} ficou R${somat:.2f} com 10% de desconto")
elif  opcao == 2: # Cálculo para 5% de desconto
    desconto = preco * 0.05
    somat = preco - desconto
    print(f"Sua compra de R${preco:.2f} ficou R${somat:.2f} com 05% de desconto")
elif opcao == 3: # Preço normal dividido em 2 parcelas
    parcela = preco / 2
    print(f"Sua compra de R${preco:.2f} ficou em 2x de R${parcela:.2f} ")
elif opcao == 4: # Acréscimo de 20% de juros
    juros = preco * 0.2
    parcela = (juros + preco) / 3
    print(f"Sua compra de R${preco:.2f} ficou em 3x de R${parcela:.2f} com R${juros:.2f} de juros ")
else:
   # Tratamento de erro caso o usuário digite uma opção que não existe
    print("Opção inválida")

print("Obrigado por comprar na PY-STORE")
