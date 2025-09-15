import sqlite3
from datetime import datetime


def create_table_parking():
    connection = sqlite3.connect("data_access/parking.db")
    connection.cursor().execute("create table if not exists parkings (id integer primary key autoincrement, name text, model text, plate text, color text, date_time text)")
    connection.commit()
    connection.close()

def save_parking(name, model, plate, color):
    connection = sqlite3.connect("data_access/parking.db")
    connection.cursor().execute("insert into parkings (name, model, plate, color, date_time) values (?, ?, ?, ?, ?)",
                   [name, model, plate, color, datetime.now()])
    connection.commit()
    connection.close()

    
