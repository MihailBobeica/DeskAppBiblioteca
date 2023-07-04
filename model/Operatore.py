import pickle
class Operatore:

    def __init__(self,codiceFiscale,nome,cognome,email,telefono):
        self.codiceFiscale = codiceFiscale
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.telefono = telefono

    def stampa(self):
        print(self.codiceFiscale+self.nome+self.cognome+self.email+self.telefono)

    def inserisci_operatore(data):
        with open('Operatori.pickle', 'ab') as file:
            pickle.dump(data, file)




    def ricerca_operatore(operatore):
        with open('Operatori.pickle', 'rb') as f:
            try:
                while True:
                    data = pickle.load(f)

                    if (operatore['codiceFiscale'] == data['codiceFiscale']):
                        return data
            except EOFError:
                pass

        return None









