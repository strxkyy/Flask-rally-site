import sqlite3 #banco de dados embutido 
from flask import Flask  #flask e funçoes necessarias

con = sqlite3.connect("pilotos.db")

cursor = con.cursor()

cursor.execute("""insert into pilotos (nome,carro) values (?,?)
               """, ("Colin Mcrae","Subaru inprenza wrx Sti")) #inserindo piloto e carro no arquivo de banco de dados

con.commit() #codigo que faz a conexão apos o comando anterior e envia a inserção para o banco de dados 