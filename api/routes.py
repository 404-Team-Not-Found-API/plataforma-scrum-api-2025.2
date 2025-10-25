from flask import Blueprint, render_template, request, session, redirect, url_for, send_from_directory
from .modulos.modulo1 import modulo1_perguntas
from .modulos.modulo2 import modulo2_perguntas
from .modulos.modulo3 import modulo3_perguntas
from .modulos.modulo4 import modulo4_perguntas
from .modulos.config import MODULES_CONFIG, DOWNLOADS

bp = Blueprint('routes', __name__)

@bp.route('/')
def homepage():
    return render_template("index.html")

@bp.route('/conteudo')
def conteudo():
    return render_template('conteudo.html', MODULES_CONFIG=MODULES_CONFIG)

@bp.route('/conteudo/<module_name>/', defaults={'section_name': None}, methods=['GET', 'POST'])
@bp.route('/conteudo/<module_name>/<section_name>', methods=['GET', 'POST'])
def module_route(module_name, section_name=None):
    if module_name not in MODULES_CONFIG:
        return "Module not found", 404

    module_config = MODULES_CONFIG[module_name]
    section_config = module_config['sections'].get(section_name or module_name, {})

    template_data = {
        'titulo_modulo': section_config.get('titulo_modulo', ''),
        'numero_modulo': section_config.get('numero_modulo', ''),
        'numero_secao': section_config.get('numero_secao', ''),
        'descricao_secao': section_config.get('descricao_secao', ''),
        'titulo_complementar': section_config.get('titulo_complementar'),
        'conteudo_complementar': section_config.get('conteudo_complementar', False),
        'url_download_complementar': url_for('routes.download', key=section_config.get('url_download_key')) if section_config.get('url_download_key') else None,
        'url_anterior': url_for(section_config.get('url_anterior'), **section_config.get('url_anterior_params', {})) if section_config.get('url_anterior') else None,
        'url_proximo': url_for(section_config.get('url_proximo'), **section_config.get('url_proximo_params', {})) if section_config.get('url_proximo') else None,
        'mostrar_exercicios': section_config.get('mostrar_exercicios', False),
        'quiz_available': module_config.get('quiz', False),
        'module_name': module_name, 
        'section_name': section_name, 
        'cards': section_config.get('cards', [])
    }

    template = section_config.get('template', f'{module_name}.html')

    if module_config.get('quiz') and (request.method == 'POST' or section_config.get('mostrar_exercicios', False)):
        return exercicio(
            modulo_nome=module_name,
            template_name=template,
            redirect_endpoint='routes.module_route',
            section_name=section_name,
            start_quiz=False,
            template_data=template_data
        )

    return render_template(template, **template_data)

@bp.route('/download/<key>')
def download(key):
    if key not in DOWNLOADS:
        return "File not found", 404
    filename = DOWNLOADS[key]
    return send_from_directory('static/assets', filename, as_attachment=True)


@bp.route('/exercicio/<modulo_nome>', methods=['GET', 'POST'])
def exercicio(modulo_nome, template_name="form_exercicio.html", redirect_endpoint=None, section_name=None, start_quiz=False, template_data=None):
    if redirect_endpoint is None:
        redirect_endpoint = 'routes.exercicio'

    modulos = {
        "modulo1": modulo1_perguntas,
        "modulo2": modulo2_perguntas,
        "modulo3": modulo3_perguntas,
        "modulo4": modulo4_perguntas
    }
    perguntas = modulos.get(modulo_nome)
    if not perguntas:
        return "Módulo não encontrado", 404

    force_start = request.args.get('start', 'false').lower() == 'true' or start_quiz

    if force_start or session.get('modulo_nome') != modulo_nome:
        session['current_index'] = 0
        session['acertos'] = 0
        session['modulo_nome'] = modulo_nome
        session['respostas'] = {}
        session['acertos_contados'] = []

    current_index = session.get('current_index', 0)
    acertos = session.get('acertos', 0)
    respostas_sessao = session.get('respostas', {})
    total = len(perguntas)
    pergunta = perguntas[current_index]

    feedback = None
    correta = False
    explicacao = ""
    resposta_usuario = respostas_sessao.get(str(current_index))

    if request.method == 'POST':
        if 'prev' in request.form:
            if current_index > 0:
                session['current_index'] = current_index - 1
            return redirect(url_for(redirect_endpoint, module_name=modulo_nome, section_name=section_name, _anchor='secao-exercicios'))

        elif 'next' in request.form:
            if current_index + 1 < len(perguntas):
                session['current_index'] = current_index + 1
                return redirect(url_for(redirect_endpoint, module_name=modulo_nome, section_name=section_name, _anchor='secao-exercicios'))
            else:
                pontuacao = session.get('acertos', 0)
                session.clear()
                return render_template(
                    template_name,
                    quiz_finalizado=True,
                    pontuacao=pontuacao,
                    total=total,
                    modulo_nome=modulo_nome,
                    redirect_endpoint=redirect_endpoint,
                    **(template_data or {}))

        elif 'confirm' in request.form:
            resposta_str = request.form.get('resposta')
            if resposta_str:
                try:
                    resposta = int(resposta_str)
                except ValueError:
                    resposta = None

                respostas_sessao[str(current_index)] = resposta
                session['respostas'] = respostas_sessao

                resposta_usuario = resposta
                correta = (resposta == pergunta["correta"])
                feedback = "Correto!" if correta else "Incorreto!"
                explicacao = pergunta.get("explicacao", "Revise o conceito e tente novamente.")

                if correta and str(current_index) not in session.get('acertos_contados', []):
                    session['acertos'] = acertos + 1
                    session.setdefault('acertos_contados', []).append(str(current_index))
                
            else:
                feedback = "Você precisa selecionar uma opção antes de continuar!"

            

    progress_percentage = int(((current_index + 1) / total * 100)) if total else 0

    return render_template(
        template_name,
        pergunta=pergunta,
        current_index=current_index,
        total=total,
        feedback=feedback,
        correta=correta,
        explicacao=explicacao,
        resposta_usuario=resposta_usuario,
        progress_percentage=progress_percentage,
        **(template_data or {})
    )
                                    