from tv import Tv
from calcDef import Calculadora
from counterLetters import contLe

tv = Tv()
print(tv.ligada)
tv.power()
print(tv.ligada)
calc = Calculadora(10,5)
print(calc.soma())
print(calc.mult())
lista = ['cachorro', 'gato', 'arara', 'urubu', 'ornitorrinco']
print(contLe(lista))