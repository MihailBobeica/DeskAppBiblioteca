import PySimpleGUI as sg
#ciao
layout = [  [sg.Text('Name'), sg.Input(key='-NAME-')],
            [sg.Text('Address'), sg.Input(key='-ADDRESS-')],
            [sg.Text('City and State'), sg.Input(key='-CITY AND STATE-')],
            [sg.Ok(), sg.Cancel()]]

window = sg.Window('Simple Inputs', layout, element_justification='r')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

window.close()
