import sqlite3 #banco de dados embutido 
from flask import Flask,redirect,render_template,get_flashed_messages  #flask e funçoes necessarias

con = sqlite3.connect("usuario.db")

cursor = con.cursor()

cursor.execute("""insert into usuario (nome,senha) values (?,?)
               """, ("gituser","62956")) #inserção de usuario para verificação da primeira rota 

con.commit() 

