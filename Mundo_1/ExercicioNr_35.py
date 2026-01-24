print("="*10, "Analizador de triânuglos", "="*10)
a = float(input("Digite um valor: "))
b = float(input("Digite um valor: "))
c = float(input("Digite um valor: "))
if a + b > c and a + c > b and b + c > a:
    print("Você consegue fazer um triângulo com essas medias")
else:
    print("Você não consegue fazer um triângulo com essas medidas")