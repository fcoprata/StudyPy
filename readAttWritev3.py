def write(texto):
    diretorio = 'C:/Code/Study.py/notas.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def att_alunos(nome_arquivo, texto):
    arquivo = open(nome_arquivo,'a')
    arquivo.write(texto)
    arquivo.close()

def read_alunos(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    notaAluno = arquivo.read()
    notaAluno = notaAluno.split('\n')
    lista_media = []
    for x in notaAluno:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        average = lambda notas: sum([int(i) for i in notas]) / 4
        print(average(lista_notas))
        lista_media.append({aluno:average(lista_notas)})
    return lista_media

if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    print(lista_media)

