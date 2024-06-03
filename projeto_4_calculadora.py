def calcular(num_1, num_2,oper):
    if oper == 1:
        return num_1 + num_2
    elif oper == 2:
        return num_1 - num_2
    elif oper == 3:
        return num_1 * num_2
    elif oper == 4:
        return num_1 / num_2
    else:
        return 0
    
if __name__ == '__main__':
    num_1 = int(input('Digite o primeiro número: '))
    num_2 = int(input('Digite o segundo número: '))
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    oper = int(input('Digite a operação desejada: '))
    resultado = calcular(num_1, num_2, oper)
    print(f'O resultado da operação é: {resultado}')