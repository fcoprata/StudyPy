from datetime import date,time,datetime

def usingDate(): #uso para identificação de data
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%A-%B'))

def usingTime(): #uso mais manual, para ajuste de horario
    horario = time(hour=17,minute=35,second=00)
    print(horario)

def usingDateTime(): #uso geral
    data_atual = datetime.now()
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%H:%M:%S'))
    #print(data_atual.strftime('%c')) #diretiva mais completa
    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo')
    print(tupla[data_atual.weekday()]) #maneira de sair traduzido

if __name__ == '__main__':
    usingTime()
    usingDate()
    usingDateTime()

