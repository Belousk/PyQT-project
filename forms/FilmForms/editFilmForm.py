import sqlite3

import main
from PyQt5.QtWidgets import QDialog

from design.addEditFilmForm import BookFormUI


class ChangeFilm(QDialog, BookFormUI):
    def __init__(self, parent=None):
        super(ChangeFilm, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setModal(True)
        self.con = sqlite3.connect(main.DB_NAME)  # connecting to data base
        self.pushButton.setText('Изменить')
        self.pushButton.clicked.connect(self.change_data)  # call function when button clicked
        cur = self.con.cursor()
        items = cur.execute("""SELECT title, id FROM genres""").fetchall()  # taking all genres
        self.comboBox.addItems([i[0] for i in items])
        self.genre = {}
        self.id = self.parent.tableWidget.item(self.parent.tableWidget.currentRow(),
                                               0)  # taking first column of current row
        if self.id:
            self.id = self.id.text()
            data = cur.execute(f"""SELECT title, year, duration FROM films
                    WHERE id = {self.id}""").fetchall()
            self.lineEdit.setText(data[0][0])  # putting title form data base
            self.lineEdit_2.setText(str(data[0][1]))  # putting year form data base
            self.lineEdit_4.setText(str(data[0][2]))  # putting duration form data base
            self.pushButton.clicked.connect(self.change_data)  # call function when button clicked
        else:
            self.close()

        for i in items:
            self.genre[i[0]] = i[1]

    def closeEvent(self, event):
        self.parent.show()

    def change_data(self):

        if len(self.lineEdit.text()) > 0 and int(self.lineEdit_2.text()) <= 2021 and int(
                self.lineEdit_4.text()) >= 1 and self.id:
            title = self.lineEdit.text()
            year = self.lineEdit_2.text()
            genre = self.comboBox.currentText()
            duration = self.lineEdit_4.text()
            cur = self.con.cursor()
            cur.execute(f"""UPDATE films SET 
            title = ?,
            year = ?,
            genre = ?,
            duration = ?
            WHERE id = ?""", (title, year, self.genre[genre], duration, self.id))  # changing information about film
            self.con.commit()
            self.parent.rendering_table()
            self.close()
