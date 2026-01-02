import os

temperatura = int(input('Digite a temperatura atual:'))
if temperatura >= 25:
    os.system('cls')
    print(f'Temperatura {temperatura}°C')
    print('Alerta! Temperatura acima do limite permitido')
else:
    os.system('cls')
    print(f'Temperatura {temperatura}°C')
    print("Temperatura dentro do limite seguro.")
