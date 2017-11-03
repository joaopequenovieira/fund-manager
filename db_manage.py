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
            '''CREATE TABLE funds (fund_link TEXT, ISIN TEXT,fund_name TEXT,nav TEXT,change TEXT);'''
        )

    def add_fund(self, link):
        #parametrized input to prevent SQL Injections
        #values 0=fund_link 1=isin, 2=name, 3=nav, 4=change
        values = fund_manager.main_funcs.add_new_fund(link)
        check_exists = self.db_cursor.execute('SELECT ISIN FROM funds WHERE ISIN =?;', (values[0],))
        for row in check_exists:
            if row[1] == values[0]:
                print("fund already exists")
                return


        self.db_cursor.execute('INSERT INTO funds VALUES (?, ?, ?, ?, ?);', (values[0], values[1], values[2], values[3], values[4]))
        self.connection.commit()

    def update_funds(self):
        target_funds = self.db_cursor.execute('SELECT fund_link FROM funds;')
        for row in target_funds:
            temp = fund_manager.main_funcs.add_new_fund(row[0])
            self.db_cursor.execute('UPDATE funds SET nav=?, change=? WHERE isin=?', (temp[3], temp[4], temp[1]))
            self.connection.commit()
            

    def retrieve_fund_data(self):
        self.update_funds()
        results = []
        for row in (self.db_cursor.execute(
            '''SELECT * FROM funds;'''
        )):
            results.append(row)
        return(results)


if __name__ == '__main__':
    db = db_manager('fund_manager.db')
    db.load_database()
    db.close()
    