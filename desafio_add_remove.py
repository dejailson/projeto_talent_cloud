lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

if __name__ == '__main__':
    print(lista_produtos)
    lista_produtos[1] = 'rímel'
    lista_produtos[4] = 'cremes hidratantes'
    lista_produtos.pop()
    print(lista_produtos)
    
    lista_produtos.append('Locão pós-barba')
    lista_produtos.append('pó compacto')
    print(lista_produtos)