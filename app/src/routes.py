from flask import Blueprint, render_template, request, session, redirect, url_for
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
        "modulo1": modulo1_perguntas
    }
    perguntas = modulos.get(modulo_nome)
    if not perguntas:
        return "Módulo não encontrado", 404

    # Salva progresso na sessão
    session['current_index'] = 0
    session['acertos'] = 0
    session['modulo_nome'] = modulo_nome

    return redirect(url_for('routes.exercicio', modulo_nome=modulo_nome))

# Mostra uma pergunta por vez
@bp.route('/exercicio/<modulo_nome>', methods=['GET', 'POST'])
def exercicio(modulo_nome):
    modulos = {
        "modulo1": modulo1_perguntas
      }
    perguntas = modulos.get(modulo_nome)
    if not perguntas:
        return "Módulo não encontrado", 404

    current_index = session.get('current_index', 0)
    acertos = session.get('acertos', 0)
    feedback = None
    correta = False
    explicacao = None
    resposta_usuario = None

    # Se usuário respondeu
    if request.method == 'POST':
        resposta = int(request.form.get('resposta', -1))
        pergunta = perguntas[current_index]
        correta = (resposta == pergunta["correta"])
        feedback = "Correto!" if correta else "Incorreto!"
        explicacao = pergunta.get("explicacao", "Revise o conceito e tente novamente.")

        if correta:
            acertos += 1
            session['acertos'] = acertos

        # Próxima questão se usuário clicar em "Próxima"
        if 'next' in request.form:
            if current_index + 1 < len(perguntas):
                session['current_index'] = current_index + 1
                return redirect(url_for('routes.exercicio', modulo_nome=modulo_nome))
            else:
                return redirect(url_for('routes.resultado', modulo_nome=modulo_nome))

    # Renderiza questão atual
    pergunta = perguntas[current_index]
    total = len(perguntas)
    return render_template(
        "form_exercicio.html",
        pergunta=pergunta,
        current_index=current_index,
        total=total,
        feedback=feedback,
        correta=correta,
        explicacao=explicacao,
        resposta_usuario=resposta_usuario  
    )

# Mostra resultado final
@bp.route('/resultado/<modulo_nome>')
def resultado(modulo_nome):
    acertos = session.get('acertos', 0)
    modulos = {
        "modulo1": modulo1_perguntas
    }
    total = len(modulos[modulo_nome])
    session.clear()
    return render_template("resultado.html", pontuacao=acertos, total=total)
