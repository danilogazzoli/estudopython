import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #sg.preview_all_look_and_feel_themes()
        sg.change_look_and_feel('Material2')
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(60,0), key='nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(2,0),tooltip='Digite a idade',key='idade')],
            [sg.Text('Qual o provedor de email?')],
            [sg.Checkbox('Gmail',key='gmail'), sg.Checkbox('Yahoo',key='yahoo'), sg.Checkbox('Outlook',key='outlook')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartoes',key='simAceita'), sg.Radio('Não','cartoes',key='naoAceita')],
            [sg.Slider(range=(0,255), default_value=0, orientation='h', size=(15,20), key='velocidade')],
            [sg.Button('Enviar Dados')]
        ]

        self.janela = sg.Window("Dados do usuário").layout(layout)



    def iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            print(self.values)
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            sim_Aceita = self.values['simAceita']
            nao_Aceita = self.values['naoAceita']
            velocidade = self.values['velocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita cartão: { "Sim" if (sim_Aceita == True ) else "Não"}')
            print(f'Velocidade Script: {velocidade}')
        
        


tela = TelaPython()
tela.iniciar()