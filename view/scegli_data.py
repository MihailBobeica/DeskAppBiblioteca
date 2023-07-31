from PySide6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QCalendarWidget, QComboBox, QMessageBox, QTimeEdit
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
        self.calendar_widget.setMinimumDate(QDate.currentDate())
        self.calendar_widget.setMaximumDate(QDate(2099, 12, 31))
        self.calendar_widget.setFixedSize(200, 200)
        self.calendar_widget.setFirstDayOfWeek(Qt.Monday)
        self.calendar_widget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar_widget.setNavigationBarVisible(False)
        layout.addWidget(self.calendar_widget)

        self.selected_date_label = QLabel("Data selezionata: ")
        layout.addWidget(self.selected_date_label)

        label_ora = QLabel("Ora di inizio:")
        layout.addWidget(label_ora)

        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("HH:mm")
        self.time_edit.setTimeRange(QTime(8, 30), QTime(18, 45))
        layout.addWidget(self.time_edit)

        label_durata = QLabel("Scegli la durata:")
        layout.addWidget(label_durata)

        self.combo_durata = QComboBox()
        self.combo_durata.addItems(["1 ora", "2 ore", "3 ore", "4 ore"])  # Opzioni fisse per la durata
        layout.addWidget(self.combo_durata)

        submit_button = QPushButton("Avanti")
        layout.addWidget(submit_button)

        submit_button.clicked.connect(self.on_submit_clicked)
        self.calendar_widget.clicked.connect(self.on_calendar_clicked)

    def on_calendar_clicked(self, date):
        selected_date = date.toString("dd/MM/yyyy")
        self.selected_date_label.setText("Data selezionata: " + selected_date)

    def on_submit_clicked(self):
        selected_date = self.calendar_widget.selectedDate()
        selected_time = self.time_edit.time()

        data = selected_date.toString("yyyy-MM-dd")
        ora = selected_time.toString("HH:mm")

        durata = self.combo_durata.currentText().split(" ")[0]  # Estrai solo la parte numerica della durata

        self.data_selezionata = f"{data} {ora}"
        self.durata = durata

        if self.data_selezionata and self.durata:
            scegli_aula_view = ScegliAulaView(self.tipo_prenotazione, self.data_selezionata, self.durata)
            self.main_window.set_view(scegli_aula_view)
        else:
            QMessageBox.warning(self, "Attenzione", "Devi selezionare una data e una durata.")
