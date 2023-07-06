
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

















