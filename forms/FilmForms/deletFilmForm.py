import sqlite3

import main


class DeleteFilm:
    def __init__(self, parent=None):
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.con = sqlite3.connect(main.DB_NAME)  # connecting to data base
        self.id = self.parent.tableWidget.item(self.parent.tableWidget.currentRow(),
                                               0).text()  # taking first column of current row
        self.delete_film()

    def delete_film(self):
        cur = self.con.cursor()
        cur.execute(f"""DELETE FROM films
        WHERE id = ?""", (self.id,))  # deleting selected film from data base
        self.con.commit()
        self.parent.rendering_table()
