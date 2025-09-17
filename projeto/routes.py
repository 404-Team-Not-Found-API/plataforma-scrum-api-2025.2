from projeto import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/conteudo')
def conteudo():
    return render_template('conteudo.html') 