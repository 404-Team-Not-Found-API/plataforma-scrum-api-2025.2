from flask import render_template, url_for, Blueprint, send_from_directory

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

@bp.route('/download/modulo1-secao1')
def download_modulo1_secao1():
    return send_from_directory('static/assets', 'Módulo 1 - Seção 1.pdf', as_attachment=True)

@bp.route('/download/modulo1-secao2')
def download_modulo1_secao2():
    return send_from_directory('static/assets', 'Módulo 1 - Seção 2.pdf', as_attachment=True)

