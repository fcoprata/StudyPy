#diferença de tupla para lista, é a mutabilidade
#ou capacidade de alterar, na lista é possível
#a tupla não permite
#lista usa [], tupla usa ()
print('Caso queira ver a tupla inteira, coloque 0')
num = int(input('Caso queira ver apenas uma posição:'))
tupla = (2,3,5,7)
if num > 0:
    print(tupla[num-1])
else:
    print(tupla)
