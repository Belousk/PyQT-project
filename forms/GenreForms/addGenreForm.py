import sqlite3
import main
from PyQt5.QtWidgets import QDialog

from design.addEditGenreForm import GenreFormUI


class AddGenre(QDialog, GenreFormUI):
    def __init__(self, parent=None):
        super(AddGenre, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setModal(True)
        self.con = sqlite3.connect(main.DB_NAME)  # connection to data base
        self.pushButton.setText('Добавить')
        self.pushButton.clicked.connect(self.add_data)  # call function when button clicked

    def closeEvent(self, event):
        self.parent.show()

    def add_data(self):
        if len(self.lineEdit.text()) > 0:
            title = self.lineEdit.text()
            cur = self.con.cursor()
            cur.execute(f"""INSERT INTO genres(title)
             VALUES(?)""", (title,))
            self.con.commit()
            self.parent.rendering_table()
            self.close()