import pickle
class Operatore:

    def __init__(self,codiceFiscale,nome,cognome,email,telefono):
        self.codiceFiscale = codiceFiscale
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.telefono = telefono

    def get_codice_fiscale(self):
        return self.codiceFiscale

    def set_nome(self, nuovo_nome):
        self.nome = nuovo_nome

    def get_nome(self):
        return self.nome

    def set_cognome(self, nuovo_cognome):
        self.cognome = nuovo_cognome

    def get_cognome(self):
        return self.cognome

    def set_email(self, nuova_email):
        self.email = nuova_email

    def get_email(self):
        return self.email

    def set_telefono(self, nuovo_telefono):
        self.telefono = nuovo_telefono

    def get_telefono(self):
        return self.telefono

    def stampa(self):
        print(self.codiceFiscale+' '+self.nome+' '+self.cognome+' '+self.email+' '+self.telefono)

    def inserisci_operatore(data):
        with open('Operatori.pickle', 'ab') as file:
            pickle.dump(data, file)




    def ricerca_operatore(cf):
        try:
            with open('Operatori.pickle', 'rb') as f:
                while True:
                    try:
                        data = pickle.load(f)
                        if data.get_codice_fiscale() == cf:
                            return data
                    except EOFError:
                        break
        except FileNotFoundError:
            print("Il file specificato non esiste.")
        except Exception as e:
            print(f"Si è verificato un errore: {str(e)}")

        return None

    def modifica_operatore(operatore, new_data):
        with open('Operatori.pickle', 'rb') as f:
            objects = []
            while True:
                try:
                    obj = pickle.load(f)
                    if obj.get_codice_fiscale() == operatore.get_codice_fiscale():
                        obj.set_nome(new_data['nome'])
                        obj.set_cognome(new_data['cognome'])
                        obj.set_email(new_data['email'])
                        obj.set_telefono(new_data['telefono'])
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
                    if obj.get_codice_fiscale() == operatore.codiceFiscale:
                        pass
                    else:
                        objects.append(obj)
                except EOFError:
                    break

        with open('Operatori.pickle', 'wb') as f:
            for obj in objects:
                pickle.dump(obj, f)















