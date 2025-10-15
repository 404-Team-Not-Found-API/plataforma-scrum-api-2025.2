from flask import Blueprint, render_template, request, session, redirect, url_for
from .modulos.modulo1 import modulo1_perguntas
from .modulos.modulo2 import modulo2_perguntas

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

@bp.route('/modulo1s2', methods=['GET', 'POST'])
def modulo1s2():
    return exercicio(
        modulo_nome="modulo1",
        template_name="modulo1s2.html",
        redirect_endpoint='routes.modulo1s2'
    )


@bp.route('/modulos/<modulo_nome>', methods=['GET'])
def mostrar_modulo(modulo_nome):
    modulos = {
        "modulo1": modulo1_perguntas,
        "modulo2": modulo2_perguntas
    }
    perguntas = modulos.get(modulo_nome)
    if not perguntas:
        return "Módulo não encontrado", 404

    session['current_index'] = 0
    session['acertos'] = 0
    session['modulo_nome'] = modulo_nome
    session['respostas'] = {}

    return redirect(url_for('routes.exercicio', modulo_nome=modulo_nome))


@bp.route('/exercicio/<modulo_nome>', methods=['GET', 'POST'])
def exercicio(modulo_nome, template_name="form_exercicio.html", redirect_endpoint=None):
    if redirect_endpoint is None:
        redirect_endpoint = 'routes.exercicio'

    modulos = {
        "modulo1": modulo1_perguntas,
        "modulo2": modulo2_perguntas
    }
    perguntas = modulos.get(modulo_nome)
    if not perguntas:
        return "Módulo não encontrado", 404

    force_start = request.args.get('start', 'false').lower() == 'true'

    if force_start or 'modulo_nome' not in session or session['modulo_nome'] != modulo_nome:
        session['current_index'] = 0
        session['acertos'] = 0
        session['modulo_nome'] = modulo_nome
        session['respostas'] = {}
        session['acertos_contados'] = []

    current_index = session.get('current_index', 0)
    acertos = session.get('acertos', 0)
    respostas = session.get('respostas', {})
    total = len(perguntas)
    pergunta = perguntas[current_index]

    feedback = None
    correta = False
    explicacao = ""
    resposta_usuario = respostas.get(str(current_index))

    if request.method == 'POST':
        if 'prev' in request.form:
            if current_index > 0:
                session['current_index'] = current_index - 1
            return redirect(url_for(redirect_endpoint, modulo_nome=modulo_nome, _anchor='secao-exercicios'))

        elif 'next' in request.form:
            if current_index + 1 < len(perguntas):
                session['current_index'] = current_index + 1
                return redirect(url_for(redirect_endpoint, modulo_nome=modulo_nome, _anchor='secao-exercicios'))
            else:
                pontuacao = session.get('acertos', 0)
                session.clear()
                return render_template(
                    template_name,
                    quiz_finalizado=True,
                    pontuacao=pontuacao,
                    total=total,
                    modulo_nome=modulo_nome)

        elif 'confirm' in request.form:
            resposta_str = request.form.get('resposta')
            if resposta_str:
                try:
                    resposta = int(resposta_str)
                except ValueError:
                    resposta = None
 
                respostas[str(current_index)] = resposta
                session['respostas'] = respostas
 
                resposta_usuario = resposta
                correta = (resposta == pergunta["correta"])
                feedback = "Correto!" if correta else "Incorreto!"
                explicacao = pergunta.get("explicacao", "Revise o conceito e tente novamente.")
 
                if correta and str(current_index) not in session.get('acertos_contados', []):
                    session['acertos'] = acertos + 1
                    session.setdefault('acertos_contados', []).append(str(current_index))
            else:
                feedback = "Você precisa selecionar uma opção antes de continuar!"

    return render_template(
        template_name,
        pergunta=pergunta,
        current_index=current_index,
        total=total,
        feedback=feedback,
        correta=correta,
        explicacao=explicacao,
        resposta_usuario=resposta_usuario
    )
