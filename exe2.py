import os
def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    Outputs:
    - Retorna ao menu principal'''
    os.system('cls')
    print('Erro os dias não podem ser negativados\n')
    menu_inicial()
def menu_inicial():
    atividade_A = int(input("Digite os dias para a atividade A:"))
    atividade_B = int(input("Digite os dias para a atividade B:"))
    atividade_C = int(input("Digite os dias para a atividade C:"))

    if atividade_A >= 0 and atividade_B >=0 and atividade_C >=0:
        os.system('cls')
        print(f'Atividade A {atividade_A} dias \nAtividade B {atividade_B} dias \nAtividade C {atividade_C} Dias')
    else:
        opcao_invalida()

if __name__ == '__main__':
    menu_inicial()