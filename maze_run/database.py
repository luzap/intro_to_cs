"""database.py:

Interface with local database for simplified
score management (no need to manually parse through
text files.)
"""

import sqlite3


class ScoresDB:

    def __init__(self):
        self.connection = sqlite3.connect('highscores.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS highscores (id integer primary key \
            autoincrement, name text, score real)""")

    def get_scores(self):
        self.cursor.execute(
            "SELECT name, score FROM highscores ORDER By score DESC")
        return self.cursor.fetchall()

    def add_score(self, name: str, score: float):
        # The first value is self-incrementing, so no value needed
        self.cursor.execute(
            "INSERT INTO highscores values (?, ?, ?)",
            (None, name, score)
        )
        self.connection.commit()

    def del_null(self):
        self.cursor.execute("DELETE FROM highscores WHERE name=''")
        self.connection.commit()
