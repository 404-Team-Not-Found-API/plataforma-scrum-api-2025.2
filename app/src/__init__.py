from flask import Flask



def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.secret_key = 'chave-secreta'

    from .routes import bp as main_bp
    app.register_blueprint(main_bp)
    return app