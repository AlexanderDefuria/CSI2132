import psycopg2


class DB:
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host='db-postgresql-nyc3-00259-do-user-7775406-0.b.db.ondigitalocean.com',
                database='uottawa',
                user='uottawa',
                password='GTf1BoV4mjZK0R3z',
                port='25060'
            )
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return

    def query(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        out = cur.fetchall()
        cur.close()
        return out


def build():
    db = DB()
    db.query("")
