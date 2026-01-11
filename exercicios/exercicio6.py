hora = int(input("Digite a hora atual: \n"))
if(8 <= hora < 18):
    print(f"Acesso permitido, restam {18 - hora} horas restantes.")
else:
    print("Acesso negado!")