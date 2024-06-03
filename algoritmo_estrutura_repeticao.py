def imprimir_andares_ordem_crescente():
    for i in range(1,21):
        if i != 13:
            print(f'{i}o andar')
            
def imprimir_andares_ordem_decrescente():
    contador = 20
    while contador > 0:
        if contador != 13:
            print(f'{contador}o andar')
        contador -= 1

if __name__ == "__main__":
    imprimir_andares_ordem_crescente()
    print('##### IMPRIMINDO EM ORDEM DECRESCENTE #################')
    imprimir_andares_ordem_decrescente()