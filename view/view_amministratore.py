import PySimpleGUI as sg


def view_amministratore():
    view_amministratore = [[sg.LabeledButton('Gestione operatori')], [sg.LabeledButton('Gestione libri')]]
    window_amministratore = sg.Window('Amministratore',view_amministratore)
    return window_amministratore.read()

