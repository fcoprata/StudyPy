n1 = int(input('Primeiro Número : '))
n2 = int(input('Segundo Número : '))

class Calculadora:
    # Opcional já que não inicializa
    # def __init__(self):
    #     pass

    def soma(self,a,b):
        return a + b
    def sub(self,a,b):
        return a - b
    def mult(self,a,b):
        return a * b
    def div(self,a,b):
        return a / b
if __name__ == '__main__':
    calculadora = Calculadora()
    print(calculadora.soma(n1,n2))
    print(calculadora.mult(n1,n2))
    print(calculadora.div(n1,n2))
    print(calculadora.sub(n1,n2))
