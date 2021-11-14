import sqlite3
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from design.mainUI import MainUI
from forms.FilmForms import addFilmForm, editFilmForm, deletFilmForm
from forms.GenreForms import addGenreForm, editGenreForm, deletGenreForm

DB_NAME = "data/films_db.sqlite"


class MyWidget(QMainWindow, MainUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect(DB_NAME)
        self.pushButton.clicked.connect(self.open_create_widget)
        self.pushButton_2.clicked.connect(self.open_change_widget)
        self.pushButton_3.clicked.connect(self.open_delete_widget)
        self.pushButton_7.clicked.connect(self.open_create_genre)
        self.pushButton_8.clicked.connect(self.open_change_genre)
        self.pushButton_9.clicked.connect(self.open_delete_genre)
        self.rendering_table()
        self.titles = None
        self.do_paint = False
        self.tabWidget.setStyleSheet('background-image: url("space.jpg");')
        self.tableWidget.setStyleSheet('background: none;')
        self.tableWidget_3.setStyleSheet('background: none;')
        self.pushButton.setStyleSheet('background: none;')
        self.pushButton_2.setStyleSheet('background: none;')
        self.pushButton_3.setStyleSheet('background: none;')
        self.pushButton_7.setStyleSheet('background: none;')
        self.pushButton_8.setStyleSheet('background: none;')
        self.pushButton_9.setStyleSheet('background: none;')

    def open_create_widget(self):
        ex1 = addFilmForm.AddFilm(self)
        ex1.show()
        self.rendering_table()

    def open_change_widget(self):
        if self.tableWidget.item(self.tableWidget.currentRow(), 0) is not None:
            ex1 = editFilmForm.ChangeFilm(self)
            ex1.show()
            self.rendering_table()

    def open_delete_widget(self):
        if self.tableWidget.item(self.tableWidget.currentRow(), 0) is not None:
            deletFilmForm.DeleteFilm(self)
            self.rendering_table()

    def open_create_genre(self):
        ex1 = addGenreForm.AddGenre(self)
        ex1.show()
        self.rendering_table()

    def open_change_genre(self):
        if self.tableWidget_3.item(self.tableWidget_3.currentRow(), 0) is not None:
            ex1 = editGenreForm.ChangeGenre(self)
            ex1.show()
            self.rendering_table()

    def open_delete_genre(self):
        if self.tableWidget_3.item(self.tableWidget_3.currentRow(), 0) is not None:
            ex1 = deletGenreForm.DeleteGenre(self, self.tableWidget_3.item(self.tableWidget_3.currentRow(), 0))
            self.rendering_table()

    def rendering_table(self):
        cur = self.con.cursor()
        table = cur.execute("""SELECT films.id as id,
       films.title as title,
       films.year as year, 
    genres.title as GenreName,
    films.duration as duration
FROM
    films
    LEFT JOIN genres
ON films.genre = genres.id
ORDER BY title
""").fetchall()
        genres = cur.execute("""SELECT * FROM genres""").fetchall()
        self.tableWidget_3.setRowCount(len(genres))
        self.tableWidget_3.setColumnCount(len(genres[0]))
        for i, row in enumerate(genres):
            for j, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget_3.setItem(i, j, item)

        self.tableWidget.setRowCount(len(table))
        self.tableWidget.setColumnCount(len(table[0]))
        for i, row in enumerate(table):
            for j, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, j, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
