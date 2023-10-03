from typing import Optional

from sqlalchemy import or_

from abstract import Model
from database import Session, Operatore
from utils.auth import hash_password


class ModelOperatori(Model):
    def inserisci(self, **kwargs):
        pass

    def __init__(self):
        super().__init__()

    def aggiungi(self,
                 username: str,
                 nome: str,
                 cognome: str,
                 password: str):
        db_session = Session()
        operatore = Operatore(username=username,
                              nome=nome,
                              cognome=cognome,
                              password=hash_password(password))
        db_session.add(operatore)
        db_session.commit()
        db_session.close()

    def by_text(self, text: str) -> list[Operatore]:
        db_session = Session()
        operatori = db_session.query(Operatore).filter(
            or_(Operatore.username.ilike(f"%{text}%"),
                Operatore.nome.ilike(f"%{text}%"),
                Operatore.cognome.ilike(f"%{text}%"))
        ).all()
        db_session.close()
        return operatori

    def by_id(self, id_operatore: int) -> Operatore:
        db_session = Session()
        operatore = db_session.query(Operatore).get(id_operatore)
        db_session.close()
        return operatore

    def elimina(self, id_operatore: int):
        db_session = Session()
        operatore = db_session.query(Operatore).get(id_operatore)
        db_session.delete(operatore)
        db_session.commit()
        db_session.close()

    def modifica(self,
                 id_operatore: int,
                 nome: str,
                 cognome: str,
                 password: Optional[str]):
        db_session = Session()
        operatore: Operatore = db_session.query(Operatore).get(id_operatore)
        operatore.nome = nome
        operatore.cognome = cognome
        if password:
            operatore.password = hash_password(password)
        db_session.merge(operatore)
        db_session.commit()
        db_session.close()
