import os

from PySide6.QtGui import QImage
from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout, QSpinBox, QDateEdit, QFileDialog
from datetime import datetime

from abstract.view import View
from utils.ui import PATH_IMAGE, FOLDER_COVER


class InserisciLibroView(View):
    def create_layout(self) -> None:
        self.setWindowTitle('Inserisci libro')
        layout = QVBoxLayout()

        grid_layout = QGridLayout()

        # Prima riga
        '''label1 = QLabel('immagine:')
        self.input1 = QFileDialog()
        grid_layout.addWidget(label1, 0, 0)
        grid_layout.addWidget(self.input1, 0, 1)'''

        # Seconda riga
        label2 = QLabel('titolo:')
        self.input2 = QLineEdit()
        grid_layout.addWidget(label2, 1, 0)
        grid_layout.addWidget(self.input2, 1, 1)

        # Terza riga
        label3 = QLabel('autori:')
        self.input3 = QLineEdit()
        grid_layout.addWidget(label3, 2, 0)
        grid_layout.addWidget(self.input3, 2, 1)

        label4 = QLabel('editore:')
        self.input4 = QLineEdit()
        grid_layout.addWidget(label4, 3, 0)
        grid_layout.addWidget(self.input4, 3, 1)

        label5 = QLabel('isbn:')
        self.input5 = QLineEdit()
        grid_layout.addWidget(label5, 4, 0)
        grid_layout.addWidget(self.input5, 4, 1)

        label6 = QLabel('anno edizione:')
        self.input6 = QDateEdit()
        grid_layout.addWidget(label6, 5, 0)
        grid_layout.addWidget(self.input6, 5, 1)

        label7 = QLabel('anno pubblicazione:')
        self.input7 = QDateEdit()
        grid_layout.addWidget(label7, 6, 0)
        grid_layout.addWidget(self.input7, 6, 1)

        label8 = QLabel('disponibili:')
        self.input8 = QSpinBox()
        self.input8.setMinimum(1)
        grid_layout.addWidget(label8, 7, 0)
        grid_layout.addWidget(self.input8, 7, 1)

        label9 = QLabel('dati:')
        self.input9 = QLineEdit()
        grid_layout.addWidget(label9, 8, 0)
        grid_layout.addWidget(self.input9, 8, 1)

        # immagine
        self.button = QPushButton("Select Image", self)
        self.button.setGeometry(150, 80, 100, 40)
        self.button.clicked.connect(self.show_file_dialog)
        grid_layout.addWidget(self.button, 9, 0)

        layout.addLayout(grid_layout)

        invia = QPushButton('Aggiungi libro')
        invia.clicked.connect(self.invia)
        layout.addWidget(invia)

        self.setLayout(layout)

    def attach_controllers(self) -> None:
        from app import controller_gestione_libri
        self.attach(controller_gestione_libri)

    def __init__(self):
        super().__init__()
        self.filename = None

    def show_file_dialog(self):
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
                save_dialog = QFileDialog(self, "Save Image", path_copertine, "Images (*.png *.jpg *.jpeg *.bmp *.gif *.ppm *.pgm)")
                save_dialog.setAcceptMode(QFileDialog.AcceptSave)

                if save_dialog.exec_():
                    save_file = save_dialog.selectedFiles()[0]
                    self.filename = os.path.basename(save_file)
                    if image.save(save_file):
                        print(f"Image saved to: {save_file}")
                    else:
                        print("Failed to save image.")
            else:
                print("Failed to load the selected image.")

    def invia(self):
        if self.input2.text() and self.input2.text() and self.input3.text() and self.input4.text() and self.input5.text() and self.input6.text() and self.input7.text() and self.input8.text() and self.input9.text():
            self.notify(message="inserisci_libro",
                        data={"titolo": self.input2.text(),
                              "autori": self.input3.text(),
                              "editore": self.input4.text(),
                              "isbn": self.input5.text(),
                              "disponibili": self.input8.text(),
                              "dati": self.input9.text(),
                              "anno_edizione": datetime.strptime(self.input6.date().toString('yyyy-MM-dd'), '%Y-%m-%d'),
                              "anno_pubblicazione": datetime.strptime(self.input7.date().toString('yyyy-MM-dd'),
                                                                      '%Y-%m-%d'),
                              "immagine": self.filename})
        else:
            pass
