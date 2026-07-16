import sqlite3 #banco de dados embutido 
from flask import Flask,redirect,render_template, request,flash

con = sqlite3.connect("usuario.db")

cursor = con.cursor()

cursor.execute("""""")

con.commit() 

site = Flask(__name__)

site.secret_key = "TRUENO"

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

    resultado = cursor.fetchone()

    con.close()

    if resultado:
     return redirect("/home")
    
    else:
     flash("LOGIN OU USUARIO INCORRETOS!", "erro")
     return redirect("/")

@site.route("/home")
def home():
   return render_template("home.html")


site.run(debug=True)



