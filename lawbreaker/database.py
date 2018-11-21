import sqlite3
from datetime import datetime

from lawbreaker.exceptions import NoResultsFound


class Database(object):
    def __init__(self):
        self.conn = sqlite3.connect('lawbreaker.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS characters
                                   (character_id text,
                                    character_json text,
                                    timestamp text)''')
        self.conn.commit()

    def select(self, character_id):
        result = self.cursor.execute('''SELECT character_json FROM characters WHERE character_id=?''',
                                     (character_id,))
        try:
            return result.fetchone()[0]
        except TypeError:
            raise NoResultsFound

    def insert(self, character_id, character_json):
        self.cursor.execute('''INSERT INTO characters(character_id, character_json, timestamp)
                               VALUES (?, ?, ?)''',
                            (character_id, character_json, str(datetime.utcnow())))
        self.conn.commit()
