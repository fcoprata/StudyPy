a = int(input('Entre com um valor :'))
b = int(input('Entre com um valor :'))

resto_a = a % 2
resto_b = b % 2
if resto_a == 1 or resto_b == 1:
    print('algum número é ímpar')
else:
    print('somente números é par')
