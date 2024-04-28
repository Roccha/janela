import PySimpleGUI as sg

layout = [  [sg.Text("Digite seu nome:")],
            [sg.InputText()],
            [sg.Text("Digite sua senha:")],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
            ]

window = sg.Window ('Olá', layout)
while True:
         event,values = window.read()
         if event == sg.WIN_CLOSED or event == 'Cancel':
             break
         print('Olá ', values[0],'Você agora esta logado' '!')

         window.close()