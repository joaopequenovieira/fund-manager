import sqlite3
import os
import fund_manager

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
            '''CREATE TABLE funds (ISIN TEXT,fund_name TEXT,nav TEXT,change TEXT);'''
        )

    def add_fund(self, link):
        #parametrized input to prevent SQL Injections
        #values 0=isin, 1=name, 2=nav, 3=change
        values = fund_manager.main_funcs.add_new_fund(link)
        self.db_cursor.execute('INSERT INTO funds VALUES (?, ?, ?, ?);', (values[0], values[1], values[2], values[3]))
        self.connection.commit()



if __name__ == '__main__':
    db = db_manager('fund_manager.db')
    db.load_database()
    db.add_fund("insert fund here")
    db.close()
    