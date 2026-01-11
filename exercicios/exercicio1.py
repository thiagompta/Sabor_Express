import os

macas = int(input("Digite a quantidade de maçãs vendidas: \n"))
bananas = int(input("Digite a quantidade de bananas vendidas: \n"))
if macas > bananas:
    print("As maçãs tiveram mais vendas.")
elif bananas > macas:
    print("As bananas tiveram mais vendas.")
else:
    print("As vendas foram iguais.")