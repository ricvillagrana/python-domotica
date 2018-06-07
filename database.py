#!/usr/bin/python

import psycopg2

class Database:

    hostname = 'localhost'
    username = 'ricardo'
    password = '1234'
    database = 'domotica'

    def connect (self):
        try:
            return psycopg2.connect(host=self.hostname, user=self.username, password=self.password, dbname=self.database)
        except:
            print("Error al conectar con la base de datos " + database + " con el usuario " + username)
        return "Error"

    def close_cursor (self):
        psql.close()
        conn.close()