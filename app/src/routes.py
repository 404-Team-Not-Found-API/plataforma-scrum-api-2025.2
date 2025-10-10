from flask import Blueprint, render_template, request
from .modulos.modulo1 import modulo1_perguntas

bp = Blueprint('routes', __name__)

@bp.route('/')
def homepage():
    return render_template("index.html")

@bp.route('/conteudo')
def conteudo():
    return render_template('conteudo.html') 


@bp.route('/modulo1')
def modulo1():
    return render_template('modulo1.html')


@bp.route('/modulo1s2')
def modulo1s2():
    return render_template('modulo1s2.html')

@bp.route('/modulos/<modulo_nome>', methods=['GET'])
def mostrar_modulo(modulo_nome):
    modulos = {
        "modulo1": modulo1_perguntas, 
    }
    perguntas = modulos.get(modulo_nome)
    if not perguntas:
        return "Módulo não encontrado", 404
    return render_template(
        "form_exercicio.html",
        titulo_formulario=f"{modulo_nome.capitalize()} Exercícios",
        descricao_formulario="Responda às perguntas.",
        perguntas=perguntas,
        modulo_nome=modulo_nome
    )

# Rota genérica de processamento de respostas
@bp.route('/exe_modulo/<modulo_nome>', methods=['POST'])
def exe_modulo(modulo_nome):
    modulos = {
        "modulo1": modulo1_perguntas
    }
    perguntas = modulos.get(modulo_nome)
    if not perguntas:
        return "Módulo não encontrado", 404

    respostas = request.form
    pontuacao = 0
    for i, pergunta in enumerate(perguntas, start=1):
        resposta = respostas.get(f"resposta_{i}")
        if resposta and int(resposta) == pergunta["correta"]:
            pontuacao += 1

    return render_template("resultado.html", pontuacao=pontuacao, total=len(perguntas))
