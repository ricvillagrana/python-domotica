#!/usr/bin/python
from database import Database
import datetime
import os

class Temperature:
    db = Database()
    def add(self, new_temperature):
        conn = self.db.connect()
        psql = conn.cursor()
        now = datetime.datetime.now()
        try:
            #print("Insertando tu dato: {0}".format(new_temperature) )
            psql.execute("INSERT INTO {0} (temperature, created_at) VALUES({1}, '{2}')".format("temperature_logs", new_temperature, now))
            conn.commit()
        except:
            print("Hubo un problema al insertar tu dato: %s °C" % new_temperature )

    def log(self):
        conn = self.db.connect()
        psql = conn.cursor()
        psql.execute(""" SELECT * FROM temperature_logs """)
        print("\n_________________________________________")
        print("|\t\tDatos\t\t\t|")
        for row in psql.fetchall():
            print("----------------------------------------")
            print("\tTemperatura: " + str(row[0]) +" °C")
            print("\tFecha recabada: " + str(row[1]))
        print("----------------------------------------")

    def log_realtime(self):
        conn = self.db.connect()
        psql = conn.cursor()
        psql2 = conn.cursor()
        os.system('clear')
        psql.execute(""" SELECT * FROM temperature_logs ORDER BY created_at DESC LIMIT 1 """)
        psql2.execute(""" SELECT count(*) FROM temperature_logs """)
        print("________________________________________________")
        print("|\t\tDatos (" + str(psql2.fetchone()[0]) + " rows)\t\t|")
        for row in psql.fetchall():
            print("-------------------------------------------------")
            print("\tTemperatura: " + str(row[0]) +" °C")
            print("\tFecha recabada: " + str(row[1]))
        print("-------------------------------------------------")
