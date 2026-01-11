horario_de_entrada = int(input("Digite a hora atual (Formato 24 horas):"))
if horario_de_entrada >=8 and horario_de_entrada <= 18:
    print("Acesso permitido.")
else:
    print('Acesso negado!')