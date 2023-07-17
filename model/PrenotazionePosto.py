class PrenotazionePosto:
    def __init__(self, data_prenotazione, ID, data_effettuazione, ora_inizio, ora_fine, ora_attivazione, disponibilita, codice_posto):
        self.data_prenotazione = data_prenotazione
        self.ID = ID
        self.data_effettuazione = data_effettuazione
        self.ora_inizio = ora_inizio
        self.ora_fine = ora_fine
        self.ora_attivazione = ora_attivazione
        self.disponibilita = disponibilita
        self.codice_posto = codice_posto

    # Getter per la proprietà 'data_prenotazione'
    def get_data_prenotazione(self):
        return self.data_prenotazione

    # Setter per la proprietà 'data_prenotazione'
    def set_data_prenotazione(self, data_prenotazione):
        self.data_prenotazione = data_prenotazione

    # Getter per la proprietà 'ID'
    def get_ID(self):
        return self.ID

    # Setter per la proprietà 'ID'
    def set_ID(self, ID):
        self.ID = ID

    # Getter per la proprietà 'data_effettuazione'
    def get_data_effettuazione(self):
        return self.data_effettuazione

    # Setter per la proprietà 'data_effettuazione'
    def set_data_effettuazione(self, data_effettuazione):
        self.data_effettuazione = data_effettuazione

    # Getter per la proprietà 'ora_inizio'
    def get_ora_inizio(self):
        return self.ora_inizio

    # Setter per la proprietà 'ora_inizio'
    def set_ora_inizio(self, ora_inizio):
        self.ora_inizio = ora_inizio

    # Getter per la proprietà 'ora_fine'
    def get_ora_fine(self):
        return self.ora_fine

    # Setter per la proprietà 'ora_fine'
    def set_ora_fine(self, ora_fine):
        self.ora_fine = ora_fine

    # Getter per la proprietà 'ora_attivazione'
    def get_ora_attivazione(self):
        return self.ora_attivazione

    # Setter per la proprietà 'ora_attivazione'
    def set_ora_attivazione(self, ora_attivazione):
        self.ora_attivazione = ora_attivazione

    # Getter per la proprietà 'disponibilita'
    def get_disponibilita(self):
        return self.disponibilita

    # Setter per la proprietà 'disponibilita'
    def set_disponibilita(self, disponibilita):
        self.disponibilita = disponibilita

    # Getter per la proprietà 'codice_aula'
    def get_codice_posto(self):
        return self.codice_posto

    # Setter per la proprietà 'codice_posto'
    def set_codice_aula(self, codice_posto):
        self.codice_posto = codice_posto

    def stampa(self):
        print(self.data_prenotazione, self.ID, self.data_effettuazione, self.ora_inizio, self.ora_fine, self.ora_attivazione, self.disponibilita, self.codice_posto)
