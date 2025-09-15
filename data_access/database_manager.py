import sqlite3
import datetime

parking_list = []

def create_table_parking():
    connection = sqlite3.connect("parking.db")
    connection.cursor().execute("create table parking (id integer primary key autoincrement, name text, model text, plate text, color text, datetime text)")
    connection.commit()
    connection.close()

def save_parking(name, model, plate, color, datetime):
    connection = sqlite3.connect("parking.db")
    connection.cursor().execute("insert into parking (name, model, plate, color, datetime) values (?, ?, ?, ?, ?)",
                   [name, model, plate, color, datetime])
    connection.commit()
    connection.close()

    
