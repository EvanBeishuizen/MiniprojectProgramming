__author__ = 'Dennis'

import sqlite3
import os

class database(object):

    def __init__(self, db):
        self.db = db
        self.setup()

    def setup(self):
        self.checkIfDatabaseExists()

    def checkIfDatabaseExists(self):
        if os.path.isfile(self.db) == False:
            self.create_db()

    def create_db(self):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute("Create table reisgegevens('reisID' INTEGER PRIMARY KEY AUTOINCREMENT, 'naam' TEXT, 'ov_nummer' INTEGER, 'beginstation' TEXT, 'eindstation' TEXT)")
        conn.commit()
        conn.close()

    def insert_traveldata(self, naam, ov_nummer, beginstation, eindstation):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute("INSERT into reisgegevens(naam,ov_nummer,beginstation,eindstation) values(?,?,?,?)",(naam,ov_nummer,beginstation,eindstation))
        conn.commit()

    def get_travelID(self,ov_nummer):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute('''SELECT reisID from reisgegevens where ov_nummer = ?''', (ov_nummer,))
        return c.fetchall()[-1][0]


    def get_traveldata(self,ov_nummer):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute('''SELECT reisID, ov_nummer, naam, beginstation, eindstation from reisgegevens where ov_nummer = ?''', (ov_nummer,))
        return c.fetchall()

    def get_countOV(self):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute('''SELECT ov_nummer, count(ov_nummer) from reisgegevens group by ov_nummer''')
        return c.fetchall()

    def get_countBS(self):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute('''SELECT beginstation, count(beginstation)from reisgegevens group by beginstation''')
        return c.fetchall()

    def get_countES(self):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute('''SELECT eindstation, count(eindstation)from reisgegevens group by eindstation''')
        return c.fetchall()





