nota1 = float(input('Digite a sua 1 nota: '))
nota2 = float(input('Digite a sua 2 nota: '))
nota3 = float(input('Digite a sua 3 nota: '))
media = (nota1 + nota2 + nota3) /3
if media>=7:
    print(f'Aprovado')
elif media >= 5 and media <7:
    print(f'Recuperação')
else:
    print(f'Reprovado')
