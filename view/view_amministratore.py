import PySimpleGUI as sg


def view_amministratore():
    view_amministratore = [[sg.Button('Gestione operatori')],[sg.Button('Gestione libri')]]
    window_amministratore = sg.Window('Amministratore',view_amministratore)
    return window_amministratore.read()

