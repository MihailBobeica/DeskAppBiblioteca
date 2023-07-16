import PySimpleGUI as sg


class gestioneOperatoreView:

    def view_errore(text):
        view_errore = [[sg.Text(text)]]
        window_errore = sg.Window('Errore', view_errore)
        while True:
            event, values = window_errore.read()
            if event == sg.WINDOW_CLOSED:
                break

        window_errore.close()



    def view_gestione_operatore():
        view_gestione_operatore = [[sg.LabeledButton('Inserisci un nuovo operatore')],
                                   [sg.LabeledButton('Visualizza un operatore')],
                                   [sg.LabeledButton('Modifica un operatore')],
                                   [sg.LabeledButton('Elimina un operatore')]]
        window_gestione_operatore = sg.Window('Gestione operatore', view_gestione_operatore)
        return window_gestione_operatore.read()

    def view_ricerca_operatore():
        view_ricerca_operatore = [[sg.Text('Codice fiscale'), sg.Input(key='codiceFiscale')], [sg.LabeledButton('Cerca')]]
        window_ricerca_operatore = sg.Window('Ricerca operatore', view_ricerca_operatore)
        while True:
            event, values = window_ricerca_operatore.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Cerca':
                if values['codiceFiscale'] == None or values['codiceFiscale'] == '':
                    gestioneOperatoreView.view_errore()
                break

        window_ricerca_operatore.close()
        return event,values



    def view_inserisci_operatore(value):
        view_inserisci_operatore = [
            [sg.Text('Codice fiscale'), sg.Input(str(value[1]['codiceFiscale']), key='codiceFiscale', readonly=True)],
            [sg.Text('Nome'), sg.Input(key='nome')],
            [sg.Text('Cognome'), sg.Input(key='cognome')],
            [sg.Text('email'), sg.Input(key='email')],
            [sg.Text('Telefono'), sg.Input(key='telefono')],
            [sg.LabeledButton('Invia')]]
        window_inserisci_operatore = sg.Window('Inserisci operatore', view_inserisci_operatore)
        while True:
            event, values = window_inserisci_operatore.read()
            if event == sg.WINDOW_CLOSED or event == 'Invia':
                break
        window_inserisci_operatore.close()
        return event, values

    def view_visualizza_operatore(operatore):
        view_visualizza_operatore = [
            [sg.Text('Codice fiscale: '), sg.Text(operatore['codiceFiscale'])],
            [sg.Text('Nome: '), sg.Text(operatore['nome'])],
            [sg.Text('Cognome: '), sg.Text(operatore['cognome'])],
            [sg.Text('Email: '), sg.Text(operatore['email'])],
            [sg.Text('Telefono: '), sg.Text(operatore['telefono'])]]

        window_visualizza_operatore = sg.Window('Visualizza operatore',view_visualizza_operatore)
        while True:
            event, values = window_visualizza_operatore.read()
            if event == sg.WINDOW_CLOSED:
                break
        window_visualizza_operatore.close()
        return event, values

    def view_modifica_operatore(operatore):
        view_modifica_operatore = [
            [sg.Text('Nome'), sg.Input(default_text=operatore['nome'], key='nome')],
            [sg.Text('Cognome'), sg.Input(default_text=operatore['cognome'], key='cognome')],
            [sg.Text('email'), sg.Input(default_text=operatore['email'], key='email')],
            [sg.Text('Telefono'), sg.Input(default_text=operatore['telefono'], key='telefono')],
            [sg.LabeledButton('Invia')]]
        window_modifica_operatore = sg.Window('Modifica operatore',view_modifica_operatore)
        while True:
            event, values = window_modifica_operatore.read()
            if event == sg.WINDOW_CLOSED or event == 'Invia':
                break
        window_modifica_operatore.close()
        return event, values















