# api/modulos/modulo2.py

modulo2_perguntas = [
    {
        "pergunta": "Qual papel é responsável por priorizar o Product Backlog?",
        "alternativas": [
            "Scrum Master.",
            "Product Owner.",
            "Time de Desenvolvimento.",
            "Todos igualmente."
        ],
        "correta": 2,
        "explicacao": "O Product Owner é o responsável por criar e priorizar as tarefas do Product Backlog."
    },
    {
        "pergunta": "Quem é o responsável por facilitar os eventos do Scrum?",
        "alternativas": [
            "Product Owner.",
            "Time de desenvolvimento.",
            "Scrum Master.",
            "Gerente de projeto."
        ],
        "correta": 3,
        "explicacao": "O Scrum Master é o responsável por otimizar e adaptar o processo para que os eventos sejam entregues no tempo certo."
    },
    {
        "pergunta": "Qual característica define o time de desenvolvimento?",
        "alternativas": [
            "Hierarquia clara.",
            "Auto-organização.",
            "Especialização individual.",
            "Dependência externa."
        ],
        "correta": 2,
        "explicacao": "O time de desenvolvimento deve ser auto-organizado, sabendo cumprir seus objetivos individuais em colaboração com a equipe."
    }
]

def get_modulo2():
    return {
        'sections': {
            'modulo2': {
                'titulo_modulo': 'Os Papéis e as Interações',
                'numero_modulo': 2,
                'descricao_secao': 'Descubra os três papéis fundamentais do Scrum e como eles trabalham juntos para criar valor',
                'conteudo_complementar': True,
                'titulo_complementar': 'Montando a equipe: Os Papéis e as Interações',
                'url_download_complementar': 'routes.download',
                'url_download_key': 'modulo2',
                'url_anterior': 'routes.module_route',
                'url_anterior_params': {'module_name': 'modulo1', 'section_name': 'modulo1s2'},
                'url_proximo': 'routes.module_route',
                'url_proximo_params': {'module_name': 'modulo3', 'section_name': 'modulo3'},
                'mostrar_exercicios': True,
                'cards': [
                    {
                        'titulo': 'Product Owner',
                        'subtitulo': 'O product owner é o responsável pela visão do produto, pelo gerenciamento do backlog do produto e por garantir o valor do trabalho realizado pelo time.',
                        'texto': [
                            {'text': 'Principais Responsabilidades:', 'bold': True},
                            {'text': 'Gerenciar e priorizar o Backlog do Produto.'},
                            {'text': 'Garantir que o time entenda os itens do backlog.'},
                            {'text': 'Tomar decisões sobre o produto.'},
                            {'text': 'Aceitar ou rejeitar incrementos de trabalho.'},
                            {'text': 'Garantir que todo o backlog do produto seja visível, transparente e claro para todos os interessados, mostrando o que o time scrum deve buscar.'},
                            {'text': 'Habilidades essenciais:', 'bold': True},
                            {'text': 'Visão estratégica do produto.'},
                            {'text': 'Excelente comunicação.'},
                            {'text': 'Tomada de decisões.'},
                            {'text': 'Conhecimento do negócio.'},
                            {'text': 'Habilidades de negociação.'}
                        ],
                        'icon': 'File_Search.png',
                        'modal_icon': 'File_Search_az.png',
                        'bg_color': '#00AAFF' 
                    },
                    {
                        'titulo': 'Scrum Master',
                        'subtitulo': 'O scrum master é o responsável por garantir que o Scrum seja entendido e aplicado, para que o time scrum esteja aderindo aos valores do scrum, às práticas e às regras e aos princípios.',
                        'texto': [
                            {'text': 'Principais Responsabilidade:', 'bold': True},
                            {'text': 'Facilitar eventos do scrum.'},
                            {'text': 'Orientar o time em práticas ágeis.'},
                            {'text': 'Planejar implementações de scrum dentro da organização.'},
                            {'text': 'Treinar o time para ser mais produtivo.'},
                            {'text': 'Promover melhoria contínua.'},
                            {'text': 'Habilidades Essenciais:', 'bold': True},
                            {'text': 'Facilitação das reuniões.'},
                            {'text': 'Resolução de conflitos.'},
                            {'text': 'Mentor do time.'},
                            {'text': 'Conhecimento profundo do scrum.'},
                            {'text': 'Liderança.'}
                        ],
                        'icon': 'User_Voice.png',
                        'modal_icon': 'User_Voice_rx.png',
                        'bg_color': '#7200F8'   
                    },
                    {
                        'titulo': 'Equipe de Desenvolvimento',
                        'subtitulo': 'O time de desenvolvimento é responsável por executar o desenvolvimento e transformar o backlog do produto em incrementos de funcionalidade, criando um sistema pronto que possa ser entregue ao cliente.',
                        'texto': [
                            {'text': 'Principais Responsabilidades:', 'bold': True},
                            {'text': 'Criar incrementos de produto de alta qualidade.'},
                            {'text': 'Auto-organização das tarefas.'},
                            {'text': 'Estimar itens do backlog.'},
                            {'text': 'Colaborar para atingir os objetivos da Sprint.'},
                            {'text': 'Manter padrões técnicos elevados.'},
                            {'text': 'Habilidades Essenciais:', 'bold': True},
                            {'text': 'Habilidades técnicas variadas:'},
                            {'text': 'multidisciplinariedade e interdisciplinariedade.'},
                            {'text': 'Trabalho em equipe.'},
                            {'text': 'Auto-organização.'},
                            {'text': 'Comprometimento com qualidade.'},
                            {'text': 'Comunicação efetiva.'}
                        ],
                        'icon': 'Window_Terminal.png',
                        'modal_icon': 'Vector.png',
                        'bg_color': '#FF4141'   
                    }
                ],
                'template': 'modulo2.html'
            },
        },
        'quiz': True,
        'primeira_secao': 'modulo2'
    }