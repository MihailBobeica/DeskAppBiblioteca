import os
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Utente

class TestDatabase(unittest.TestCase):

    def setUp(self):
        print(os.getcwd())
        exit()
        self.db_engine = create_engine('sqlite:///../database/db.sqlite')
        Session = sessionmaker(bind=self.db_engine)
        self.db_session = Session()

        # Crea le tabelle nel database
        Base.metadata.create_all(self.db_engine)

    def tearDown(self):
        # Pulisci il database dopo ogni test
        self.db_session.close()
        Base.metadata.drop_all(self.db_engine)

    def test_creazione_utente(self):
        # Crea un nuovo utente
        user = Utente(nome='Nome', cognome='Cognome', ruolo='utente_generico', username='username', password='password')
        self.db_session.add(user)
        self.db_session.commit()


        retrieved_user = self.db_session.query(Utente).filter_by(username='username').first()


        self.assertIsNotNone(retrieved_user)
        self.assertEqual('Nome', retrieved_user.nome)
        self.assertEqual('Cognome', retrieved_user.cognome)
        self.assertEqual('utente_generico', retrieved_user.ruolo)
        self.assertEqual('username', retrieved_user.username)
        self.assertEqual('password', retrieved_user.password)

    def test_recupero_utente_inesistente(self):
        # Cerca un utente che non dovrebbe esistere nel database
        retrieved_user = self.db_session.query(Utente).filter_by(username='nonexistentuser').first()

        # Assicurati che l'utente non sia stato trovato
        self.assertIsNone(retrieved_user)

    '''def test(self):
        x="4"
        self.assertEqual(x,"4")'''

if __name__ == '__main__':
    unittest.main()





