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
    # Passa as variáveis específicas do módulo para o template
    dados_secao = {
        'titulo_modulo': 'Valores e Princípios: Manifesto Ágil',
        'numero_modulo': 1,
        'numero_secao': 1,
        'descricao_secao': 'Nada melhor do que aprender sobre o surgimento do “Manifesto Ágil” e seus princípios do que com uma história ilustrada, não é mesmo? Se após a leitura da história você ainda quiser um documento contendo todo o conteúdo desse módulo no formato padrão, fique tranquilo, é só baixar o PDF anexado ao final da página.',
        'titulo_complementar': 'VALORES E PRINCÍPIOS DO MANIFESTO ÁGIL',
        'conteudo_complementar': True,
        'url_download_complementar': url_for('routes.download_modulo1_secao1'),
        'url_anterior': None,
        'url_proximo': url_for('routes.modulo1s2'),
        'mostrar_exercicios': False
    }
    return render_template('modulo1.html', **dados_secao)


@bp.route('/conteudo/modulo1/modulo1s2')
def modulo1s2():
    dados_secao = {
        'titulo_modulo': 'Scrum: Valores e Princípios',
        'numero_modulo': 1,
        'numero_secao': 2,
        'descricao_secao': 'Trata-se de um framework para desenvolver e manter produtos complexos. Além de ser utilizado no campo do desenvolvimento, pode ser aplicado em outras áreas, devido à sua natureza interativa e incremental.',
        'conteudo_complementar': True,
        'titulo_complementar': 'SCRUM: VALORES E PRINCÍPIOS',
        'url_download_complementar': url_for('routes.download_modulo1_secao2'),
        'url_anterior': url_for('routes.modulo1'),
        'url_proximo': url_for('routes.modulo2'), # Próximo módulo quando concluido
        'mostrar_exercicios': False
    }
    return render_template('modulo1s2.html', **dados_secao)

@bp.route('/conteudo/modulo2')
def modulo2():
    # Lista de cards para esta seção
    cards_secao = [
        {
            'titulo': 'Product Owner',
            'subtitulo': 'O Product Owner é o guardião da visão do produto e responsável por maximizar o valor do trabalho realizado pelo time.',
            'texto': 'A <b>transparência</b> assegura que todas as variáveis...<br>A <b>inspeção</b> dos processos deve ser feita...<br>Em relação à <b>adaptação</b>, o processo pode ser modificado...'
        },
        {
            'titulo': 'Product Owner',
            'subtitulo': 'O Product Owner é o guardião da visão do produto e responsável por maximizar o valor do trabalho realizado pelo time.',
            'texto': 'A <b>transparência</b> assegura que todas as variáveis...<br>A <b>inspeção</b> dos processos deve ser feita...<br>Em relação à <b>adaptação</b>, o processo pode ser modificado...'
        },
        {
            'titulo': 'Product Owner',
            'subtitulo': 'O Product Owner é o guardião da visão do produto e responsável por maximizar o valor do trabalho realizado pelo time.',
            'texto': 'A <b>transparência</b> assegura que todas as variáveis...<br>A <b>inspeção</b> dos processos deve ser feita...<br>Em relação à <b>adaptação</b>, o processo pode ser modificado...'
        },
    ]
    dados_secao = {
        'titulo_modulo': 'Os Papéis e as Interações',
        'numero_modulo': 2,
        'descricao_secao': 'Descubra os três papéis fundamentais do Scrum e como eles trabalham juntos para criar valor',
        'conteudo_complementar': False,
        'url_anterior': url_for('routes.modulo1s2'),
        'url_proximo': None,
        'mostrar_exercicios': True,
        'cards': cards_secao
    }
    return render_template('modulo2.html', **dados_secao)

@bp.route('/download/modulo1-secao1')
def download_modulo1_secao1():
    return send_from_directory('static/assets', 'Módulo 1 - Seção 1.pdf', as_attachment=True)

@bp.route('/download/modulo1-secao2')
def download_modulo1_secao2():
    return send_from_directory('static/assets', 'Módulo 1 - Seção 2.pdf', as_attachment=True)

