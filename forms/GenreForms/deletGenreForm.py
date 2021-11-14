import sqlite3

import main


class DeleteGenre:
    def __init__(self, parent=None):
        self.parent = parent

        self.initUI()

    def initUI(self):
        self.con = sqlite3.connect(main.DB_NAME)
        self.id = self.parent.tableWidget_3.item(self.parent.tableWidget_3.currentRow(), 0).text()
        self.delete_genre()

    def delete_genre(self):
        cur = self.con.cursor()
        cur.execute(f"""DELETE FROM genres
        WHERE id = ?""", (self.id,))
        self.con.commit()
        self.parent.rendering_table()