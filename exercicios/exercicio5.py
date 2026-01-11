despesas = float(input("Digite o total de despesas do mês: \n"))
if(despesas<3000):
    print(f"Você esta dentro do orçamento em R${3000 - despesas}")
else:
    print(f"Você está acima do orçamento em R${3000- despesas}")