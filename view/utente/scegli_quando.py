from datetime import datetime, time, timedelta
from typing import Optional

from PySide6.QtCore import QTime, QDate
from PySide6.QtWidgets import QVBoxLayout, QLabel, QCalendarWidget, QTimeEdit, QComboBox, QPushButton, QMessageBox

from abstract import View


class ScegliQuandoView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)

        q_current_date = QDate.currentDate()
        q_next_day = q_current_date.addDays(1)
        q_current_time = QTime.currentTime()

        self.combo_box.setFixedWidth(500)

        self.combo_box.currentTextChanged.connect(self.durata_changed)

        self.time_edit.setFixedWidth(500)
        self.time_edit.setDisplayFormat("HH:mm")
        self.time_edit.setTimeRange(QTime(8, 30), QTime(18, 15))
        self.time_edit.setTime(q_current_time)

        self.calendar.selectionChanged.connect(self.date_changed)

        if q_current_time > QTime(18, 15):  # se siamo prossimi all'orario di chiusura
            self.calendar.setMinimumDate(q_next_day)
            self.calendar.setSelectedDate(q_next_day)
            self.time_edit.setTime(QTime(8, 30))
        else:
            self.calendar.setMinimumDate(q_current_date)
            self.calendar.setSelectedDate(q_current_date)
        self.date_changed()
        self.time_changed(self.time_edit.time())

        self.time_edit.timeChanged.connect(self.time_changed)

        label_data = QLabel("Scegli giorno:")
        label_ora_inizio = QLabel("Scegli ora inizio:")
        label_durata = QLabel("Scegli durata:")
        button_submit = QPushButton("Avanti")
        button_submit.setFixedWidth(200)
        button_submit.clicked.connect(self.invia)

        layout.addWidget(label_data)
        layout.addWidget(self.calendar)
        layout.addWidget(self.label_giorno)
        layout.addWidget(label_ora_inizio)
        layout.addWidget(self.time_edit)
        layout.addWidget(label_durata)
        layout.addWidget(self.combo_box)
        layout.addWidget(button_submit)

    def __init__(self, metodo: str):
        self.metodo = metodo
        self.data_prenotazione: Optional[datetime] = None
        self.ora_inizio: Optional[datetime] = None
        self.durata = 1

        self.calendar = QCalendarWidget()
        self.time_edit = QTimeEdit()
        self.combo_box = QComboBox()
        self.label_giorno = QLabel()
        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_posti
        self.attach(controller_posti)

    def date_changed(self):
        q_data_selezionata = self.calendar.selectedDate()
        q_giorno_successivo = q_data_selezionata.addDays(1)

        data_selezionata: datetime = q_data_selezionata.toPython()
        if data_selezionata.weekday() == 6:  # impedire che venga selezionata una domenica
            QMessageBox.warning(self,
                                "Attenzione",
                                "Non puoi scegliere una domenica.")
            self.calendar.setSelectedDate(q_giorno_successivo)

        data_selezionata: datetime = self.calendar.selectedDate().toPython()
        self.data_prenotazione = data_selezionata
        self.label_giorno.setText(f"Giorno selezionato: {data_selezionata.strftime('%d %B %Y')}")

        self.update_ora_inizio()

    def update_ora_inizio(self):
        data_selezionata: datetime = self.calendar.selectedDate().toPython()
        time_ora_inizio: time = self.time_edit.time().toPython()
        self.ora_inizio = datetime(hour=time_ora_inizio.hour,
                                   minute=time_ora_inizio.minute,
                                   day=data_selezionata.day,
                                   month=data_selezionata.month,
                                   year=data_selezionata.year)

    def time_changed(self, q_time: QTime):
        time_ora_inizio: time = q_time.toPython()

        # update box durata
        timedelta_ora_inizio = timedelta(hours=time_ora_inizio.hour,
                                         minutes=time_ora_inizio.minute)
        timedelta_ora_limite = timedelta(hours=19,
                                         minutes=15)
        ore_rimanenti = int((timedelta_ora_limite - timedelta_ora_inizio).total_seconds() / 3600)

        self.combo_box.clear()
        self.combo_box.addItems(["1 ora"] + [f"{i} ore" for i in range(2, ore_rimanenti + 1)])

        self.update_ora_inizio()

    def durata_changed(self, text: str):
        if text:
            self.durata = int(text.split()[0])
        else:
            self.durata = 1

    def invia(self):
        ora_fine = self.ora_inizio + timedelta(hours=self.durata)
        self.notify("scegli_aula",
                    data={"metodo": self.metodo,
                          "ora_inizio": self.ora_inizio,
                          "ora_fine": ora_fine})
