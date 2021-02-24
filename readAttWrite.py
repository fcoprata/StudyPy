
def escrever_arq(texto):
    diretorio = 'C:/Code/teste.txt' #meu diretorio
    arquivo = open(diretorio,'w')
    arquivo.write(texto)
    arquivo.close()
def att_arq(texto):
    arquivo = open('teste.txt','a')
    arquivo.write(texto)
    arquivo.close()
def read_arq(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
if __name__ == '__main__':
    escrever_arq('Primeira linha.\n')
    #att_arq('Segunda linha.')
    #read_arq('teste.txt')