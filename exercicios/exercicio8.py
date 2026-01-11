km = int(input("Digite a distância percorrida (em km): \n"))
if(km <= 100):
    pedagio = 10
    print(f"Valor do pedágio: R${pedagio}")
elif(100 < km <= 200):
    pedagio = 20
    print(f"Valor do pedágio: R${pedagio}")
else:
    pedagio = 30
    print(f"Valor do pedágio: R${pedagio}")