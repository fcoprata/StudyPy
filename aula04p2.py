a = int(input('Até qual valor? '))
for num in range(a+1):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        if resto == 0:
            div += 1
    if div == 2:
        print(num)
