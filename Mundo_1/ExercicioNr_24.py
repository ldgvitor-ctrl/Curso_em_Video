cidade = input("Qual cidade você nasceu? ").strip()
#Verificador se a pessoa nasceu ou não em uma cidade que começa com santo
print(cidade[:5].upper() == "SANTO")