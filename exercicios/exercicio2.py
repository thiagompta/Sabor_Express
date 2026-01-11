a = int(input("Informe os dias para a atividade A: /n"))
b = int(input("Informe os dias para a atividade B: /n"))
c = int(input("Informe os dias para a atividade C: /n"))

if (a >=0 and b >=0 and c >=0):
    tempo_total = a + b + c
    print(f"O tempo total é de {tempo_total} dias")
else:
    print("Erro: os dias nâo podem ser negativos \n") 