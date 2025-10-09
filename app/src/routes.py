from flask import render_template, url_for, Blueprint, request
import importlib

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

@bp.route('/conteudo/<modulo_nome>')
def modulo(modulo_nome):
    try:
        modulo = importlib.import_module(f'src.modules.{modulo_nome}')
        dados = modulo.get_dados()
    except ModuleNotFoundError:
        return render_template('erro.html', mensagem=f'Módulo "{modulo_nome}" não encontrado.'), 404

    # Apenas renderiza o HTML do módulo
    template_modulo = f"{modulo_nome}.html"
    caminho = os.path.join("src", "templates", template_modulo)

    if os.path.exists(caminho):
        return render_template(template_modulo, **dados)
    else:
        return render_template("conteudo_generico.html", **dados)
    
@bp.route('/conteudo/<modulo_nome>/formulario', methods=['GET', 'POST'])
def formulario(modulo_nome):
    try:
        modulo = importlib.import_module(f'src.modules.{modulo_nome}')
        dados = modulo.get_dados()
    except ModuleNotFoundError:
        return render_template('erro.html', mensagem=f'Módulo "{modulo_nome}" não encontrado.'), 404

    resultado = None
    if request.method == 'POST':
        resposta = request.form.get('resposta')
        if resposta == dados['resposta_certa']:
            resultado = "✅ Resposta correta!"
        else:
            resultado = f"❌ Resposta incorreta. Resposta certa: {dados['resposta_certa']}"

    return render_template("form_exercicio.html", resultado=resultado, **dados)

