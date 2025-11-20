from flask import Blueprint, render_template, request, session, redirect, url_for, send_from_directory, jsonify, Response
from .modulos.modulo1 import modulo1_perguntas
from .modulos.modulo2 import modulo2_perguntas
from .modulos.modulo3 import modulo3_perguntas
from .modulos.modulo4 import modulo4_perguntas
from .modulos.modulo5 import modulo5_perguntas, verificar_respostas_modulo5
from .modulos.config import MODULES_CONFIG, DOWNLOADS


# Mapeamento centralizado de módulos para as perguntas
perguntas_modulos = {
    'modulo1': modulo1_perguntas,
    'modulo2': modulo2_perguntas,
    'modulo3': modulo3_perguntas,
    'modulo4': modulo4_perguntas,
    'modulo5': modulo5_perguntas, 
}

bp = Blueprint('routes', __name__)

@bp.route('/')
def homepage():
    return render_template("index.html")

@bp.route('/conteudo')
def conteudo():
    return render_template('conteudo.html', MODULES_CONFIG=MODULES_CONFIG)

# A rota de conteúdo agora só aceita 'GET'.
# A lógica de 'POST' foi movida para uma API dedicada para evitar recarregamentos de página.
@bp.route('/conteudo/<module_name>/', defaults={'section_name': None}, methods=['GET'])
@bp.route('/conteudo/<module_name>/<section_name>', methods=['GET'])
def module_route(module_name, section_name=None):
    if module_name not in MODULES_CONFIG:
        return "Module not found", 404

    module_config = MODULES_CONFIG[module_name]
    # Garante que pega a seção correta ou a padrão
    section_key = section_name if section_name else module_config.get('primeira_secao', module_name)
    section_config = module_config['sections'].get(section_key, {})

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
        'cards': section_config.get('cards', []),
        # --- CORREÇÃO AQUI: Adicionamos 'conteudo' para o template acessar tudo ---
        'conteudo': module_config
    }

    template = section_config.get('template', f'{module_name}.html')

    # ALTERAÇÃO AJAX: A condição foi simplificada. Se a seção deve mostrar exercícios,
    # a função 'exercicio' é chamada para renderizar o estado inicial do quiz.
    if module_config.get('quiz') and section_config.get('mostrar_exercicios', False):
        # Lógica para separar o quiz do Módulo 5 dos demais
        if module_name == 'modulo5':
            return exercicio_modulo5(template_data=template_data)
        else:
            # Prepara os dados do quiz para os módulos 1-4 e os passa para o template do módulo
            perguntas = perguntas_modulos.get(module_name)
            if perguntas:
                session.pop('score', None)  # Limpa o score anterior
                template_data['perguntas'] = perguntas
                template_data['pergunta'] = perguntas[0]
                template_data['current_index'] = 0
                template_data['total'] = len(perguntas)
                template_data['total_questions'] = len(perguntas)

    return render_template(template, **template_data)

@bp.route('/download/<key>')
def download(key):
    if key not in DOWNLOADS:
        return "File not found", 404
    filename = DOWNLOADS[key]
    return send_from_directory('static/assets', filename, as_attachment=True)


# NOVA ROTA: Esta é a nova rota de API.
# Ela recebe a resposta do usuário via JSON, processa a lógica de verificação e pontuação,
# e retorna um JSON com o feedback e os dados da próxima pergunta (ou o resultado final).
# Isso permite que o frontend se atualize sem recarregar a página.
@bp.route('/verificar-resposta/<module_name>', methods=['POST'])
def verificar_resposta(module_name):
    data = request.get_json()
    question_index = int(data['question_index'])
    user_answer = data.get('answer')  # For modulo5, it's string like 'a', for others int
    action = data.get('action', 'check')  # Default to 'check', can be 'prev'

    perguntas = perguntas_modulos.get(module_name)
    if not perguntas:
        return jsonify({'error': 'Módulo não encontrado'}), 404

    total_questions = len(perguntas)

    if action == 'prev':
        # Handle going back to previous question
        prev_index = question_index
        if prev_index >= 0 and prev_index < len(perguntas):
            response_data = {
                'prev_question': perguntas[prev_index],
                'prev_question_index': prev_index,
                'total_questions': total_questions
            }
            return jsonify(response_data)
        else:
            return jsonify({'error': 'Invalid question index'}), 400

    if module_name == 'modulo5':
        # For modulo5, store answers in session
        if 'modulo5_answers' not in session:
            session['modulo5_answers'] = {}
        session['modulo5_answers'][f'question_{perguntas[question_index]["id"]}'] = user_answer
        session.modified = True

        next_question_index = question_index + 1
        response_data = {
            'next_question': None,
            'next_question_index': None,
            'total_questions': total_questions
        }

        if next_question_index < len(perguntas):
            # Se houver uma próxima pergunta, envia seus dados
            response_data['next_question'] = perguntas[next_question_index]
            response_data['next_question_index'] = next_question_index
        else:
            # Se for a última pergunta, compute the diagnostic result
            respostas = session.pop('modulo5_answers', {})
            resultado = verificar_respostas_modulo5(respostas)
            response_data['resultado'] = resultado

        return jsonify(response_data)
    else:
        # Original logic for other modules
        user_answer = int(user_answer)
        pergunta_atual = perguntas[question_index]
        is_correct = user_answer == pergunta_atual['correta']

        # Inicia o score na sessão se não existir
        if 'score' not in session:
            session['score'] = 0


        if is_correct:
            session['score'] += 1

        next_question_index = question_index + 1
        response_data = {
            'correct': is_correct,
            'correct_answer': pergunta_atual['correta'],
            'explanation': pergunta_atual.get('explicacao', ''),
            'next_question': None,
            'next_question_index': None,
            'total_questions': total_questions # Adicionado para o frontend
        }

        if next_question_index < len(perguntas):
            # Se houver uma próxima pergunta, envia seus dados
            response_data['next_question'] = perguntas[next_question_index]
            response_data['next_question_index'] = next_question_index
        else:
            # Se for a última pergunta, finaliza e envia o score
            response_data['score'] = session.pop('score', 0)
            response_data['total'] = total_questions

        return jsonify(response_data)

                                    
@bp.route('/exercicio/modulo5', methods=['GET', 'POST'])
def exercicio_modulo5(template_data=None):
    if template_data is None:
        template_data = MODULES_CONFIG['modulo5']['sections']['modulo5']
        template_data['module_name'] = 'modulo5'
        template_data['section_name'] = 'modulo5'

    resultado = None
    if request.method == 'POST':
        respostas = request.form.to_dict()
        resultado = verificar_respostas_modulo5(respostas)

    # Renderiza o template do Módulo 5, passando as perguntas e o resultado
    return render_template(
        'modulo5.html',
        perguntas=modulo5_perguntas,
        resultado=resultado,
        **template_data
    )
                                    