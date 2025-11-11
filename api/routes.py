from flask import Blueprint, render_template, request, session, redirect, url_for, send_from_directory, jsonify, Response
from .modulos.modulo1 import modulo1_perguntas
from .modulos.modulo2 import modulo2_perguntas
from .modulos.modulo3 import modulo3_perguntas
from .modulos.modulo4 import modulo4_perguntas
from .modulos.config import MODULES_CONFIG, DOWNLOADS
import os
import requests
import time


# Mapeamento centralizado de módulos para as perguntas
perguntas_modulos = {
    'modulo1': modulo1_perguntas,
    'modulo2': modulo2_perguntas,
    'modulo3': modulo3_perguntas,
    'modulo4': modulo4_perguntas,
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

    # ALTERAÇÃO AJAX: A condição foi simplificada. Se a seção deve mostrar exercícios,
    # a função 'exercicio' é chamada para renderizar o estado inicial do quiz.
    if module_config.get('quiz') and section_config.get('mostrar_exercicios', False):
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

@bp.route('/gerar-relatorio-pdf-modulo6', methods=['POST'])
def gerar_relatorio_modulo6():
    # 1. Obter chaves da API a partir das variáveis de ambiente
    public_key = os.environ.get('ILOVEPDF_PUBLIC_KEY')
    secret_key = os.environ.get('ILOVEPDF_SECRET_KEY')

    # 2. Autenticar e obter token de acesso
    auth_response = requests.post('https://api.ilovepdf.com/v1/auth', data={'public_key': public_key, 'secret_key': secret_key})
    if auth_response.status_code != 200:
        return jsonify({'error': 'Falha na autenticação com a API iLovePDF'}), 500
    token = auth_response.json()['token']
    headers = {'Authorization': f'Bearer {token}'}

    # 3. Iniciar a tarefa 'htmlpdf'
    start_response = requests.get('https://api.ilovepdf.com/v1/start/htmlpdf', headers=headers)
    if start_response.status_code != 200:
        return jsonify({'error': 'Falha ao iniciar a tarefa na API iLovePDF'}), 500
    task_data = start_response.json()
    task_id = task_data['task']
    server_url = f"https://{task_data['server']}"

    # 4. Preparar o HTML para upload
    form_data = request.get_json()
    from datetime import datetime
    html_content = render_template('relatorio_modulo6.html',
                                   meta_sprint=form_data.get('meta_sprint', ''),
                                   backlog_itens=form_data.get('backlog_itens', ''),
                                   riscos=form_data.get('riscos', ''),
                                   data_atual=datetime.now().strftime('%d/%m/%Y'))

    # 5. Enviar o HTML para a API
    files = {'file': ('report.html', html_content, 'text/html')}
    upload_response = requests.post(f'{server_url}/v1/upload', headers=headers, data={'task': task_id}, files=files)
    if upload_response.status_code != 200:
        return jsonify({'error': 'Falha no upload do HTML para a API iLovePDF'}), 500
    server_filename = upload_response.json()['server_filename']

    # 6. Processar o arquivo (converter HTML para PDF)
    process_payload = {
        'task': task_id,
        'tool': 'htmlpdf',
        'files': [{'server_filename': server_filename, 'filename': 'relatorio.html'}]
    }
    process_response = requests.post(f'{server_url}/v1/process', headers=headers, json=process_payload)
    if process_response.status_code != 200:
        return jsonify({'error': 'Falha no processamento do arquivo na API iLovePDF'}), 500

    # 7. Baixar o PDF resultante
    download_url = f'{server_url}/v1/download/{task_id}'
    
    # Loop para aguardar o processamento (opcional, mas recomendado)
    for _ in range(10): # Tenta por até 10 segundos
        download_response = requests.get(download_url, headers=headers, stream=True)
        if download_response.status_code == 200:
            break
        time.sleep(1)
    else:
        return jsonify({'error': 'Tempo de processamento excedido na API iLovePDF'}), 500

    # 8. Enviar o PDF para o usuário
    return Response(download_response.content,
                    mimetype='application/pdf',
                    headers={'Content-Disposition': 'attachment;filename=relatorio_planejamento_sprint.pdf'})


# NOVA ROTA: Esta é a nova rota de API.
# Ela recebe a resposta do usuário via JSON, processa a lógica de verificação e pontuação,
# e retorna um JSON com o feedback e os dados da próxima pergunta (ou o resultado final).
# Isso permite que o frontend se atualize sem recarregar a página.
@bp.route('/verificar-resposta/<module_name>', methods=['POST'])
def verificar_resposta(module_name):
    data = request.get_json()
    question_index = int(data['question_index'])
    user_answer = int(data['answer'])

    perguntas = perguntas_modulos.get(module_name)
    if not perguntas:
        return jsonify({'error': 'Módulo não encontrado'}), 404

    total_questions = len(perguntas)
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
        'explanation': pergunta_atual.get('explicacao', 'Explicação não disponível.'),
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


# A função 'exercicio' agora só lida com requisições 'GET'.
# Sua única responsabilidade é carregar a primeira pergunta do quiz e limpar a pontuação da sessão anterior, preparando para a interação via JavaScript.
@bp.route('/exercicio/<modulo_nome>', methods=['GET'])
def exercicio(modulo_nome, template_name="form_exercicio.html", section_name=None, template_data=None, **kwargs):
    perguntas = perguntas_modulos.get(modulo_nome)
    if not perguntas:
        return "Módulo não encontrado", 404

    # Limpa o score da sessão anterior para garantir um novo começo a cada vez que o quiz é carregado.
    session.pop('score', None)

    # A lógica agora sempre começa da primeira pergunta
    current_index = 0
    total = len(perguntas)
    pergunta = perguntas[current_index]

    return render_template(
        template_name,
        pergunta=pergunta,
        current_index=current_index,
        total=total,
        **(template_data or {})
    )
                                    