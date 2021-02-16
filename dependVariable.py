a = int(input("Primeiro valor:"))
b = int(input("Segundo valor:"))
c = int(input("Terceiro valor:"))
if a > b and a > c:
    print('O número A = {}, é o maior'.format(a))
    if b > c:
        print('B é maior que C , pois {} > {}'.format(b,c))
        print("{} > {} > {}".format(a,b,c))
    else:
        print('C é maior que B, pois {} > {}'.format(c,b))
        print("{} > {} > {}".format(a, c, b))
elif b > a and b > c :
    print('O número B = {}, é o maior'.format(b))
    if a > c:
        print('A é maior que C , pois {} > {}'.format(a, c))
        print("{} > {} > {}".format(b, a, c))
    else:
        print('C é maior que A, pois {} > {}'.format(c, a))
        print("{} > {} > {}".format(b, c, a))

elif c > a and c > b:
    print('O número C = {}, é o maior'.format(c))
    if a > b:
        print('A é maior que B , pois {} > {}'.format(a, b))
        print("{} > {} > {}".format(c, a, b))
    else:
        print('B é maior que A, pois {} > {}'.format(b, a))
        print("{} > {} > {}".format(c, b, a))
