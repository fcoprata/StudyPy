contadorLet = lambda lista: [len(x) for x in lista]
lista_animais = ['cachorro', 'gato', 'arara', 'urubu', 'ornitorrinco']
print(contadorLet(lista_animais))

soma = lambda a,b: a + b
print(soma(5,10))
sub = lambda a,b: a - b
print(sub(10,5))

calculadora = {
    'soma':lambda a,b: a + b,
    'sub':lambda a,b: a - b,
    'mult':lambda a,b: a*b,
    'div':lambda a,b: a/b,
}
soma = calculadora['soma']
sub = calculadora['sub']
mult = calculadora['mult']
div = calculadora['div']
print(f'A soma é {soma(10,5)}')
print(f'A multiplicação é {mult(10,2)}')