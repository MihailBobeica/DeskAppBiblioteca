import PySimpleGUI as sg
from model import Operatore
from controller import gestioneOperatore
import pickle




view_gestione_operatore = [[sg.Button('Inserisci un nuovo operatore')],
                     [sg.Button('Visualizza un operatore')],
                     [sg.Button('Modifica un operatore')],
                     [sg.Button('Elimina un operatore')]]

view_ricerca_operatore = [[sg.Text('Codice fiscale'), sg.Input(key='codiceFiscale')],[sg.Button('Cerca')]]


window_gestione_operatore = sg.Window('Gestione operatore', view_gestione_operatore)

while True:
    event, values = window_gestione_operatore.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Inserisci un nuovo operatore':
        window_ricerca_operatore = sg.Window('Ricerca operatore', view_ricerca_operatore)
        while True:
            event9, values9 = window_ricerca_operatore.read()
            if event9 == sg.WINDOW_CLOSED:
                break
            elif event9 == 'Cerca':
                operatore = Operatore.Operatore.ricerca_operatore(str(values9['codiceFiscale']))
                if operatore:
                    inserisciOperatore = [[sg.Text("L'operatore è già stato inserito")]]
                    window_inserisci_operatore = sg.Window('Inserisci operatore', inserisciOperatore)
                    while True:
                        event10, values10 = window_inserisci_operatore.read()
                        if event10 == sg.WINDOW_CLOSED:
                            break
                else:

                    inserisciOperatore = [[sg.Text('Codice fiscale'),sg.Input(str(values9['codiceFiscale']), key='codiceFiscale',readonly=True)],
                                          [sg.Text('Nome'), sg.Input(key='nome')],
                                          [sg.Text('Cognome'), sg.Input(key='cognome')],
                                          [sg.Text('email'), sg.Input(key='email')],
                                          [sg.Text('Telefono'), sg.Input(key='telefono')],
                                          [sg.Button('Invia')]]
                    window_inserisci_operatore = sg.Window('Inserisci operatore', inserisciOperatore)
                    while True:
                        event2, values2 = window_inserisci_operatore.read()
                        if event2 == sg.WINDOW_CLOSED:
                            break
                        elif event2 == 'Invia':
                            Operatore.Operatore.inserisci_operatore(values2)
                            window_inserisci_operatore.close()

    elif event == 'Visualizza un operatore':
        window_ricerca_operatore = sg.Window('Ricerca operatore', view_ricerca_operatore)
        while True:
            event3, values3 = window_ricerca_operatore.read()
            if event3 == sg.WINDOW_CLOSED:
                break
            elif event3 == 'Cerca':
                operatore = Operatore.Operatore.ricerca_operatore(str(values3['codiceFiscale']))
                if operatore:
                    view_visualizza_operatore = [[sg.Text('Codice fiscale: '),sg.Text(operatore.get_codice_fiscale())],
                                                 [sg.Text('Nome: '),sg.Text(operatore.get_nome())],
                                                 [sg.Text('Cognome: '),sg.Text(operatore.get_cognome())],
                                                 [sg.Text('Email: '),sg.Text(operatore.get_email())],
                                                 [sg.Text('Telefono: '),sg.Text(operatore.get_telefono())]]

                else:
                    view_visualizza_operatore = [[sg.Text('Operatore non trovato')]]
                window_visualizza_operatore = sg.Window('Visualizza operatore', view_visualizza_operatore)
                window_ricerca_operatore.close()
                while True:
                    event5, values5 = window_visualizza_operatore.read()
                    if event5 == sg.WINDOW_CLOSED:
                        break



    elif event == 'Modifica un operatore':
        window_ricerca_operatore = sg.Window('Ricerca operatore', view_ricerca_operatore)

        while True:
            event4, values4 = window_ricerca_operatore.read()
            if event4 == sg.WINDOW_CLOSED or event4 == "Chiudi":
                break
            elif event4=='Cerca':
                operatore = Operatore.Operatore.ricerca_operatore(str(values4['codiceFiscale']))
                if operatore:
                    modificaOperatore = [
                        [sg.Text('Nome'), sg.Input(default_text=operatore.get_nome(),key='nome')],
                        [sg.Text('Cognome'), sg.Input(default_text=operatore.get_cognome(),key='cognome')],
                        [sg.Text('email'), sg.Input(default_text=operatore.get_email(),key='email')],
                        [sg.Text('Telefono'), sg.Input(default_text=operatore.get_telefono(),key='telefono')],
                        [sg.Button('Invia')]]
                else:
                    modificaOperatore = [[sg.Text('Operatore non trovato')]]
                window_modifica_operatore = sg.Window('Modifica operatore', modificaOperatore)
                window_ricerca_operatore.close()
                while True:
                    event6, values6 = window_modifica_operatore.read()
                    if event6 == sg.WINDOW_CLOSED:
                        break
                    elif event6 == 'Invia':
                        Operatore.Operatore.modifica_operatore(operatore,values6)
                        window_modifica_operatore.close()




    elif event == 'Elimina un operatore':
        window_ricerca_operatore = sg.Window('Ricerca operatore', view_ricerca_operatore)

        while True:
            event7, values7 = window_ricerca_operatore.read()
            if event7 == sg.WINDOW_CLOSED or event7 == "Chiudi":
                break
            elif event7 == 'Cerca':
                operatore = Operatore.Operatore.ricerca_operatore(str(values7['codiceFiscale']))
                window_ricerca_operatore.close()
                if operatore:
                    Operatore.Operatore.elimina_operatore(operatore)
                    view_operatore_eliminato = [[sg.Text('Operatore eliminato')]]
                else:
                    view_operatore_eliminato = [[sg.Text('Operatore non trovato')]]
                window_elimina_operatore = sg.Window('Elimina operatore',view_operatore_eliminato)
                while True:
                    event8, values8 = window_elimina_operatore.read()
                    if event8 == sg.WINDOW_CLOSED:
                        break





window_gestione_operatore.close()








