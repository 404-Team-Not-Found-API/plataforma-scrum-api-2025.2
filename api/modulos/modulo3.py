# Arquivo para o questionário do módulo 3

modulo3_perguntas = [
    {
        "pergunta": "Qual é o Time-Box (duração máxima) para uma Sprint?",
        "alternativas": [
            "15 dias corridos.",
            "Quatro semanas ou menos.",
            "Duas semanas, sem exceções.",
            "O tempo necessário para completar o Incremento."
        ],
        "correta": 2,
        "explicacao": "O Scrum Guide estabelece o ciclo de tempo fixo para consistência em um mês ou menos."
    },
    {
        "pergunta": "Qual é o principal resultado (artefato) e o objetivo definidos ao final do evento Sprint Planning?",
        "alternativas": [
            "O Product Backlog revisado e a Lista de Impedimentos.",
            "A Meta da Sprint e o Sprint Backlog.",
            "O Incremento Potencialmente Entregável e a Definição de Pronto (DoD).",
            "O Plano de Ação da Retrospectiva e o status do projeto."
        ],
        "correta": 2,
        "explicacao": "O Sprint Planning define o objetivo (Meta) da Sprint e o plano detalhado (Sprint Backlog) para alcançá-lo."
    },
    {
        "pergunta": "Qual é o Time-Box máximo e o foco primário do evento Daily Scrum?",
        "alternativas": [
            "30 minutos, focado em resolver impedimentos técnicos detalhadamente.",
            "15 minutos, focado em inspecionar o progresso para a Meta da Sprint e adaptar o plano das próximas 24 horas.",
            "15 minutos, focado em relatar o status do trabalho para o Product Owner.",
            "1 hora, focado em discutir a priorização dos itens do Product Backlog."
        ],
        "correta": 2,
        "explicacao": "O Daily Scrum é estritamente limitado a 15 minutos e é um evento de planejamento de 24 horas para o Time de Desenvolvimento."
    },
    {
        "pergunta": "Quem é a única pessoa com autoridade para cancelar uma Sprint?",
        "alternativas": [
            "O Time de Desenvolvimento, após votação unânime.",
            "O Scrum Master, após consultar o Product Owner.",
            "O Product Owner (PO).",
            "Os Stakeholders Chave, após demonstração do incremento."
        ],
        "correta": 3,
        "explicacao": "O Product Owner é o único responsável por maximizar o valor do produto e, portanto, o único com autoridade para cancelar a Sprint se a Meta se tornar obsoleta."
    },
    {
        "pergunta": "Qual é o principal resultado do evento Sprint Retrospective, que é implementado na próxima Sprint?",
        "alternativas": [
            "O Incremento Potencialmente Entregável.",
            "O Sprint Backlog, criado pelo Time de Desenvolvimento.",
            "Um plano de melhorias acionáveis para aumentar a eficácia e a qualidade.",
            "O Product Backlog Revisado, com novas prioridades."
        ],
        "correta": 3,
        "explicacao": "A Retrospectiva foca na melhoria contínua do processo do time, gerando ações para serem implementadas."
    },
    {
        "pergunta": "Qual evento Scrum tem como objetivo inspecionar o Incremento (o produto) e adaptar o Product Backlog (o plano de longo prazo)?",
        "alternativas": [
            "Daily Scrum.",
            "Sprint Retrospective.",
            "Sprint Planning.",
            "Sprint Review."
        ],
        "correta": 4,
        "explicacao": "O Sprint Review é o evento dedicado à demonstração e inspeção do Incremento com Stakeholders, resultando na adaptação do Product Backlog."
    },
    {
        "pergunta": "Durante o Daily Scrum, quem é o único grupo dentro da Equipe Scrum que é o participante ativo e responsável por planejar o trabalho das próximas 24 horas?",
        "alternativas": [
            "O Product Owner.",
            "O Time de Desenvolvimento.",
            "O Scrum Master.",
            "O Scrum Master e o Product Owner em conjunto."
        ],
        "correta": 2,
        "explicacao": "O Time de Desenvolvimento é autogerenciável e o único responsável por adaptar seu próprio plano de trabalho no Daily Scrum."
    },
    {
        "pergunta": "Qual dos elementos do Scrum é considerado o mais importante do framework, atuando como um container de duração fixa para todos os outros eventos?",
        "alternativas": [
            "O Incremento.",
            "A Sprint.",
            "O Product Backlog.",
            "O Sprint Planning."
        ],
        "correta": 2,
        "explicacao": "A Sprint é o ciclo de tempo fixo (Time-Box) que contém todos os outros eventos e o trabalho de desenvolvimento."
    },
    {
        "pergunta": "Na Sprint Retrospective, o que a Equipe Scrum inspeciona em relação ao seu próprio trabalho?",
        "alternativas": [
            "O valor de negócio dos itens concluídos para Stakeholders.",
            "A capacidade e a estimativa de tempo do Time de Desenvolvimento.",
            "O Product Backlog, para garantir a ordem de prioridade.",
            "Indivíduos, interações, processos, ferramentas e a Definição de Pronto (DoD)."
        ],
        "correta": 4,
        "explicacao": "O foco da Retrospectiva é a inspeção interna do processo de trabalho da equipe, visando aumentar a eficácia."
    },
    {
        "pergunta": "Para uma Sprint de um mês, qual é o Time-Box máximo estabelecido para o evento Sprint Review?",
        "alternativas": [
            "1 hora.",
            "3 horas.",
            "4 horas.",
            "8 horas."
        ],
        "correta": 3,
        "explicacao": "4 horas é o limite máximo para o Sprint Review. O Planning é de 8 horas e a Retrospective é de 3 horas."
    }
]

