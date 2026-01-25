# ============================================================
# DESAFIO 040 - MÉDIA ESCOLAR
# Objetivo: Ler duas notas de um aluno e calcular sua média, 
# mostrando uma mensagem final de acordo com o resultado:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: EM RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
# ============================================================
primeira_nota = float(input("Primeira nota: "))
segunda_nota = float(input("Segunda nota: "))

media = (primeira_nota + segunda_nota) / 2 #Pegar a média do aluno

if media >= 7: # Se a média for maior ou igual a 7 o aluno será aprovado
    print(f"Sua média final foi {media} PYrabéns!  ")
elif media >= 5: # Caso seja maior ou igual a 5 ele estará em recupreração  
    print(f"Sua média final foi {media} e você de recuperação continue se esforçando ")
else:
    print(f"Sua média final foi {media} te vejo no próximo ano. ")

# Não existe conflito entre if e elif pois o if e o primeiro da fila, ou seja se ele for verdadeiro
# ele ignora o resto.