conjunto1 = {1,2,3}
conjunto2 = {1,2,3,4,5,6}
set_subset = conjunto1.issubset(conjunto2)
set_subset2 = conjunto2.issubset(conjunto1)
print(set_subset) #conjunto está contido no conjunto 2
print(set_subset2) #conjunto2 não está contido no conjunto 1


#.issubset -> define se um conjunto está contido em outro
#.issuperset -> define se o conjunto contém os outros conjuntos

#caso de conversão de lista em conjunto, para retirada de duplicidade
lista = [1,2,2,3,4,5]
conjunto3 = set(lista)
print(conjunto3)
listaNum = list(conjunto3)
print(listaNum)