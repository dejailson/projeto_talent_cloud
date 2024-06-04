def calular_idade(ano_nasc,ano_base):
    if not ano_nasc.isdigit():
        raise AttributeError('Informe um valor do tipo inteiro')
    ano_nasc = int(ano_nasc)
    if ano_nasc < 1922 or ano_nasc > 2021:
        raise ValueError('Informe um valor entre 1922 e 2021')
    return ano_base - ano_nasc


if __name__ == '__main__':
    to_stop = False
    ano_base = 2022
    
    while(not to_stop):
        try:
            ano_nasc = input('Informe o ano de nascimento: ')
            idade = calular_idade(ano_nasc,ano_base)
            print(f'A idade é: {idade}')
            to_stop = True
        except ValueError as ve:
            print(ve)
        except AttributeError as ae:
            print(ae)