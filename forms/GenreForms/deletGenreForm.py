import sqlite3

import main


class DeleteGenre:
    def __init__(self, item, parent=None):
        self.parent = parent
        self.item = item
        self.initUI()

    def initUI(self):
        self.con = sqlite3.connect(main.DB_NAME)  # connecting to data base
        self.id = self.item.text()  # current row's column
        self.delete_genre()

    def delete_genre(self):
        cur = self.con.cursor()
        cur.execute(f"""DELETE FROM genres
        WHERE id = ?""", (self.id,))  # deleting genre
        self.con.commit()
        self.parent.rendering_table()