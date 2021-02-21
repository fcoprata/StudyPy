class Tv:
    def __init__(self):
        self.ligada = False
        self.canal = 5
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    def plschanel(self):
        self.canal += 1
    def leschanel(self):
        self.canal -= 1
televisão = Tv()
if __name__ == '__main__':
    power = input('Deseja ligar Tv?')
    if power.upper()[0] == 'S':
        if televisão.ligada == False:
            televisão.power()
            print('Tv ligando')
            chanel = input('Deseja mudar de canal?')
        if chanel.upper()[0] == 'S':
            change = input('Mudar para mais ou menos? ')
            if change.lower() == 'mais':
                televisão.plschanel()
                print(f'A canal agora é {televisão.canal}')
            elif change.lower() == 'menos':
                televisão.leschanel()
                print(f'O canal agora é {televisão.canal}')
