# api/modulos/modulo6.py

# O Módulo 6 não tem questionário no estilo padrão, é uma simulação.
# Mantemos a lista vazia ou definimos algo se necessário futuramente.
modulo6_perguntas = []

def get_modulo6():
    """
    Retorna os dados para a simulação da Sprint (Módulo 6).
    Estrutura focada em fases da simulação.
    """
    return {
        "sections": {
            "modulo6": {
                "titulo_modulo": "Módulo Final: Sua Primeira Sprint",
                "numero_modulo": 6,
                "descricao_secao": "Vamos colocar a mão na massa. Defina a visão, crie o backlog e gere seu documento.",
                'url_anterior': 'routes.module_route',
                'url_anterior_params': {'module_name': 'modulo4', 'section_name': 'modulo4'},
                'conteudo_complementar': False,
                'mostrar_exercicios': False,
                "template": "modulo6.html",
                "cards": [
                    {
                        "id": "visao",
                        "titulo": "1. Defina a Visão do Produto",
                        "dicas": [
                            "Comece pequeno - um projeto de 1-2 semanas.",
                            "Foque na dor real do usuário.",
                            "Seja específico no público-alvo."
                        ],
                        "campos": [
                            {"id": "nome_projeto", "label": "Nome do Projeto", "tipo": "input", "placeholder": "Ex: Sistema de Gestão de Tarefas"},
                            {"id": "publico_alvo", "label": "Para quem? (Público-alvo)", "tipo": "textarea", "placeholder": "Quem vai usar seu produto?"},
                            {"id": "necessidade", "label": "Qual a necessidade?", "tipo": "textarea", "placeholder": "Qual problema ele resolve?"}
                        ]
                    },
                    {
                        "id": "backlog",
                        "titulo": "2. Crie o Product Backlog",
                        "dicas": [
                            "Priorize pelo valor de negócio.",
                            "Quebre grandes tarefas em menores."
                        ],
                        "campos": [
                            {"id": "back_item_1", "label": "Item de Alta Prioridade", "tipo": "input", "placeholder": "Funcionalidade principal..."},
                            {"id": "estimativa_1", "label": "Estimativa", "tipo": "input", "placeholder": "Ex: 3 dias"},
                            {"id": "back_item_2", "label": "Item de Média Prioridade", "tipo": "input", "placeholder": "Funcionalidade secundária..."},
                            {"id": "back_item_3", "label": "Item de Baixa Prioridade", "tipo": "input", "placeholder": "Funcionalidade secundária..."}
                        ]
                    }
                ]
            }
        },
        "quiz": False, # Este módulo não usa o sistema de quiz padrão
        "primeira_secao": "modulo6"
    }