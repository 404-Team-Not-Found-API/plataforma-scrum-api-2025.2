# api/modulos/modulo1.py

# Mantemos a lista de perguntas aqui para compatibilidade com routes.py
modulo1_perguntas = [
    {
        "pergunta": "O que é SCRUM?",
        "alternativas": [
            "Uma linguagem de programação para desenvolvimento Web.",
            "Uma metodologia Ágil para gerenciar o desenvolvimento de produtos complexos.",
            "Um tipo de banco de dados.",
            "Uma ferramenta de design gráfico."
        ],
        "correta": 2,
        "explicacao": "O Scrum é uma estrutura ágil e leve, ideal para gerenciar o desenvolvimento de qualquer produto complexo."
    },
    {
        "pergunta": "Qual dos seguintes não é um pilar fundamental do Scrum mencionado mencionado no site?",
        "alternativas": [
            "Agilidade.",
            "Coletividade.",
            "Eficiência.",
            "Lucratividade."
        ],
        "correta": 4,
        "explicacao": "Os três pilares mencionados são: Agilidade, Coletividade e Eficiência.Lucratividade não é um dos pilares fundamentais apresentados."
    },
    {
        "pergunta": "Qual o principal benefício da Agilidade no Scrum?",
        "alternativas": [
            "Reduzir custos de infraestrutura.",
            "Responder rapidamente ás mudanças e entregar valor continuamente.",
            "Eliminar a necessidade de documentação.",
            "Trabalhar em planejamento."
        ],
        "correta": 2,
    "explicacao": "A agilidade permite responder rapidamente às mudanças e entregar valor continuamente ao cliente."
    },
    {
        "pergunta": "Como funciona a coletividade no Scrum?",
        "alternativas": [
            "Apenas o gerente toma a decisões.",
            "Cada membro trabalha isoladamente.",
            "Times auto-organizados trabalhando de forma coletiva.",
            "Scrum Master define todas as tarefas de cada pessoa do time de desenvolvimento."
        ],
        "correta": 3,
        "explicacao": "A Coletividade no Scrum é baseada em times auto-organizados que trabalham de forma colaborativa."
    },
    {
        "pergunta": "O que significa a Eficiência no contexto do Scrum?",
        "alternativas": [
            "Trabalhar mais horas por dia.",
            "Contratar mais funcionários.",
            "Maximizar a produtividade e minimizar desperdícios no processo.",
            "Reduzir a qualidade para entregar mais rápido."
        ],
        "correta": 3,
        "explicacao": "Eficiência siginifica maximizar a produtividade e minimizar desperdícios no processo, mantendo a qualidade."
    },
    {
        "pergunta": "Qual característica melhor define o Scrum?",
        "alternativas": [
            "Rígido e flexível.",
            "Poderoso, leve e adaptável.",
            "Complexo e burocrático.",
            "Exclusivo para empresas."
        ],
        "correta": 2,
        "explicacao": "O Scrum é uma estrutura poderosa e leve, ideal para gerenciar o desenvolvimento de produtos complexos com flexibilidade."
    },
    {
        "pergunta": "Qual benefício da flexibilidade no Scrum?",
        "alternativas": [
            "Não precisar seguir nenhuma regra.",
            "Adaptar-se rapidamente ás mundanças.",
            "Evitar qualquer tipo de planejamento.",
            "Trabalhar sem objetivos definidos."
        ],
        "correta": 2,
        "explicacao": "A flexibilidade permite que as equipes se adaptem rapidamente ás mudanças de requisitos e prioridades."
    },
    {
        "pergunta": "O que significa 'Entrega de Valor' no Scrum?",
        "alternativas": [
            "Entregar o produto apenas no final do projeto.",
            "Focar apenas em lucros financeiros.",
            "Produzir resultados concretos e contínuos.",
            "Trabalhar sem metas específicas."
        ],
        "correta": 3,
        "explicacao": "Entrega de Valor no Scrum significa produzir resultados concretos e contínuos que agregam valor ao cliente."
    }
]

def get_modulo1():
    return {
        'sections': {
            'modulo1': {
                'titulo_modulo': 'Valores e Princípios: Manifesto Ágil',
                'numero_modulo': 1,
                'numero_secao': 1,
                'descricao_secao': 'Nada melhor do que aprender sobre o surgimento do "Manifesto Ágil" e seus princípios do que com uma história ilustrada, não é mesmo? Se após a leitura da história você ainda quiser um documento contendo todo o conteúdo desse módulo no formato padrão, fique tranquilo, é só baixar o PDF anexado ao final da página.',
                'titulo_complementar': 'VALORES E PRINCÍPIOS DO MANIFESTO ÁGIL',
                'conteudo_complementar': True,
                'url_download_complementar': 'routes.download',
                'url_download_key': 'modulo1_secao1',
                'url_anterior': None,
                'url_proximo': 'routes.module_route',
                'url_proximo_params': {'module_name': 'modulo1', 'section_name': 'modulo1s2'},
                'mostrar_exercicios': False,
                'template': 'modulo1.html'
            },
            'modulo1s2': {
                'titulo_modulo': 'Scrum: Valores e Princípios',
                'numero_modulo': 1,
                'numero_secao': 2,
                'descricao_secao': 'Trata-se de um framework para desenvolver e manter produtos complexos. Além de ser utilizado no campo do desenvolvimento, pode ser aplicado em outras áreas, devido à sua natureza interativa e incremental.',
                'conteudo_complementar': True,
                'titulo_complementar': 'SCRUM: VALORES E PRINCÍPIOS',
                'url_download_complementar': 'routes.download',
                'url_download_key': 'modulo1_secao2',
                'url_anterior': 'routes.module_route',
                'url_proximo': 'routes.module_route',  # Próximo módulo quando concluído
                'url_anterior_params': {'module_name': 'modulo1', 'section_name': 'modulo1'},
                'url_proximo_params': {'module_name': 'modulo2', 'section_name': 'modulo2'},
                'mostrar_exercicios': True,
                'template': 'modulo1s2.html'
            }
        },
        'quiz': True,
        'primeira_secao': 'modulo1'
    }