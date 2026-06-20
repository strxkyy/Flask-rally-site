import sqlite3 #banco de dados embutido 
from flask import Flask,redirect,render_template,get_flashed_messages  #flask e funçoes necessarias

con = sqlite3.connect("usuario.db")

cursor = con.cursor()

cursor.execute("""""")

con.commit() 

site = Flask(__name__)

@site.route("/") # rota de entrada inicial/verificação do site 
def verificacao_usuario(): #necessario definir uma função,necessaria para retornar o comando "render_template" que ira executar nosso arquivo .html na pasta templates
    return render_template("verificacao.html")

site.run(debug=True)



