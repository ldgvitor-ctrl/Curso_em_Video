# ============================================================
# DESAFIO 065 - MAIOR E MENOR VALORES
# Objetivo: Crie um programa que leia vários números inteiros. 
# No final, mostre a média entre todos e qual foi o maior e 
# o menor valores lidos. O programa deve perguntar ao usuário 
# se ele quer ou não continuar a digitar valores.
# ============================================================
contador = soma = maior = menor = 0
pergunta = "S"
while pergunta == "S": # Começa com S para entrar no loop
    numero = int(input("Digite um número: "))
    contador += 1
    soma += numero
# Lógica para definir maior e menor
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
# Validação da pergunta para continuar
    pergunta = input("Você Quer continuar ? [S/N]").strip().upper()[0]
    while pergunta not in ["S","N"]:
        print("Opção inválida. Quer continuar? [S/N]: ")

media = soma / contador
print(f"Você digitou {contador} números e a média foi {media:.2f}")
print(f"O maior número foi {maior} e o menor foi {menor}")
    

