def contLe(listap):
    contador = []
    for x in listap:
        qtd = len(x)
        contador.append(qtd)
    return contador

if __name__ == '__main__':
    lista = ['cachorro','gato','arara','urubu','ornitorrinco']
    print(contLe(lista))