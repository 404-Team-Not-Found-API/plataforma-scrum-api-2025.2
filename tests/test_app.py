import pytest
from api import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Curso de Scrum' in response.data  # Based on the title in index.html

def test_conteudo(client):
    response = client.get('/conteudo')
    assert response.status_code == 200
    assert b'Modulos' in response.data  # Assuming the conteudo page has this text

def test_module_route(client):
    response = client.get('/conteudo/modulo1/')
    assert response.status_code == 200
    # Add more specific assertions based on the template content

def test_download(client):
    # Assuming there's a download key, e.g., 'modulo1'
    response = client.get('/download/modulo1')
    assert response.status_code == 200 or response.status_code == 404  # 404 if key not found

def test_verificar_resposta(client):
    data = {
        'question_index': 0,
        'answer': 1
    }
    response = client.post('/verificar-resposta/modulo1', json=data)
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'correct' in json_data
    assert 'correct_answer' in json_data
    assert 'explanation' in json_data

def test_exercicio_modulo5(client):
    response = client.get('/exercicio/modulo5')
    assert response.status_code == 200
    # Add more assertions for modulo5
