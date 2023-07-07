import pickle
import PySimpleGUI as sg
from view import gestioneOperatore


def inserisci_operatore(data):
    with open('Operatori.pickle', 'ab') as file:
        pickle.dump(data, file)


def ricerca_operatore(cf):
    try:
        with open('Operatori.pickle', 'rb') as f:
            while True:
                try:
                    data = pickle.load(f)
                    if data['codiceFiscale'] == cf:
                        return data
                except EOFError:
                    break
    except FileNotFoundError:
        print("Il file specificato non esiste.")
    except Exception as e:
        print(f"Si è verificato un errore: {str(e)}")

    return None

#da rivedere
def modifica_operatore(operatore, new_data):
    with open('Operatori.pickle', 'rb') as f:
        objects = []
        while True:
            try:
                obj = pickle.load(f)
                if obj['codiceFiscale'] == operatore['codiceFiscale']:
                    obj['nome']=new_data['nome']
                    obj['cognome']=new_data['cognome']
                    obj['email'] = new_data['email']
                    obj['telefono'] = new_data['telefono']
                objects.append(obj)
            except EOFError:
                break

    with open('Operatori.pickle', 'wb') as f:
        for obj in objects:
            pickle.dump(obj, f)


def elimina_operatore(operatore):
    with open('Operatori.pickle', 'rb') as f:
        objects = []
        while True:
            try:
                obj = pickle.load(f)
                if obj['codiceFiscale'] == operatore['codiceFiscale']:
                    pass
                else:
                    objects.append(obj)
            except EOFError:
                break

    with open('Operatori.pickle', 'wb') as f:
        for obj in objects:
            pickle.dump(obj, f)



def gestione_operatore():
    while True:
        event, values = gestioneOperatore.gestioneOperatoreView.view_gestione_operatore()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'Inserisci un nuovo operatore':
            value = gestioneOperatore.gestioneOperatoreView.view_ricerca_operatore()
            operatore = ricerca_operatore(str(value[1]['codiceFiscale']))
            if operatore:
                gestioneOperatore.gestioneOperatoreView.view_errore('Operatore già inserito')
            else:
                data = gestioneOperatore.gestioneOperatoreView.view_inserisci_operatore(value)
                inserisci_operatore(data[1])

        elif event == 'Visualizza un operatore':
            value = gestioneOperatore.gestioneOperatoreView.view_ricerca_operatore()
            operatore = ricerca_operatore(str(value[1]['codiceFiscale']))
            if operatore:
                gestioneOperatore.gestioneOperatoreView.view_visualizza_operatore(operatore)
            else:
                gestioneOperatore.gestioneOperatoreView.view_errore('Operatore non trovato')

        elif event == 'Modifica un operatore':
            value = gestioneOperatore.gestioneOperatoreView.view_ricerca_operatore()
            operatore = ricerca_operatore(str(value[1]['codiceFiscale']))
            if operatore:
                value = gestioneOperatore.gestioneOperatoreView.view_modifica_operatore(operatore)
                if value[0] == 'Invia':
                    modifica_operatore(operatore,value[1])
            else:
                gestioneOperatore.gestioneOperatoreView.view_errore('Operatore non trovato')

        elif event == 'Elimina un operatore':
            value = gestioneOperatore.gestioneOperatoreView.view_ricerca_operatore()
            operatore = ricerca_operatore(str(value[1]['codiceFiscale']))
            if operatore:
                gestioneOperatore.gestioneOperatoreView.view_errore('Operatore eliminato')
                elimina_operatore(operatore)
            else:
                gestioneOperatore.gestioneOperatoreView.view_errore('Operatore non trovato')



gestione_operatore()







