# ==============================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# ==============================================================================
# Desafio: 083
# Tema: Validando expressões matemáticas
# Enunciado: Crie um programa onde o usuário digite uma expressão qualquer que 
#            use parênteses. Seu aplicativo deverá analisar se a expressão 
#            passada está com os parênteses abertos e fechados na ordem correta.
# ==============================================================================
lista = [] 
impar = []
par = []
while True:
    while True:
        try:
            numero = int(input("Digite um número! "))
            lista.append(numero)
            lista.sort()
            break
        except ValueError:
            print("Digite apenas números inteiros!  ")
    while True:
        pergunta = input("Você quer continuar? [S/N] ").strip().upper()[0]
        if pergunta not in "SN":
            print("Digite apenas sim ou não")
        else:
            break
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero) 
    
    if pergunta == "N":
        break
print("="*20, f"{"Resultados":^15}", "="*20 )
print(f"Você digitou os números {lista}")
print(f"Os números {par} são números pares! ")
print(f"Os números {impar} são ímpares! ")