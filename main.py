import sqlite3 #banco de dados embutido 
from flask import Flask,redirect,render_template,get_flashed_messages  #flask e funçoes necessarias

con = sqlite3.connect("usuario.db")

cursor = con.cursor()

cursor.execute("""
               create table if not exists usuario
               
               (id integer PRIMARY KEY AUTOINCREMENT,
               nome text not null unique,
               senha text not null)
               """)  #criação da tabela de usuario para validação na rota html

con.commit() 

