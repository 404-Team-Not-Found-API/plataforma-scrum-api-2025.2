from projeto import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/conteudo')
def conteudo():
    return render_template('conteudo.html') 

@app.route('/conteudo/modulo1')
def modulo1():
    return render_template('modulo1.html') 