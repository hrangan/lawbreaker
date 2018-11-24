import os
import psycopg2

from datetime import datetime, timedelta

from lawbreaker.exceptions import NoResultsFound


class Database(object):
    def __init__(self):
        database_url = os.environ['DATABASE_URL']
        conn = psycopg2.connect(database_url, sslmode='require')
        conn.set_session(autocommit=True)
        self.cursor = conn.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS characters (character_id text PRIMARY KEY UNIQUE,
                                                                      character_json text,
                                                                      expiry timestamp)''')

        self.cursor.execute('''DELETE FROM characters WHERE expiry < now()''')

    def select(self, character_id):
        self.cursor.execute("SELECT character_json FROM characters WHERE character_id=%s", (character_id,))
        result = self.cursor.fetchone()
        if result is None:
            raise NoResultsFound
        else:
            self.cursor.execute("UPDATE characters SET expiry=%s where character_id=%s",
                                (datetime.utcnow()+timedelta(days=30), character_id))
            return result[0]

    def insert(self, character_id, character_json):
        self.cursor.execute("""INSERT INTO characters(character_id, character_json, expiry) VALUES (%s, %s, %s)""",
                            (character_id, character_json, datetime.utcnow()+timedelta(days=2)))
