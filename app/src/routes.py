from flask import Blueprint, render_template, request, session, redirect, url_for
from .modulos.modulo1 import modulo1_perguntas
from .modulos.modulo2 import modulo2_perguntas

bp = Blueprint('routes', __name__)

# Rotas básicas
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


# Mostra o módulo e inicia sessão
@bp.route('/modulos/<modulo_nome>', methods=['GET'])
def mostrar_modulo(modulo_nome):
    modulos = {
        "modulo1": modulo1_perguntas,
        "modulo2": modulo2_perguntas  # ← módulo 2 adicionado
    }
    perguntas = modulos.get(modulo_nome)
    if not perguntas:
        return "Módulo não encontrado", 404

    # Inicia progresso e respostas
    session['current_index'] = 0
    session['acertos'] = 0
    session['modulo_nome'] = modulo_nome
    session['respostas'] = {}  # Guarda respostas do usuário

    return redirect(url_for('routes.exercicio', modulo_nome=modulo_nome))


# Mostra perguntas do módulo
@bp.route('/exercicio/<modulo_nome>', methods=['GET', 'POST'])
def exercicio(modulo_nome):
    modulos = {
        "modulo1": modulo1_perguntas,
        "modulo2": modulo2_perguntas
    }
    perguntas = modulos.get(modulo_nome)
    if not perguntas:
        return "Módulo não encontrado", 404

    current_index = session.get('current_index', 0)
    acertos = session.get('acertos', 0)
    respostas = session.get('respostas', {})
    total = len(perguntas)
    pergunta = perguntas[current_index]

    feedback = None
    correta = False
    explicacao = ""
    resposta_usuario = respostas.get(str(current_index))  # resposta já salva

    if request.method == 'POST':
        # Botão "Anterior"
        if 'prev' in request.form:
            if current_index > 0:
                session['current_index'] = current_index - 1
            return redirect(url_for('routes.exercicio', modulo_nome=modulo_nome))

        # Botão "Confirmar"
        resposta_str = request.form.get('resposta')
        if resposta_str:
            try:
                resposta = int(resposta_str)
            except ValueError:
                resposta = None

            # Salva resposta
            respostas[str(current_index)] = resposta
            session['respostas'] = respostas

            resposta_usuario = resposta
            correta = (resposta == pergunta["correta"])
            feedback = "Correto!" if correta else "Incorreto!"
            explicacao = pergunta.get("explicacao", "Revise o conceito e tente novamente.")

            if correta:
                acertos += 1
                session['acertos'] = acertos
        else:
            feedback = "Você precisa selecionar uma opção antes de continuar!"

        # Botão "Próxima" só funciona se houver feedback
        if 'next' in request.form and feedback:
            if current_index + 1 < len(perguntas):
                session['current_index'] = current_index + 1
                return redirect(url_for('routes.exercicio', modulo_nome=modulo_nome))
            else:
                return redirect(url_for('routes.resultado', modulo_nome=modulo_nome))

    # Renderiza pergunta atual
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
        "modulo1": modulo1_perguntas,
        "modulo2": modulo2_perguntas
    }
    total = len(modulos[modulo_nome])
    session.clear()  # limpa progresso para reiniciar
    return render_template(
        "resultado.html",
        pontuacao=acertos,
        total=total,
        modulo_nome=modulo_nome  # necessário para o botão "Refazer Exercícios"
    )
