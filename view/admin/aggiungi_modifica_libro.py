import os
from datetime import datetime
from typing import Optional
from uuid import uuid4

from PySide6.QtCore import QDate, QDateTime
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QLineEdit, QDateEdit, QSpinBox, QPushButton, QGridLayout, QLabel, QVBoxLayout, \
    QHBoxLayout, QMessageBox, QFileDialog

from abstract import View
from database import Libro
from utils.ui import PATH_IMAGE, FOLDER_COVER


class AggiungiModificaLibroView(View):
    def create_layout(self) -> None:
        v_layout = QVBoxLayout(self)

        adesso = datetime.now()
        q_adesso = QDate(adesso.year, adesso.month, adesso.day)
        self.anno_edizione.setDisplayFormat("yyyy")
        self.anno_pubblicazione.setDisplayFormat("yyyy")
        self.anno_edizione.setMaximumDate(q_adesso)
        self.anno_pubblicazione.setMaximumDate(q_adesso)
        self.disponibili.setMinimum(1)
        self.seleziona_copertina.setText("Seleziona copertina")
        self.seleziona_copertina.setFixedWidth(150)
        self.conferma.setFixedWidth(150)

        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(self.conferma)
        h_layout.addStretch()

        label_window_title = QLabel()
        if self.metodo == "aggiungi":
            label_window_title.setText("Aggiungi libro")
            self.conferma.setText("Aggiungi")
        elif self.metodo == "modifica":
            label_window_title.setText("Modifica libro")
            self.conferma.setText("Modifica")
        else:
            raise ValueError("metodo aggiungi/modifica libro view errato!")

        grid_layout = QGridLayout()

        label_titolo = QLabel("Titolo")
        label_autori = QLabel("Autori")
        label_editore = QLabel("Editore")
        label_isbn = QLabel("ISBN")
        label_anno_edizione = QLabel("Anno edizione")
        label_anno_pubblicazione = QLabel("Anno pubblicazione")
        label_disponibili = QLabel("Disponibili")
        label_dati = QLabel("Dati")

        grid_layout.addWidget(label_titolo, 0, 0)
        grid_layout.addWidget(self.titolo, 0, 1)
        grid_layout.addWidget(label_autori, 1, 0)
        grid_layout.addWidget(self.autori, 1, 1)
        grid_layout.addWidget(label_editore, 2, 0)
        grid_layout.addWidget(self.editore, 2, 1)
        grid_layout.addWidget(label_isbn, 3, 0)
        grid_layout.addWidget(self.isbn, 3, 1)
        grid_layout.addWidget(label_anno_edizione, 4, 0)
        grid_layout.addWidget(self.anno_edizione, 4, 1)
        grid_layout.addWidget(label_anno_pubblicazione, 5, 0)
        grid_layout.addWidget(self.anno_pubblicazione, 5, 1)
        grid_layout.addWidget(label_disponibili, 6, 0)
        grid_layout.addWidget(self.disponibili, 6, 1)
        grid_layout.addWidget(label_dati, 7, 0)
        grid_layout.addWidget(self.dati, 7, 1)
        grid_layout.addWidget(self.seleziona_copertina, 8, 0)
        grid_layout.addWidget(self.label_copertina, 8, 1)

        v_layout.addLayout(grid_layout)
        v_layout.addStretch()
        v_layout.addLayout(h_layout)

        self.seleziona_copertina.clicked.connect(self.dialog_selezione_copertina)
        self.conferma.clicked.connect(self.aggiungi_modifica_libro)

    def __init__(self, metodo: str, libro: Optional[Libro] = None):
        self.metodo = metodo
        self.libro = libro

        self.titolo = QLineEdit()
        self.autori = QLineEdit()
        self.editore = QLineEdit()
        self.isbn = QLineEdit()
        self.anno_edizione = QDateEdit()
        self.anno_pubblicazione = QDateEdit()
        self.disponibili = QSpinBox()
        self.dati = QLineEdit()
        self.copertina = ""
        self.label_copertina = QLabel()
        self.seleziona_copertina = QPushButton()
        self.conferma = QPushButton()

        self.fill_dati_libro()

        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_libri
        self.attach(controller_libri)

    def fill_dati_libro(self):
        if self.libro:
            self.titolo.setText(self.libro.titolo)
            self.autori.setText(self.libro.autori)
            self.editore.setText(self.libro.editore)
            self.isbn.setText(self.libro.isbn)
            self.anno_edizione.setDateTime(QDateTime(self.libro.anno_edizione))
            self.anno_pubblicazione.setDateTime(QDateTime(self.libro.anno_pubblicazione))
            self.disponibili.setValue(self.libro.disponibili)
            self.dati.setText(self.libro.dati)
            self.copertina = self.libro.immagine
            self.label_copertina.setText(self.copertina)

    def aggiungi_modifica_libro(self):
        if not (titolo := self.titolo.text()):
            QMessageBox.warning(self,
                                "Attenzione",
                                "Devi inserire il titolo del libro.")
            return
        if not (autori := self.autori.text()):
            QMessageBox.warning(self,
                                "Attenzione",
                                "Devi inserire gli autori del libro.")
            return
        if not (editore := self.editore.text()):
            QMessageBox.warning(self,
                                "Attenzione",
                                "Devi inserire l'editore del libro.")
            return
        if not (isbn := self.isbn.text()):
            QMessageBox.warning(self,
                                "Attenzione",
                                "Devi inserire l'ISBN del libro.")
            return
        if not (anno_edizione := self.anno_edizione.date().toPython()):
            QMessageBox.warning(self,
                                "Attenzione",
                                "Devi inserire l'anno edizione del libro.")
            return
        if not (anno_pubblicazione := self.anno_pubblicazione.date().toPython()):
            QMessageBox.warning(self,
                                "Attenzione",
                                "Devi inserire l'anno pubblicazione del libro.")
            return
        if not (disponibili := self.disponibili.value()):
            QMessageBox.warning(self,
                                "Attenzione",
                                "Devi inserire il numero di copie presenti.")
            return
        if not (dati := self.dati.text()):
            QMessageBox.warning(self,
                                "Attenzione",
                                "Devi inserire i dati del libro.")
            return
        if not self.copertina:
            self.copertina = "default.jpg"
        data = {"titolo": titolo,
                "autori": autori,
                "editore": editore,
                "isbn": isbn,
                "anno_edizione": anno_edizione,
                "anno_pubblicazione": anno_pubblicazione,
                "disponibili": disponibili,
                "dati": dati,
                "copertina": self.copertina}
        if self.metodo == "aggiungi":
            self.notify("aggiungi_libro",
                        data=data)
        elif self.metodo == "modifica":
            data.update({"id_libro": self.libro.id})
            self.notify("modifica_libro",
                        data=data)
        else:
            raise ValueError("metodo aggiungi/modifica libro view errato!")

    def dialog_selezione_copertina(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog(self, options=options)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp *.gif *.ppm *.pgm)")
        file_dialog.setViewMode(QFileDialog.List)

        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            image = QImage(selected_file)

            if not image.isNull():
                path_copertine = os.path.join(os.path.join(os.getcwd(), PATH_IMAGE), FOLDER_COVER)
                extension = selected_file.split('.')[-1].lower()
                if self.metodo == "aggiungi":
                    filename_without_extension = str(uuid4())[:8]
                elif self.metodo == "modifica":
                    filename_without_extension = self.libro.immagine.split(".")[0]
                else:
                    raise ValueError("metodo aggiungi/modifica libro view errato!")
                self.copertina = f"{filename_without_extension}.{extension}"
                self.label_copertina.setText(self.copertina)
                save_file = os.path.join(path_copertine, self.copertina)
                if image.save(save_file):
                    print(f"Image saved to: {save_file}")
                else:
                    print("Failed to save image.")
            else:
                print("Failed to load the selected image.")
