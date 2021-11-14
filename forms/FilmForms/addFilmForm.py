import sqlite3

import main
from PyQt5.QtWidgets import QDialog

from design.addEditFilmForm import BookFormUI


class AddFilm(QDialog, BookFormUI):
    def __init__(self, parent=None):
        super(AddFilm, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setModal(True)
        self.con = sqlite3.connect(main.DB_NAME)  # connect to data base
        self.pushButton.setText('Добавить')
        self.pushButton.clicked.connect(self.add_data)  # call function add_data when button clicked
        cur = self.con.cursor()
        items = cur.execute("""SELECT title, id FROM genres""").fetchall()  # all genres
        self.comboBox.addItems([i[0] for i in items])
        self.genre = {}
        for i in items:
            self.genre[i[0]] = i[1]

    def closeEvent(self, event):
        self.parent.show()

    def add_data(self):
        if len(self.lineEdit.text()) > 0 and int(self.lineEdit_2.text()) <= 2021 and int(self.lineEdit_4.text()) >= 1:
            title = self.lineEdit.text()
            year = self.lineEdit_2.text()
            genre = self.comboBox.currentText()
            duration = self.lineEdit_4.text()
            cur = self.con.cursor()
            cur.execute(f"""INSERT INTO films(title, year, genre, duration)
             VALUES(?,?,?,?)""", (title, year, self.genre[genre], duration))  # adding new film into data base
            self.con.commit()
            self.close()
