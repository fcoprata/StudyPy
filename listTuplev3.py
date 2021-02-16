animal = input('Qual é o animal:')
lista_animal = ['gato','cachorro','elefante']

if animal.lower() in lista_animal:
    print('Existe {} na lista'.format(animal.lower()))
else:
    print('Não existe {} na lista'.format(animal.lower()))
    lista_animal.append(animal.lower())
    print('Mas iremos acrescentar!!!\n')
    print(lista_animal)


#Para retirar o ultimo elemento da lista
#coloca lista_animal.pop()
#se não especificar a posição dele, irá tirar o último
#caso deseje retirar a posição
# lembresse de que é posição-1, pois começa em 0

#caso queira remover elemento que já conhece
#usa lista_animal.remove('elemento')
