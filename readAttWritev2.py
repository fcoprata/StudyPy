
def write(texto):
    diretorio = 'C:/Code/Study.py/alunos.txt'
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

if __name__ == '__main__':
    aluno = '\nRoberto,7,2,10,8'
    att_alunos('alunos.txt', aluno)
