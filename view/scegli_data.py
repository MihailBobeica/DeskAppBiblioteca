
from datetime import datetime, timedelta

from PySide6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QCalendarWidget, QComboBox, QMessageBox, QTimeEdit
from PySide6.QtCore import QDate, Qt, QTime
from abstract.view import View
from controller.gestione_prenotazione_posto import PrenotazioneController
from view.scegli_aula import ScegliAulaView

class ScegliDataView(View):
    def __init__(self, tipo_prenotazione):
        super().__init__()
        self.tipo_prenotazione = tipo_prenotazione
        self.data_selezionata = None
        self.durata = None

    def create_layout(self):
        layout = QVBoxLayout(self)

        label_data = QLabel("Scegli la data:")
        layout.addWidget(label_data)

        self.calendar_widget = QCalendarWidget()
        current_time = QTime.currentTime()
        if current_time > QTime(18, 15):
            next_day = QDate.currentDate().addDays(1)
            self.calendar_widget.setDateRange(next_day, QDate(2099, 12, 31))
            self.calendar_widget.setSelectedDate(next_day)
            self.selected_date_label = QLabel("Data selezionata: " + next_day.toString("dd/MM/yyyy"))
        else:
            self.calendar_widget.setDateRange(QDate.currentDate(), QDate(2099, 12, 31))
            self.calendar_widget.setSelectedDate(QDate.currentDate())
            self.selected_date_label = QLabel("Data selezionata: " + QDate.currentDate().toString("dd/MM/yyyy"))

        self.calendar_widget.setFixedSize(250, 250)
        self.calendar_widget.setFirstDayOfWeek(Qt.Monday)
        self.calendar_widget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar_widget.setNavigationBarVisible(True)

        layout.addWidget(self.calendar_widget)
        layout.addWidget(self.selected_date_label)

        label_ora = QLabel("Ora di inizio:")
        layout.addWidget(label_ora)

        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("HH:mm")
        self.time_edit.setTimeRange(QTime(8, 30), QTime(18, 45))

        if QDate.currentDate() == self.calendar_widget.selectedDate() and current_time < QTime(18, 15):
            self.time_edit.setTime(current_time)
        else:
            self.time_edit.setTime(QTime(8, 30))

        layout.addWidget(self.time_edit)

        label_durata = QLabel("Scegli la durata:")
        layout.addWidget(label_durata)

        self.combo_durata = QComboBox()
        self.combo_durata.addItems(["1 ora", "2 ore", "3 ore", "4 ore", "5 ore", "6 ore", "7 ore", "8 ore",
                                    "9 ore"])  # Opzioni fisse per la durata
        layout.addWidget(self.combo_durata)

        submit_button = QPushButton("Avanti")
        layout.addWidget(submit_button)

        submit_button.clicked.connect(self.on_submit_clicked)
        self.calendar_widget.clicked.connect(self.on_calendar_clicked)
        self.calendar_widget.clicked.connect(self.update_time_edit)

    def on_calendar_clicked(self, date):
        selected_date = date.toString("dd/MM/yyyy")
        self.selected_date_label.setText("Data selezionata: " + selected_date)

    def update_time_edit(self, date):
        current_time = QTime.currentTime()
        if date == QDate.currentDate() and current_time < QTime(18, 15):
            self.time_edit.setTime(current_time)
        else:
            self.time_edit.setTime(QTime(8, 30))

        if current_time > QTime(18, 15):
            self.calendar_widget.setMinimumDate(QDate.currentDate().addDays(1))
        else:
            self.calendar_widget.setMinimumDate(QDate.currentDate())

    def on_submit_clicked(self):
        selected_date = self.calendar_widget.selectedDate()
        selected_time = self.time_edit.time()

        data = selected_date.toString("yyyy-MM-dd")
        ora = selected_time.toString("HH:mm")

        durata = self.combo_durata.currentText().split(" ")[0]  # Estrai solo la parte numerica della durata

        self.data_selezionata = f"{data} {ora}"
        self.durata = durata

        if self.data_selezionata and self.durata:
            # Verifica se la data selezionata è una domenica
            if datetime.strptime(data, "%Y-%m-%d").weekday() == 6:
                QMessageBox.warning(self, "Attenzione", "Non puoi scegliere una domenica.")
            else:
                # Converti la data selezionata in un oggetto datetime
                data_selezionata = datetime.strptime(self.data_selezionata, "%Y-%m-%d %H:%M")

                # Converti la durata in un numero intero rappresentante le ore e moltiplicala per 60 per ottenere i minuti
                durata_ore = int(self.durata)
                durata_minuti = durata_ore * 60

                # Calcola ora_inizio e ora_fine in base alla data selezionata e alla durata
                ora_inizio = data_selezionata
                ora_fine = data_selezionata + timedelta(minutes=durata_minuti)

                if ora_fine > datetime.strptime(f"{data} 19:15", "%Y-%m-%d %H:%M"):
                    QMessageBox.warning(self, "Attenzione", "Dovresti scegliere una durata inferiore!")
                else:
                    prenotazione_controller = PrenotazioneController()
                    utente_id = prenotazione_controller.get_username_utente_loggato()

                    # Verifica se l'utente loggato ha già una prenotazione
                    has_prenotazione = prenotazione_controller.has_prenotazione_in_fascia_oraria(utente_id,
                                                                                                 data_selezionata,
                                                                                                 ora_inizio, ora_fine)

                    if has_prenotazione:
                        QMessageBox.warning(self, "Attenzione",
                                            "Hai già una prenotazione per questa fascia oraria e data.")
                    else:
                        scegli_aula_view = ScegliAulaView(self.tipo_prenotazione, self.data_selezionata, self.durata)
                        self.main_window.set_view(scegli_aula_view)