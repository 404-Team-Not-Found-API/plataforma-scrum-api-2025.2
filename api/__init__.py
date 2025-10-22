from flask import Flask
from .routes import bp as routes_bp  

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.secret_key = "chave-super-secreta"
    app.register_blueprint(routes_bp)
    return app

app = create_app()
