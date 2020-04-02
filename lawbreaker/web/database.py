import os

from contextlib import contextmanager
from datetime import datetime, timedelta

from psycopg2.pool import ThreadedConnectionPool

from lawbreaker.exceptions import NoResultsFound


MIN_CONNECTIONS = 1
MAX_CONNECTIONS = 10


class Database(object):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Query to aggregate expiry details grouped by day and month,

            SELECT
                   extract(day from expiry) AS day,
                   extract(month from expiry) AS month,
                   extract(year from expiry) AS year,
                   count(*)
            FROM characters
            GROUP BY year, month, day
            ORDER BY year, month, day;


        Can be created into a view with,
            CREATE VIEW name AS query
        """
        self._pool = None

    @contextmanager
    def connectionpool(self, *args, **kwargs):
        if self._pool is None:
            self._pool = ThreadedConnectionPool(MIN_CONNECTIONS,
                                                MAX_CONNECTIONS,
                                                dsn=os.environ['DATABASE_URL'])
            self.create_db()

        conn = self._pool.getconn()
        cursor = conn.cursor()
        try:
            yield cursor
        finally:
            conn.commit()
            cursor.close()
            self._pool.putconn(conn)

    def create_db(self):
        with self.connectionpool() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS characters (character_id text PRIMARY KEY UNIQUE,
                                                                     character_json text,
                                                                     expiry timestamp)''')

    def clear_expired(self):
        with self.connectionpool() as cursor:
            print('Deleting expired permalinks')
            cursor.execute('''DELETE FROM characters WHERE expiry < now()''')

    def select(self, character_id):
        with self.connectionpool() as cursor:
            cursor.execute(
                    "SELECT character_json FROM characters WHERE character_id=%s", (character_id,))
            result = cursor.fetchone()
            if result is None:
                raise NoResultsFound
            else:
                cursor.execute("UPDATE characters SET expiry=%s where character_id=%s",
                               (datetime.utcnow()+timedelta(days=30), character_id))
                return result[0]

    def insert(self, character_id, character_json):
        with self.connectionpool() as cursor:
            cursor.execute("""INSERT INTO characters (character_id, character_json, expiry)
                              VALUES (%s, %s, %s)""",
                           (character_id, character_json, datetime.utcnow()+timedelta(days=2)))
