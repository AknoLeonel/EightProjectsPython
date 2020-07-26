import random

import PySimpleGUI as sg


class Dado:

    def __init__(self):
        self.janela = sg.Window('Simulador de Dados', layout=self.Layout)
        self.valormin = 1
        self.valormax = 6
        self.mensagem = 'Voce gostaria de gerar um novo valor ?'
        # Layout
        self.Layout = [
            [sg.Text('Jogar o dado')],
            [sg.Button('sim'), sg.Button('nao')]
        ]

    def Inicar(self):
        self.eventos, self.valores = self.janela.Read()

        try:
            if self.eventos == 'Sim' or self.eventos == 'sim':
                self.GerarValorDoDado()
            elif self.eventos == 'Nao' or self.eventos == 'nao':
                print('Ok, Agradecemos sua participaçao')
            else:
                print('Favor digitar Sim ou Nao')
        except:
            print('ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valormin, self.valormax))


simulador = Dado()
simulador.Inicar()
