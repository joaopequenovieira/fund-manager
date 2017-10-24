import sqlite3
import os


class db_manager:

    def __init__(self,db_name):
        self.name = db_name
        self.connection = None
        self.db_cursor = None


    def load_database(self):
        if (os.path.exists(self.name)):
            self.connection = sqlite3.connect(self.name)
            self.db_cursor = self.connection.cursor()
        else:
            self.connection = sqlite3.connect(self.name)
            self.db_cursor = self.connection.cursor()
            db_manager.create_database(self)


    def close(self):
        self.connection.commit()
        self.connection.close()

    def create_database(self):
        self.db_cursor.execute(
            '''CREATE TABLE funds (ISIN TEXT,fund_name TEXT,nav INTEGER,change INTEGER);'''
        )

    def add_fund(self, isin, name, nav, change):
        #parametrized input to prevent SQL Injections
        self.db_cursor.execute('INSERT INTO funds VALUES (?, ?, ?, ?);', (isin,name,nav,change))


if __name__ == '__main__':
    db = db_manager('fund_manager.db')
    db.load_database()
    db.add_fund("isin_1", "fund_1", 50, 100)
    db.close()