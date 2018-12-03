import os
from psycopg2.pool import ThreadedConnectionPool

from datetime import datetime, timedelta

from lawbreaker.exceptions import NoResultsFound


MIN_CONNECTIONS = 1
MAX_CONNECTIONS = 10


class Database(object):
    def __init__(self):
        """
        Query to aggregate expiry details grouped by day and month,

            SELECT extract(day from expiry) AS day,
                   extract(month from expiry) AS month,
                   count(*)
            FROM characters
            GROUP BY day, month
            ORDER BY day, month;

        Can be created into a view with,
            CREATE VIEW name AS query
        """
        database_url = os.environ['DATABASE_URL']
        self.pool = ThreadedConnectionPool(MIN_CONNECTIONS,
                                           MAX_CONNECTIONS,
                                           dsn=database_url,
                                           sslmode='require')

        conn = self.pool.getconn()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS characters (character_id text PRIMARY KEY UNIQUE,
                                                                 character_json text,
                                                                 expiry timestamp)''')
        conn.commit()
        cursor.close()
        self.pool.putconn(conn)

        self.clear_expired()

    def clear_expired(self):
        print('Deleting expired permalinks')
        conn = self.pool.getconn()
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM characters WHERE expiry < now()''')
        conn.commit()
        cursor.close()
        self.pool.putconn(conn)

    def select(self, character_id):
        conn = self.pool.getconn()
        cursor = conn.cursor()
        cursor.execute(
                "SELECT character_json FROM characters WHERE character_id=%s", (character_id,))
        result = cursor.fetchone()
        if result is None:
            cursor.close()
            self.pool.putconn(conn)
            raise NoResultsFound
        else:
            cursor.execute("UPDATE characters SET expiry=%s where character_id=%s",
                           (datetime.utcnow()+timedelta(days=30), character_id))
            conn.commit()
            cursor.close()
            self.pool.putconn(conn)
            return result[0]

    def insert(self, character_id, character_json):
        conn = self.pool.getconn()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO characters(character_id, character_json, expiry) VALUES (%s, %s, %s)""",
                       (character_id, character_json, datetime.utcnow()+timedelta(days=2)))
        conn.commit()
        cursor.close()
        self.pool.putconn(conn)
