import sqlite3 #banco de dados embutido 
from flask import Flask,redirect,render_template,get_flashed_messages, request #flask e funçoes necessarias

con = sqlite3.connect("usuario.db")

cursor = con.cursor()

cursor.execute("""""")

con.commit() 

site = Flask(__name__)

@site.route("/", methods=["get","post"])
def login():
    return render_template("login.html")

@site.route("/verificacao", methods=["get","post"]) 
def verificacao_usuario(): 
    nome = request.form.get("nome")
    senha = request.form.get("senha")

    con = sqlite3.connect("usuario.db")
    cursor = con.cursor()

    cursor.execute("select * from usuario where nome = ? and senha = ?",
    (nome,senha))

    usuario = cursor.fetchone()

    con.close()

    if usuario:
    
     return render_template("login.html")
    
    else:
    
     return render_template("home.html") 


site.run(debug=True)



