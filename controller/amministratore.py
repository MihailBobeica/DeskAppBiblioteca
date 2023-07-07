import PySimpleGUI as sg
from view import view_amministratore
import gestioneOperatore

def amministratore():
    while True:
        event, values = view_amministratore.view_amministratore()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'Gestione operatori':
            gestioneOperatore.gestione_operatore()
        elif event == 'Gestione libri':
            pass

amministratore()