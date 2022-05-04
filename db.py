import sqlite3
class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS clothes (id INTEGER PRIMARY KEY, clothes text, customer text, retailer text, price text, order_time datetime)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM clothes")
        rows = self.cur.fetchall()
        return rows

    def insert(self, clothes, customer, retailer, price, order_time):
        self.cur.execute("INSERT INTO clothes VALUES (NULL, ?, ?, ?, ?, ?)",
                         (clothes, customer, retailer, price, order_time))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM clothes WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, clothes, customer, retailer, price, order_time):
        self.cur.execute("UPDATE clothes SET clothes = ?, customer = ?, price = ?, order_time = ?, retailer = ? WHERE id = ?",
                         (clothes, customer, price, order_time, retailer, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()