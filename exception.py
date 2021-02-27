
lista = [1,10]
try:
    arquivo = open('alunos.txt', 'r')
    divisão = 10/1
    num = lista[1]
except ZeroDivisionError:
    print('Não é possivel dividir por 0 ')
except IndexError:
    print('Erro ao acessar indice invalido da lista')
except BaseException as ex:
    print(f'erro {ex}')
else:
    print('Executa quando ocorrer exceção')
finally:
    print('sempre executa')
    arquivo.close()
