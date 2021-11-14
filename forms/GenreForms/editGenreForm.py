import sqlite3

import main
from PyQt5.QtWidgets import QDialog

from design.addEditGenreForm import GenreFormUI


class ChangeGenre(QDialog, GenreFormUI):
    def __init__(self, parent=None):
        super(ChangeGenre, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setModal(True)
        self.con = sqlite3.connect(main.DB_NAME)  # connecting to data base
        self.pushButton.setText('Изменить')
        self.pushButton.clicked.connect(self.change_data)  # button clicked
        cur = self.con.cursor()
        self.id = self.parent.tableWidget_3.item(self.parent.tableWidget_3.currentRow(), 0).text()

        data = cur.execute(f"""SELECT title FROM genres
                WHERE id = {self.id}""").fetchall()
        self.lineEdit.setText(data[0][0])

    def closeEvent(self, event):
        self.parent.show()

    def change_data(self):
        if len(self.lineEdit.text()) > 0:
            title = self.lineEdit.text()
            cur = self.con.cursor()
            cur.execute(f"""UPDATE genres SET 
            title = ?
            WHERE id = ?""", (title, self.id))
            self.con.commit()
            self.parent.rendering_table()
            self.close()
