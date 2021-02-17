n = int(input('Quantos números seram? '))
soma = 0
lista = []
for n in range(n):
    num = int(input('Digite um número: '))
    lista.append(num)
media = sum(lista)/len(lista)
print('A média é de {}'.format(media))
