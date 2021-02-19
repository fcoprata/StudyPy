#método = definição -> def

class Calculadora:
    def __init__(self, n1, n2):
        self.a = n1
        self.b = n2
    def soma(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mult(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

calculadora = Calculadora(10,2)
print(calculadora.soma())
print(calculadora.mult())
print(calculadora.div())
print(calculadora.sub())
