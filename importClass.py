from tv import Tv
from calcDef import Calculadora

tv = Tv()
print(tv.ligada)
tv.power()
print(tv.ligada)
calc = Calculadora(10,5)
print(calc.soma())
print(calc.mult())