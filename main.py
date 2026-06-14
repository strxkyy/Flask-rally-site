import sqlite3 #banco de dados embutido 
from flask import Flask  #flask e funçoes necessarias

con = sqlite3.connect("pilotos.db")

cursor = con.cursor()

cursor.execute("""create table if not exists pilotos (
               
        Id integer  primary key autoincrement,
        nome text not null unique,
        carro text not null  )""")