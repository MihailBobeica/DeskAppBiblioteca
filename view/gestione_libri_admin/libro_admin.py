from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QFrame, QLineEdit, QDateEdit, QSpinBox, QGridLayout, \
    QMessageBox
from view.home_admin import HomeAdminView
from abstract.view import View
from database import Libro
from model.libro import Libro as model_libro
from datetime import datetime


class LibroView(View):
    def create_layout(self) -> None:
        # content
        # copertina
        '''image_label = QLabel()
        pixmap = QPixmap(get_image_path(self.info.immagine)).scaled(320, 480, aspectMode=Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)'''
        # font
        font = QFont()
        font.setPointSize(14)
        # titolo
        label_title = QLabel("Titolo: ")
        self.input1 = QLineEdit()
        self.input1.setText(self.info.titolo)
        label_title.setWordWrap(True)
        label_title.setFont(font)
        # autori
        label_autor = QLabel("Autori: ")
        self.input2 = QLineEdit()
        self.input2.setText(self.info.autori)
        label_autor.setWordWrap(True)
        label_autor.setFont(font)
        # anno edizione
        label_anno_edizione = QLabel("Anno edizione: ")
        label_anno_edizione.setFont(font)
        self.input3 = QDateEdit()
        self.input3.setDate(self.info.anno_edizione)
        # anno pubblicazione
        label_anno_pubblicazione = QLabel("Anno pubblicazione: ")
        label_anno_pubblicazione.setFont(font)
        self.input4 = QDateEdit()
        self.input4.setDate(self.info.anno_pubblicazione)
        # editore
        label_editore = QLabel("Editore: ")
        label_editore.setFont(font)
        self.input5 = QLineEdit()
        self.input5.setText(self.info.editore)
        # copie disponibili
        label_disponibili = QLabel("Copie disponibili: ")
        label_disponibili.setFont(font)
        self.input6 = QSpinBox()
        self.input6.setValue(int(self.info.disponibili))
        # dati generici
        label_dati = QLabel("Dati: ")
        label_dati.setFont(font)
        self.input7 = QLineEdit()
        self.input7.setText(self.info.dati)

        # layout
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        #layout.setSpacing(50)

        contenitore_dati = QFrame()
        contenitore_dati.setMaximumSize(320, 480)

        v_layout = QGridLayout()
        #v_layout.setSpacing(8)

        v_layout.addWidget(label_title,0,0)
        v_layout.addWidget(label_autor,1,0)
        v_layout.addWidget(label_editore,4,0)
        v_layout.addWidget(label_anno_edizione,2,0)
        v_layout.addWidget(label_anno_pubblicazione,3,0)
        v_layout.addWidget(label_disponibili,5,0)
        v_layout.addWidget(label_dati,6,0)
        v_layout.addWidget(self.input1,0,1)
        v_layout.addWidget(self.input2,1,1)
        v_layout.addWidget(self.input3,2,1)
        v_layout.addWidget(self.input4,3,1)
        v_layout.addWidget(self.input5,4,1)
        v_layout.addWidget(self.input6,5,1)
        v_layout.addWidget(self.input7,6,1)
        #v_layout.addStretch(1)
        self.add_buttons(labels=("Indietro",
                                 "Salva Modifiche",
                                 "Rimuovi"),
                         layout=v_layout)

        contenitore_dati.setLayout(v_layout)

        #layout.addWidget(image_label)
        layout.addWidget(contenitore_dati)

    def connect_buttons(self):
        button_back = self.get_button("Indietro")
        button_back.clicked.connect(self.go_back)
        button_back = self.get_button("Salva Modifiche")
        button_back.clicked.connect(self.modifica)
        button_back = self.get_button("Rimuovi")
        button_back.clicked.connect(self.elimina)

    def __init__(self, db_libro: Libro):
        self.info = db_libro
        super().__init__()

    def go_back(self):

        self.redirect(HomeAdminView())

    def modifica(self):
        dati = {
            "titolo" : self.input1.text(),
            "autori" : self.input2.text(),
            "anno_edizione" : datetime.strptime(self.input3.text(), '%d/%m/%Y'),
            "anno_pubblicazione" : datetime.strptime(self.input4.text(), '%d/%m/%Y'),
            "editore" : self.input5.text(),
            "dati": self.input7.text(),
            "disponibili" : self.input6.text()
        }
        model_libro.modifica(self,dati,self.info.isbn)
        self.redirect(HomeAdminView())


    def elimina(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setText("Conferma")
        msg_box.setWindowTitle("Sei sicuro di voler rimuovere il libro?")
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Ok)
        response = msg_box.exec()
        if response == QMessageBox.Ok:
            model_libro.elimina(self,self.info)

        self.redirect(HomeAdminView())

