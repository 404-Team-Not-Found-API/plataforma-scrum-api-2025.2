from flask import render_template, url_for

from projeto.src import app

@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/conteudo')
def conteudo():
    return render_template('conteudo.html') 

@app.route('/conteudo/modulo1')
def modulo1():
    return render_template('modulo1.html') 