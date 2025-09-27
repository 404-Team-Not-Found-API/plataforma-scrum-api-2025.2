from flask import render_template, url_for, Blueprint

bp = Blueprint('routes', __name__)

@bp.route('/')
def homepage():
    return render_template("index.html")

@bp.route('/conteudo')
def conteudo():
    return render_template('conteudo.html') 


@bp.route('/conteudo/modulo1')
def modulo1():
    return render_template('modulo1.html')


@bp.route('/conteudo/modulo1/modulo1s2')
def modulo1s2():
    return render_template('modulo1s2.html')

