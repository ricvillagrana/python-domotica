#!/usr/bin/python
from database import Database
import datetime
import os

class Led:
    db = Database()

    def get(self):
        conn = self.db.connect()
        psql = conn.cursor()
        psql2 = conn.cursor()
        os.system('clear')
        psql.execute(""" SELECT * FROM leds ORDER BY id DESC LIMIT 1 """)
        leds = {}
        leds['red'] = False;
        leds['blue'] = False;
        for row in psql.fetchall():
            leds['blue'] = row[1]
            leds['red'] = row[2]
        return leds

    def log_realtime(self):
        conn = self.db.connect()
        psql = conn.cursor()
        psql2 = conn.cursor()
        os.system('clear')
        psql.execute(""" SELECT * FROM leds ORDER BY id DESC LIMIT 1 """)
        psql2.execute(""" SELECT count(*) FROM temperature_logs """)
        print("________________________________________________")
        print("|\t\tDatos (" + str(psql2.fetchone()[0]) + " rows)\t\t|")
        for row in psql.fetchall():
            print("-------------------------------------------------")
            print("\tled_blue: " + str(row[1]))
            print("\tled_red: " + str(row[2]))
        print("-------------------------------------------------")
