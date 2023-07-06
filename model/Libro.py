class Libro:
    def __init__(self,autore,ISBN,quantità,titolo,genere):
        self.autore = autore
        self.ISBN = ISBN
        self.quantità = quantità
        self.titolo = titolo
        self.genere = genere

        # Getter per la proprietà 'autore'
        def get_autore(self):
            return self._autore

        # Setter per la proprietà 'autore'
        def set_autore(self, autore):
            self._autore = autore

        # Getter per la proprietà 'ISBN'
        def get_ISBN(self):
            return self._ISBN

        # Setter per la proprietà 'ISBN'
        def set_ISBN(self, ISBN):
            self._ISBN = ISBN

        # Getter per la proprietà 'quantità'
        def get_quantità(self):
            return self._quantità

        # Setter per la proprietà 'quantità'
        def set_quantità(self, quantità):
            self._quantità = quantità

        # Getter per la proprietà 'titolo'
        def get_titolo(self):
            return self._titolo

        # Setter per la proprietà 'titolo'
        def set_titolo(self, titolo):
            self._titolo = titolo

        # Getter per la proprietà 'genere'
        def get_genere(self):
            return self._genere

        # Setter per la proprietà 'genere'
        def set_genere(self, genere):
            self._genere = genere

    def stampa(self):
        print(self.autore+' '+self.ISBN+' '+self.quantità+' '+self.titolo+' '+self.genere)