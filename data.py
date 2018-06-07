#!/usr/bin/python
from database import Database
import datetime
import os

class Data:
    db = Database()

    def get(self):
        conn = self.db.connect()
        psql = conn.cursor()
        psql2 = conn.cursor()
        os.system('clear')
        psql.execute(""" SELECT * FROM data ORDER BY id DESC LIMIT 1 """)
        now = datetime.datetime.now().time()
        data = {}
        data['relay'] = False;
        data['relay_main'] = False;
        data['temperature'] = 23;
        for row in psql.fetchall():
            data['relay'] = (row[3] < now and row[4] > now)
            data['relay_main'] = (row[1] < now and row[2] > now)
            data['temperature'] = row[5]
        return data

    def log_realtime(self):
        conn = self.db.connect()
        psql = conn.cursor()
        #os.system('clear')
        psql.execute(""" SELECT * FROM data ORDER BY id DESC LIMIT 1 """)
        now = datetime.datetime.now().time()
        print("________________________________________________")
        print("|\t\tDatos\t\t\t\t|")
        for row in psql.fetchall():
            print("-------------------------------------------------")
            print("Perfil: " + str(row[6]) + " (" + str(row[8]) + ")")
            #print("Descripción: " + str(row[7]))
            print("relay: " + str(row[3] < now and row[4] > now))
            print("relay_main: " + str(row[1] < now and row[2] > now))
            print("temperature_ideal: " + str(row[5]))
        print("-------------------------------------------------")
