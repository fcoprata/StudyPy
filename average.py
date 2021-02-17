n = int(input('Quantos números seram? '))
soma = 0
lista = []
for n in range(n):
    num = int(input('Digite um número: '))
    lista.append(num)
media = sum(lista)/len(lista)
print('A média é de {}'.format(media))

#Para executar a questão com expertise, necessitei usar recursos obtidos
#nas aulas de tuplas e listas