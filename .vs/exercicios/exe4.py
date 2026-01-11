import os
peso = float((input("Digite o seu peso: ")))
altura = float((input("Digite sua altura: ")))
os.system("cls")
imc = peso/(altura**2)
print(f'Seu IMC é {imc:.2f}')
if imc < 18.5:
    print('Parabéns você esta abaixo do peso')
elif imc < 25:
    print('Parabéns você esta no peso normal')
else:
    print('Você está acima do peso') 

