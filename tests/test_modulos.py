import pytest
from api.modulos.modulo1 import modulo1_perguntas
from api.modulos.modulo2 import modulo2_perguntas
from api.modulos.modulo3 import modulo3_perguntas
from api.modulos.modulo4 import modulo4_perguntas
from api.modulos.modulo5 import modulo5_perguntas, verificar_respostas_modulo5

def test_modulo1_perguntas():
    assert isinstance(modulo1_perguntas, list)
    assert len(modulo1_perguntas) > 0
    for pergunta in modulo1_perguntas:
        assert 'pergunta' in pergunta
        assert 'alternativas' in pergunta
        assert 'correta' in pergunta
        assert isinstance(pergunta['alternativas'], list)
        assert len(pergunta['alternativas']) >= 2

def test_modulo2_perguntas():
    assert isinstance(modulo2_perguntas, list)
    assert len(modulo2_perguntas) > 0
    for pergunta in modulo2_perguntas:
        assert 'pergunta' in pergunta
        assert 'alternativas' in pergunta
        assert 'correta' in pergunta
        assert isinstance(pergunta['alternativas'], list)
        assert len(pergunta['alternativas']) >= 2

def test_modulo3_perguntas():
    assert isinstance(modulo3_perguntas, list)
    assert len(modulo3_perguntas) > 0
    for pergunta in modulo3_perguntas:
        assert 'pergunta' in pergunta
        assert 'alternativas' in pergunta
        assert 'correta' in pergunta
        assert isinstance(pergunta['alternativas'], list)
        assert len(pergunta['alternativas']) >= 2

def test_modulo4_perguntas():
    assert isinstance(modulo4_perguntas, list)
    assert len(modulo4_perguntas) > 0
    for pergunta in modulo4_perguntas:
        assert 'pergunta' in pergunta
        assert 'alternativas' in pergunta
        assert 'correta' in pergunta
        assert isinstance(pergunta['alternativas'], list)
        assert len(pergunta['alternativas']) >= 2

def test_modulo5_perguntas():
    assert isinstance(modulo5_perguntas, list)
    assert len(modulo5_perguntas) > 0
    for pergunta in modulo5_perguntas:
        assert 'pergunta' in pergunta
        assert 'alternativas' in pergunta
        assert 'id' in pergunta
        assert isinstance(pergunta['alternativas'], list)
        assert len(pergunta['alternativas']) >= 2

def test_verificar_respostas_modulo5():
    # Test with empty answers
    respostas_vazias = {}
    resultado = verificar_respostas_modulo5(respostas_vazias)
    assert 'tipo' in resultado
    assert resultado['tipo'] == 'diagnostico'
    assert 'feedback_geral' in resultado

    # Test with some answers
    respostas = {'question_1': 'a', 'question_2': 'b'}
    resultado = verificar_respostas_modulo5(respostas)
    assert 'tipo' in resultado
    assert resultado['tipo'] == 'diagnostico'
    assert 'feedback_geral' in resultado
    assert 'feedback_detalhado' in resultado
