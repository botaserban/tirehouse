import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS anvelope (id INTEGER PRIMARY KEY, serieSasiu text, nrInmatriculare text, client text, dimFata text, dimSpate text, profil text, produs text, cantitate text, dataLive text )")
        self.cur.execute("CREATE TABLE IF NOT EXISTS iesiri (id INTEGER PRIMARY KEY, serieSasiu text, nrInmatriculare text, client text, dimFata text, dimSpate text, profil text, produs text, cantitate text, dataLive text )")
        self.conn.commit()



    def fetch(self):
        self.cur.execute("SELECT * FROM anvelope")
        rows = self.cur.fetchall()
        return rows

    def fetch_iesiri(self):
        self.cur.execute("SELECT * FROM iesiri")
        rows = self.cur.fetchall()
        return rows

    def insert(self, serieSasiu, nrInmatriculare, client, dimFata, dimSpate, profil, produs, cantitate, dataLive):
        self.cur.execute("INSERT INTO anvelope VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(serieSasiu, nrInmatriculare, client, dimFata, dimSpate, profil, produs, cantitate, dataLive))
        self.conn.commit()

    def insert_iesiri(self, serieSasiu, nrInmatriculare, client, dimFata, dimSpate, profil, produs, cantitate, dataLive):
        self.cur.execute("INSERT INTO iesiri VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(serieSasiu, nrInmatriculare, client, dimFata, dimSpate, profil, produs, cantitate, dataLive))
        self.conn.commit()


    def remove(self, id):
        self.cur.execute("DELETE FROM anvelope WHERE id=?", (id,))
        self.conn.commit()

    def remove_iesiri(self, id):
        self.cur.execute("DELETE FROM iesiri WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, serieSasiu, nrInmatriculare, client, dimFata, dimSpate, profil, produs, cantitate, dataLive):
        self.cur.execute("UPDATE anvelope SET serieSasiu = ?, nrInmatriculare = ?, client = ?, dimFata = ?, dimSpate = ?, profil = ?, produs = ?, cantitate = ?, dataLive = ? WHERE id = ?", (serieSasiu, nrInmatriculare, client, dimFata, dimSpate, profil, produs, cantitate,dataLive, id))
        self.conn.commit()


    def __del__(self):
        self.conn.close()

db = Database('store.db')
