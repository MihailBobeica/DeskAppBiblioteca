import pickle

class GestionePrenotazionePosto:
    @staticmethod
    def inserisci_prenotazione_posto(data):
        with open('prenotazioni_posto.pkl', 'ab') as file:
            pickle.dump(data, file)

    @staticmethod
    def inserisci_prenotazione_aula(data):
        with open('prenotazioni_aula.pkl', 'ab') as file:
            pickle.dump(data, file)

    @staticmethod
    def ricerca_prenotazione_posto(ID):
        try:
            with open('prenotazioni_posto.pkl', 'rb') as f:
                while True:
                    try:
                        data = pickle.load(f)
                        if data.get_ID() == ID:
                            return data
                    except EOFError:
                        break
        except FileNotFoundError:
            print("Il file specificato non esiste.")
        except Exception as e:
            print(f"Si è verificato un errore: {str(e)}")

        return None

    @staticmethod
    def ricerca_prenotazione_aula(ID):
        try:
            with open('prenotazioni_aula.pkl', 'rb') as f:
                while True:
                    try:
                        data = pickle.load(f)
                        if data.get_ID() == ID:
                            return data
                    except EOFError:
                        break
        except FileNotFoundError:
            print("Il file specificato non esiste.")
        except Exception as e:
            print(f"Si è verificato un errore: {str(e)}")

        return None

    @staticmethod
    def modifica_prenotazione_posto(prenotazione, new_data):
        with open('prenotazioni_posto.pkl', 'rb') as f:
            objects = []
            while True:
                try:
                    obj = pickle.load(f)
                    if obj.get_ID() == prenotazione.get_ID():
                        obj.set_data_prenotazione(new_data['data_prenotazione'])
                        obj.set_data_effettuazione(new_data['data_effettuazione'])
                        obj.set_ora_inizio(new_data['ora_inizio'])
                        obj.set_ora_fine(new_data['ora_fine'])
                        obj.set_disponibilita(new_data['disponibilita'])
                        obj.set_codice_posto(new_data['codice_posto'])
                    objects.append(obj)
                except EOFError:
                    break

        with open('prenotazioni_posto.pkl', 'wb') as f:
            for obj in objects:
                pickle.dump(obj, f)

    @staticmethod
    def modifica_prenotazione_aula(prenotazione, new_data):
        with open('prenotazioni_aula.pkl', 'rb') as f:
            objects = []
            while True:
                try:
                    obj = pickle.load(f)
                    if obj.get_ID() == prenotazione.get_ID():
                        obj.set_data_prenotazione(new_data['data_prenotazione'])
                        obj.set_data_effettuazione(new_data['data_effettuazione'])
                        obj.set_ora_inizio(new_data['ora_inizio'])
                        obj.set_ora_fine(new_data['ora_fine'])
                        obj.set_ora_attivazione(new_data['ora_attivazione'])
                        obj.set_disponibilita(new_data['disponibilita'])
                        obj.set_codice_aula(new_data['codice_aula'])
                    objects.append(obj)
                except EOFError:
                    break

        with open('prenotazioni_aula.pkl', 'wb') as f:
            for obj in objects:
                pickle.dump(obj, f)

    @staticmethod
    def elimina_prenotazione_posto(prenotazione):
        with open('prenotazioni_posto.pkl', 'rb') as f:
            objects = []
            while True:
                try:
                    obj = pickle.load(f)
                    if obj.get_ID() == prenotazione.get_ID():
                        pass
                    else:
                        objects.append(obj)
                except EOFError:
                    break

        with open('prenotazioni_posto.pkl', 'wb') as f:
            for obj in objects:
                pickle.dump(obj, f)

    @staticmethod
    def elimina_prenotazione_aula(prenotazione):
        with open('prenotazioni_aula.pkl', 'rb') as f:
            objects = []
            while True:
                try:
                    obj = pickle.load(f)
                    if obj.get_ID() == prenotazione.get_ID():
                        pass
                    else:
                        objects.append(obj)
                except EOFError:
                    break

        with open('prenotazioni_aula.pkl', 'wb') as f:
            for obj in objects:
                pickle.dump(obj, f)
