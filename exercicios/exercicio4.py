peso = float(input("Digite seu peso: \n"))
altura = float(input("digite sua altura: \n"))
imc = peso / (altura **2)
if (imc<18.5):
    print(f"Parabéns! Você está abaixo do peso! Seu IMC é {imc}")
elif(18.5 <= imc <25):
    print(f"Parabéns! Você está dentro peso! Seu IMC é {imc}")
else:
    print(f"Você está acima do peso! Seu IMC é {imc}")