def get_modulo3():
    return {
        'sections': {
            'modulo3': {
                'titulo_modulo': 'Os eventos do Scrum',
                'numero_modulo': 3,
                'descricao_secao': 'Conheça os cinco eventos essenciais que estruturam o framework Scrum e a cronologia que os baseiam a seguir:',
                'conteudo_complementar': True,
                'titulo_complementar': 'Eventos do Scrum',
                'url_download_complementar': 'routes.download',
                'url_download_key': 'modulo3_apostila',
                'url_anterior': 'routes.module_route',
                'url_anterior_params': {'module_name': 'modulo2', 'section_name': 'modulo2'},
                'url_proximo': 'routes.module_route',
                'url_proximo_params': {'module_name': 'modulo4', 'section_name': 'modulo4'},
                'mostrar_exercicios': True,
                'template': 'modulo3.html',
                'cards': [
                    {
                        'titulo': 'Sprint Planning',
                        'subtitulo': '(Planejamento da Sprint): Neste evento crucial, toda a equipe Scrum se reúne para planejar de forma colaborativa todos os trabalhos que serão realizados e entregues durante o ciclo da próxima Sprint.',
                        'texto': [
                            {'text': 'Objetivo Principal:', 'bold': True},
                            {'text': 'Definir a Meta da Sprint (O "O Quê"): A equipe deve determinar o que é realisticamente possível ser entregue como um incremento funcional ao final da Sprint.'},
                            {'text': 'Definir o "Como": A equipe deve planejar como o trabalho será realizado e estabelecer a definição de "Pronto" (Definition of Done - DoD) para garantir que as entregas sejam completas e de alta qualidade.'},
                            {'text': 'Participantes:', 'bold': True},
                            {'text': 'Product Owner.'},
                            {'text': 'Scrum Master.'},
                            {'text': 'Time de Desenvolvimento.'},
                            {'text': 'Passo a Passo do Planejamento:', 'bold': True},
                            {'text': 'Apresentação das Prioridades (Pelo PO): O Product Owner apresenta e esclarece ao Time de Desenvolvimento quais são os itens do Backlog do Produto que possuem a maior prioridade e valor.'},
                            {'text': 'Seleção dos Itens (Pelo Dev Team): O Time de Desenvolvimento, baseado em sua capacidade, seleciona os itens do Backlog que se compromete a realizar durante a Sprint.'},
                            {'text': 'Definição da Meta (Pela Equipe): A equipe, em conjunto, estabelece uma Meta clara e unificada para a Sprint (o objetivo que todos se esforçarão para alcançar).'},
                            {'text': 'Quebra e Detalhamento das Tarefas (Pelo Dev Team): Para cada item selecionado, o Time de Desenvolvimento detalha e "quebra" o trabalho em tarefas menores, identifica as estimativas de tempo ou esforço necessárias e cria o Quadro de Tarefas da Sprint (Sprint Backlog).'},
                            {'text': 'Nota: Este é o detalhamento do "Como" o trabalho será feito, transformando os itens do Backlog em passos acionáveis.'}
                         ],
                        'icon': 'planning.png',
                        'modal_icon': 'planning_rx.png',
                        'bg_color': '#8c52ff'
                    },
                    {
                        'titulo': 'Daily Scrum',
                        'subtitulo': '(Reunião Diária): O Daily Scrum é uma reunião rápida, diária e essencial para o Time de Desenvolvimento. É o principal momento de inspeção e adaptação do trabalho para garantir o foco na Meta da Sprint.',
                        'texto': [
                            {'text': 'Duração Máxima (Time-Box):', 'bold': True},
                            {'text': 'A reunião é estritamente limitada a 15 minutos.'},
                            {'text': 'Objetivo Principal:.', 'bold': True},
                            {'text': 'Sincronização: Manter todos os membros do Time de Desenvolvimento alinhados sobre o andamento do trabalho.'},
                            {'text':'Inspeção e Adaptação: Inspecionar o progresso em direção à Meta da Sprint e adaptar o plano das próximas 24 horas, identificando desvios e ajustando a rota.'},
                            {'text':'Participantes:', 'bold': True},
                            {'text':'Time de Desenvolvimento '},
                            {'text':'Scrum Master (facilitador) '},
                            {'text':'Product Owner (opcional) '},
                            {'text':'Principais Atividades:', 'bold': True},
                            {'text':'Embora o formato clássico das "três perguntas" seja comum, o foco principal deve ser a progressão em direção à Meta da Sprint. A equipe pode usar estas questões para guiar a discussão:'},
                            {'text':'1. Progresso: O que fizemos desde a última Daily que ajudou o time a alcançar a Meta da Sprint? '},
                            {'text':'2. Próximos Passos: O que farei hoje para ajudar o time a alcançar a Meta da Sprint? '},
                            {'text':'3. Impedimentos: Há algum impedimento, risco ou obstáculo que esteja atrasando a mim ou o time? '},
                            {'text':'Observação: É um momento de planejamento de 24 horas e não um relatório de status. As discussões detalhadas sobre a resolução de impedimentos ou problemas técnicos devem ser feitas imediatamente após o Daily Scrum, com quem for necessário.'}

                        ],
                        'icon': 'daily.png',
                        'modal_icon': 'daily_color.png',
                        'bg_color': '#ff5757'
                    },
                    {
                        'titulo': 'Sprint',
                        'subtitulo': '(Ciclo de Desenvolvimento): A Sprint é um período fixo (Time-Box) e constante, que serve como um contêiner para todos os outros eventos Scrum e atividades de desenvolvimento, onde o valor é criado.',
                        'texto': [
                            {'text': 'Objetivo Central:', 'bold': True},
                            {'text': 'Criar um Incremento de Produto (uma porção funcional do produto) que seja "Potencialmente Entregável" e que agregue valor ao cliente.'},
                            {'text': 'Duração:','bold': True},
                            {'text': 'O time define uma duração fixa. Normalmente, dura entre 1 e 4 semanas (sendo 2 semanas a mais comum) e uma vez definida, a duração não muda.'},
                            {'text':'Product Owner (PO)'},
                            {'text':'Scrum Master (SM)'},
                            {'text':'Time de Desenvolvimento (Dev Team)'},
                            {'text':'Principais Atividades:', 'bold': True},
                            {'text':'A Sprint é o período em que a maior parte do trabalho acontece. O foco do Time de Desenvolvimento é:'},
                            {'text':'1. Execução Focada: Realizar as tarefas necessárias para alcançar a Meta da Sprint, extraídas do Sprint Backlog.'},
                            {'text':'2. Desenvolvimento e Qualidade: Desenvolver, testar, integrar e validar o incremento do produto para que ele atenda à Definição de Pronto (DoD).'},
                            {'text':'3. Colaboração Contínua: Manter uma comunicação constante e trabalhar em conjunto para resolver impedimentos e garantir o fluxo de valor. '},
                            {'text':'4. Adaptação Diária: Inspecionar o progresso diariamente (durante o Daily Scrum) e fazer as adaptações necessárias no plano de trabalho das próximas 24 horas.'},
                            {'text':'Observação: Uma Sprint só termina quando seu time-box (tempo fixo) expira, não quando o trabalho está finalizado. Somente o Product Owner pode cancelar uma Sprint, mas isso é raro.'}
                        ],
                        'icon': 'sprint.png',
                        'modal_icon': 'sprint_color.png',
                        'bg_color': '#ff751f'
                    },
                    {
                        'titulo': 'Review',
                        'subtitulo': '(Revisão da Sprint): Uma sessão de trabalho informal realizada no final da Sprint para inspecionar o Incremento e adaptar o Product Backlog com base no feedback dos stakeholders e no desempenho da Sprint.',
                        'texto': [
                            {'text': 'Duração:', 'bold': True},
                            {'text': 'Limitado a 4 horas para uma Sprint de um mês (para Sprints mais curtas, o evento é proporcionalmente mais curto). '},
                            {'text': 'Objetivo Principal:', 'bold': True},
                            {'text': 'Inspecionar o Incremento recém-construído e adaptar o Product Backlog. O resultado é um Product Backlog revisado que define o que a equipe trabalhará em seguida.'},
                            {'text': 'Participantes:', 'bold': True},
                            {'text': 'Product Owner'},
                            {'text':'Scrum Master'},
                            {'text':'Time de Desenvolvimento'},
                            {'text':'Stakeholders'},
                            {'text':'Principais Atividades:','bold': True},
                            {'text':'1. Apresentação (Pelo PO e Dev Team):'},
                            {'text':'O Product Owner explica quais itens do Sprint Backlog foram concluídos ("Done") e quais não foram. O Time de Desenvolvimento demonstra o Incremento e responde a perguntas sobre o trabalho que foi realizado.'},
                            {'text':'2. Discussão:'},
                            {'text':'O Time de Desenvolvimento debate o que correu bem, quais problemas surgiram e como foram resolvidos.'},
                            {'text':'3. Projeção e Colaboração (Pelo PO e Stakeholders):'},
                            {'text':'O PO discute o status atual do Product Backlog, as prováveis datas de entrega futuras e a Equipe Scrum, junto aos stakeholders, colabora sobre o que fazer a seguir com base na revisão.'}
                        ],
                        'icon': 'review.png',
                        'modal_icon': 'review_color.png',
                        'bg_color': '#7ed957'
                    },
                    {

                        'titulo': 'Retrospective',
                        'subtitulo': '(Retrospectiva da Sprint): O último evento da Sprint, cujo propósito é planejar formas de aumentar a qualidade e a eficácia. A Equipe Scrum inspeciona a si mesma em relação a indivíduos, interações, processos, ferramentas e sua Definição de Pronto (DoD).',
                        'texto': [
                            {'text': 'Duração:', 'bold': True},
                            {'text': 'Estritamente limitado a 3 horas para uma Sprint de um mês (para Sprints mais curtas, o evento é proporcionalmente mais curto).'},
                            {'text': 'Objetivo Principal:', 'bold': True},
                            {'text': 'Identificar as mudanças mais úteis para melhorar sua eficácia. A Equipe Scrum planeja a incorporação dessas melhorias na próxima Sprint.'},
                            {'text': 'Participantes:','bold': True},
                            {'text': 'Product Owner'},
                            {'text': 'Scrum Master'},
                            {'text': 'Time de Desenvolvimento'},
                            {'text': 'Principais Atividades:', 'bold': True},
                            {'text': '1. Reflexão e Discussão:'},
                            {'text': 'A equipe discute o que correu bem, quais problemas encontrou e como esses problemas foram (ou não) resolvidos.'},
                            {'text': '2. Identificação de Causas:'},
                            {'text': 'A equipe identifica as suposições que a levaram ao erro e explora suas origens. '},
                            {'text': '3. Criação de Ações:'},
                            {'text': 'A equipe seleciona as melhorias mais impactantes e cria um plano concreto de ações para implementá-las na próxima Sprint'}

                        ],
                        'icon': 'retrospective.png',
                        'modal_icon': 'retrospective_color.png',
                        'bg_color': '#0081cc'
                    }
                    
                ]
            },
        },
        'quiz': True,
        'primeira_secao': 'modulo3'
    }