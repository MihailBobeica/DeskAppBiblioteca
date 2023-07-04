import PySimpleGUI as sg
from model import Operatore
from controller import gestioneOperatore

view_gestione_operatore = [[sg.Button('Inserisci un nuovo operatore')],
                     [sg.Button('Visualizza un operatore')],
                     [sg.Button('Modifica un operatore')],
                     [sg.Button('Elimina un operatore')]]

view_ricerca_operatore = [[sg.Text('Codice fiscale'), sg.Input(key='codiceFiscale')],[sg.Button('Invia')]]


window_gestione_operatore = sg.Window('Gestione operatore', view_gestione_operatore)

while True:
    event, values = window_gestione_operatore.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Inserisci un nuovo operatore':
        inserisciOperatore = [[sg.Text('Codice fiscale'), sg.Input(key='codiceFiscale')],
                              [sg.Text('Nome'), sg.Input(key='nome')],
                              [sg.Text('Cognome'), sg.Input(key='cognome')],
                              [sg.Text('email'), sg.Input(key='email')],
                              [sg.Text('Telefono'), sg.Input(key='telefono')],
                              [sg.Button('Invia')]]
        window_inserisci_operatore = sg.Window('Inserisci operatore', inserisciOperatore)
        while True:
            event2, values2 = window_inserisci_operatore.read()
            if event2 == sg.WINDOW_CLOSED or event2 == "Chiudi":
                break
            elif event2 == 'Invia':
                Operatore.Operatore.inserisci_operatore(values2)

        window_inserisci_operatore.close()

    elif event == 'Visualizza un operatore':
        window_ricerca_operatore = sg.Window('Ricerca operatore', view_ricerca_operatore)
        while True:
            event3, values3 = window_ricerca_operatore.read()
            if event3 == sg.WINDOW_CLOSED or event3 == "Chiudi":
                break
            elif event3 == 'Invia':
                operatore = Operatore.Operatore.ricerca_operatore(values3)

                view_visualizza_operatore = [[sg.Text(operatore['codiceFiscale'])],
                                             [sg.Text(operatore['nome'])],
                                             [sg.Text(operatore['cognome'])],
                                             [sg.Text(operatore['email'])],
                                             [sg.Text(operatore['telefono'])]]
                window_visualizza_operatore = sg.Window('Visualizza operatore', view_visualizza_operatore)




window_gestione_operatore.close()



