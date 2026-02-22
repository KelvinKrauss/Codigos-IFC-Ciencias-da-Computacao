cr = int(input("digite os anos a serem convertidos para anos de cachorro :"))
idadedecachorro = 0
if cr < 0 :
    print("Idade invalida")
elif cr <= 2 :
    idadedecachorro = cr * 10.5 
    print(f"a idade é {idadedecachorro}")
elif cr > 2 :
    idadedecachorro = cr = 21 + (cr - 2) * 4
    print(f"a idade é {idadedecachorro}")