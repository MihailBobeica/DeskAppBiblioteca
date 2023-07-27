from PySide6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QCalendarWidget, QComboBox, QMessageBox, QTimeEdit, QSizePolicy
from PySide6.QtCore import QDate, Qt, QTime
from abstract.view import View
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
        self.calendar_widget.setMinimumDate(QDate.currentDate())  # Impedisce di selezionare date precedenti alla data odierna
        self.calendar_widget.setMaximumDate(QDate(2099, 12, 31))
        self.calendar_widget.setFixedSize(200, 200)

        # Imposta il primo giorno della settimana su lunedì
        self.calendar_widget.setFirstDayOfWeek(Qt.Monday)

        # Nascondi la colonna delle settimane (ultima colonna)
        self.calendar_widget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar_widget.setNavigationBarVisible(False)

        layout.addWidget(self.calendar_widget)

        self.selected_date_label = QLabel("Data selezionata: ")
        layout.addWidget(self.selected_date_label)

        label_ora = QLabel("Ora di inizio:")
        layout.addWidget(label_ora)

        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("HH:mm")  # Imposta il formato dell'ora a 24 ore
        self.time_edit.setTimeRange(QTime(8, 30), QTime(18, 45))  # Imposta il range di ore consentite
        layout.addWidget(self.time_edit)

        label_durata = QLabel("Scegli la durata:")
        layout.addWidget(label_durata)

        self.combo_durata = QComboBox()
        self.update_durata_options()  # Aggiorna le opzioni della tendina inizialmente
        layout.addWidget(self.combo_durata)

        submit_button = QPushButton("Avanti")
        layout.addWidget(submit_button)

        submit_button.clicked.connect(self.on_submit_clicked)
        self.calendar_widget.clicked.connect(self.on_calendar_clicked)

    def update_durata_options(self):
        # Aggiorna le opzioni della tendina "durata" in base all'ora attuale e l'orario di chiusura consentito
        current_time = QTime.currentTime()
        max_time = QTime(18, 45)

        if self.calendar_widget.selectedDate() == QDate.currentDate():
            # Se la data selezionata è oggi, imposta le durate ammissibili tra l'ora attuale e l'orario di chiusura consentito
            self.time_edit.setTime(current_time)
            self.time_edit.setEnabled(True)
            durate_ammissibili = [f"{current_time.addSecs(i * 1800).toString('HH:mm')} ({i + 1} ore)" for i in
                                  range(current_time.secsTo(max_time) // 1800)]
        else:
            # Altrimenti, imposta le durate ammissibili tra le 8:30 e l'orario di chiusura consentito
            self.time_edit.setTime(QTime(8, 30))
            self.time_edit.setEnabled(True)
            durate_ammissibili = [f"{QTime(8, 30).addSecs(i * 1800).toString('HH:mm')} ({i + 1} ore)" for i in
                                  range(QTime(8, 30).secsTo(max_time) // 1800)]

        self.combo_durata.clear()
        self.combo_durata.addItems(durate_ammissibili)

    def on_calendar_clicked(self, date):
        # Aggiorna il QLabel con la data selezionata dall'utente
        selected_date = date.toString("dd/MM/yyyy")
        self.selected_date_label.setText("Data selezionata: " + selected_date)

        self.update_durata_options()  # Aggiorna le opzioni della tendina quando viene selezionata una nuova data

    def on_submit_clicked(self):
        selected_date = self.calendar_widget.selectedDate()
        selected_time = self.time_edit.time()

        data = selected_date.toString("yyyy-MM-dd")
        ora = selected_time.toString("HH:mm")

        # Ottieni la durata selezionata dal QComboBox
        durata = self.combo_durata.currentText().split(" ")[1]  # Estrai solo la parte numerica della durata

        self.data_selezionata = f"{data} {ora}"
        self.durata = durata

        if self.data_selezionata and self.durata:
            scegli_aula_view = ScegliAulaView(self.tipo_prenotazione, self.data_selezionata, self.durata)
            self.main_window.set_view(scegli_aula_view)
        else:
            QMessageBox.warning(self, "Attenzione", "Devi selezionare una data e una durata.")

    def on_prenota_singolo_clicked(self):
        pass
