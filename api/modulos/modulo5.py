from collections import Counter

SOFT_SKILLS_INFO = {
    "comunicacao": {
        "label": "Comunicação Eficaz",
        "description": "Você se destaca em expressar ideias claramente, ouvir ativamente e garantir que todos estejam na mesma página. Sua força está em construir pontes de entendimento."
    },
    "colaboracao": {
        "label": "Colaboração",
        "description": "Você tem um talento natural para trabalhar em equipe, apoiar os colegas e buscar objetivos comuns. Sua força é unir o time em prol de um propósito maior."
    },
    "adaptabilidade": {
        "label": "Adaptabilidade",
        "description": "Você lida muito bem com mudanças e novos contextos, ajustando-se rapidamente sem perder o foco. Sua força é a resiliência e a capacidade de navegar na incerteza."
    },
    "empatia": {
        "label": "Empatia",
        "description": "Você tem uma grande capacidade de compreender e considerar as perspectivas e sentimentos dos outros. Sua força é criar um ambiente de segurança psicológica e confiança."
    },
    "resolucao": {
        "label": "Resolução de Conflitos",
        "description": "Você aborda divergências de forma construtiva, mediando discussões e ajudando o time a encontrar soluções em que todos ganham. Sua força é manter a harmonia e o foco do time."
    },
    "pensamento": {
        "label": "Pensamento Crítico",
        "description": "Você tem uma habilidade aguçada para analisar situações, questionar premissas e tomar decisões baseadas em dados e lógica. Sua força é trazer clareza e estratégia para o time."
    }
}


modulo5_perguntas = [
    {
        "id": 1,
        "pergunta": "Durante a Daily Scrum, um colega menciona estar travado em uma tarefa. Como você normalmente reage?",
        "alternativas": [
            {"id": "a", "text": "Ofereço ajuda imediatamente e sugiro trabalharmos juntos na solução.", "soft_skill": "colaboracao"},
            {"id": "b", "text": "Faço perguntas para entender melhor o problema antes de sugerir soluções.", "soft_skill": "pensamento"},
            {"id": "c", "text": "Busco entender como ele está se sentindo e se há algo além do técnico o afetando.", "soft_skill": "empatia"},
            {"id": "d", "text": "Explico claramente como resolvi um problema similar e compartilho recursos.", "soft_skill": "comunicacao"}
        ]
    },
    {
        "id": 2,
        "pergunta": "O Product Owner mudou as prioridades no meio da sprint. Qual sua primeira reação?",
        "alternativas": [
            {"id": "a", "text": "Aceito a mudança e rapidamente reorganizo minhas tarefas.", "soft_skill": "adaptabilidade"},
            {"id": "b", "text": "Questiono os motivos e analiso o impacto antes de aceitar a mudança.", "soft_skill": "pensamento"},
            {"id": "c", "text": "Comunico ao time sobre a mudança e alinho as expectativas com todos.", "soft_skill": "comunicacao"},
            {"id": "d", "text": "Busco entender a pressão que o PO está sofrendo e ofereço suporte.", "soft_skill": "empatia"}
        ]
    },
    {
        "id": 3,
        "pergunta": "Na retrospectiva, dois membros do time têm opiniões muito diferentes sobre o mesmo problema. O que você faz?",
        "alternativas": [
            {"id": "a", "text": "Facilito a conversa buscando pontos em comum e uma solução construtiva.", "soft_skill": "resolucao"},
            {"id": "b", "text": "Ouço ambos os lados e tento entender a raiz emocional do conflito.", "soft_skill": "empatia"},
            {"id": "c", "text": "Analiso objetivamente ambas as perspectivas e proponho uma solução baseada em dados.", "soft_skill": "pensamento"},
            {"id": "d", "text": "Reformulo os argumentos de cada um para garantir o entendimento mútuo.", "soft_skill": "comunicacao"}
        ]
    },
    {
        "id": 4,
        "pergunta": "Um novo framework foi introduzido no projeto. Como você aborda essa mudança?",
        "alternativas": [
            {"id": "a", "text": "Estudo rapidamente e me adapto ao novo framework sem resistência.", "soft_skill": "adaptabilidade"},
            {"id": "b", "text": "Compartilho o que aprendo com o time e ajudo outros a entenderem.", "soft_skill": "colaboracao"},
            {"id": "c", "text": "Analiso prós e contras do novo framework comparado ao anterior.", "soft_skill": "pensamento"},
            {"id": "d", "text": "Crio documentação clara e comunicações para facilitar a transição.", "soft_skill": "comunicacao"}
        ]
    },
    {
        "id": 5,
        "pergunta": "O time não está conseguindo cumprir as metas da sprint. Como você contribui para melhorar?",
        "alternativas": [
            {"id": "a", "text": "Proponho sessões de pair programming e apoio mútuo entre os membros.", "soft_skill": "colaboracao"},
            {"id": "b", "text": "Converso individualmente para entender se há problemas pessoais afetando.", "soft_skill": "empatia"},
            {"id": "c", "text": "Analiso métricas e processos para identificar os gargalos reais.", "soft_skill": "pensamento"},
            {"id": "d", "text": "Mudo minha abordagem de trabalho e experimento novas formas de entregar.", "soft_skill": "adaptabilidade"}
        ]
    }
]

def verificar_respostas_modulo5(respostas):
    skill_counts = Counter()
    for q in modulo5_perguntas:
        resposta_usuario = respostas.get(f'question_{q["id"]}')
        if resposta_usuario:
            for option in q['alternativas']:
                if option['id'] == resposta_usuario:
                    skill_counts[option['soft_skill']] += 1
    
    if not skill_counts:
        return {'tipo': 'diagnostico', 'feedback_geral': 'Responda as perguntas para ver seu resultado.'}

    dominant_skill_id = skill_counts.most_common(1)[0][0]
    dominant_skill_info = SOFT_SKILLS_INFO[dominant_skill_id]

    feedback_geral = f"Sua soft skill em destaque é **{dominant_skill_info['label']}**."
    feedback_detalhado = dominant_skill_info['description']

    return {
        'tipo': 'diagnostico',
        'feedback_geral': feedback_geral,
        'feedback_detalhado': feedback_detalhado
    }

def get_modulo5():
    return{
        'sections': {
            'modulo5': {
                'titulo_modulo': 'Scrum e Soft Skills em ação',
                'numero_modulo': 5,
                'descricao_secao': 'Descobrindo como habilidades humanas trasformam equipes ágeis',
                'conteudo_complementar': True,
                'titulo_complementar': 'Soft Skills e Scrum na Prática',
                'url_download_complementar': 'routes.download',
                'url_download_key': 'modulo5_apostila',
                'url_anterior': 'routes.module_route',
                'url_anterior_params': {'module_name': 'modulo4', 'section_name': 'modulo4'},
                'url_proximo': 'routes.module_route',
                'url_proximo_params': {'module_name': 'modulo6', 'section_name': 'modulo6'},
                'mostrar_exercicios': True,
                'template': 'modulo5.html',
                'cards': [
                    {
                        'titulo': 'Spotify',
                        'subtitulo': 'Tecnologia / Streaming de Música',
                        'texto': [
                            {'text': 'Contexto:', 'bold': True},
                            {'text': 'Com mais de 500 desenvolvedores distribuídos em diversos países, o Spotify enfrentava o desafio de manter a inovação e a velocidade de entrega sem perder a coordenação entre times.'},
                            {'text': 'Aplicação do Scrum:', 'bold': True},
                            {'text': 'Criaram o Spotify Model com Squads (times Scrum autônomos), Tribes (conjuntos de squads), Chapters (grupos de especialidade) e Guilds (comunidades de prática).'},
                            {'text': 'Cada Squad funciona como um mini-startup ágil com Product Owner e autonomia para decisões.'},
                            {'text': 'Desafios enfrentados:', 'bold': True},
                            {'text': 'Coordenar centenas de desenvolvedores sem criar burocracia'},
                            {'text': 'Manter alinhamento entre times autônomos'},
                            {'text': 'Evitar duplicação de esforços e retrabalho'},
                            {'text': 'Cultivar cultura de inovação em larga escala'},
                            {'text': 'Resultados Obtidos:', 'bold': True},
                            {'text': 'Autonomia dos times aumentou significativamente'},
                            {'text': 'Velocidade de entrega de features dobrou'},
                            {'text': 'Inovação contínua com experimentação rápida'},
                            {'text': 'Cultura colaborativa entre times diferentes'},
                            {
                                'soft_skills': [
                                    'Comunicação: Essencial para coordenação entre squads e tribes',
                                    'Colaboração: Chapters e Guilds promovem compartilhamento de conhecimento',
                                    'Adaptabilidade: Times ajustam processos conforme necessidade',
                                    'Autonomia e Responsabilidade: Squads tomam decisões próprias'
                                ],

                                'refletir': [
                                    'Como a comunicação entre times autônomos poderia funcionar na sua organização?',
                                    'Quais soft skills você precisaria desenvolver para trabalhar em um modelo como este?',
                                    'Como você equilibraria autonomia com alinhamento organizacional?'
                                ]
                            }
                            
                         ],
                        'icon': 'bi bi-spotify',
                        'modal_icon': 'bi bi-spotify',
                        'bg_color': "#1ED760",
                        'modal_icon_color': '#1DB954'
                    }, 
                    {
                        'titulo': 'Ifood',
                        'subtitulo': 'FoodTech / Delivery',
                        'texto': [
                            {'text': 'Contexto:', 'bold': True},
                            {'text': 'Em um mercado extremamente competitivo e dinâmico, o iFood precisava escalar rapidamente sua plataforma enquanto mantinha alta qualidade e respondia a mudanças constantes do mercado.'},
                            {'text': 'Aplicação do Scrum:', 'bold': True},
                            {'text': 'Implementaram Scrum com times multifuncionais (devs, designers, analistas), sprints de 2 semanas, e entregas contínuas.'},
                            {'text': 'Forte foco em feedback de usuários através de testes A/B e análise de dados em cada sprint.'},
                            {'text': 'Desafios enfrentados:', 'bold': True},
                            {'text': 'Escalar sem perder qualidade do código e da experiência'},
                            {'text': 'Responder rapidamente a mudanças de mercado e concorrência'},
                            {'text': 'Coordenar múltiplos times trabalhando no mesmo produto'},
                            {'text': 'Manter motivação em ambiente de alta pressão'},
                            {'text': 'Resultados Obtidos:', 'bold': True},
                            {'text': 'Redução de 40% no time-to-market'},
                            {'text': 'Qualidade de código melhorou com práticas ágeis'},
                            {'text': 'Capacidade de responder a mudanças em dias, não meses'},
                            {'text': 'Satisfação de clientes aumentou consistentemente'},
                            {
                                'soft_skills': [
                                    'Adaptabilidade: Responder rapidamente a mudanças de mercado',
                                    'Resiliência: Manter produtividade sob pressão',
                                    'Colaboração: Times multifuncionais trabalhando juntos',
                                    'Foco no Cliente: Empatia para entender necessidades dos usuários'
                                ],

                                'refletir': [
                                    'Como sua equipe lida com mudanças frequentes de prioridade?',
                                    'Que soft skills ajudariam você a trabalhar melhor sob pressão?',
                                    'Como você promoveria feedback constante dos usuários no seu contexto?'
                                ]
                            }
                            
                         ],
                        'icon': 'bi bi-cart',
                        'modal_icon': 'bi bi-cart',
                        'bg_color': "#EA1D2C",
                        'modal_icon_color': '#EA1D2C'
                    }, 
                    {
                        'titulo': 'Hospital Albert Einstein',
                        'subtitulo': 'Saúde',
                        'texto': [
                            {'text': 'Contexto:', 'bold': True},
                            {'text': 'Um dos maiores hospitais da América Latina precisava modernizar seus sistemas de TI críticos sem comprometer a segurança dos pacientes ou interromper operações vitais.'},
                            {'text': 'Aplicação do Scrum:', 'bold': True},
                            {'text': 'Scrum foi aplicado com sprints cuidadosamente planejadas, validação constante com equipes médicas (stakeholders), e entregas incrementais em ambientes de homologação antes de produção.'},
                            {'text': ' Cerimônias adaptadas para incluir profissionais de saúde.'},
                            {'text': 'Desafios enfrentados:', 'bold': True},
                            {'text': 'Trabalhar em ambiente altamente regulado e crítico'},
                            {'text': 'Engajar stakeholders médicos ocupados nas cerimônias'},
                            {'text': 'Garantir zero downtime em sistemas vitais'},
                            {'text': 'Equilibrar inovação com segurança e compliance'},
                            {'text': 'Resultados Obtidos:', 'bold': True},
                            {'text': 'Sistemas implantados sem interrupção de serviços'},
                            {'text': 'Adoção pelos médicos 3x mais rápida'},
                            {'text': 'Feedback contínuo melhorou usabilidade drasticamente'},
                            {'text': 'Projetos entregues 30% mais rápido'},
                            {
                                'soft_skills': [
                                    'Empatia: Entender pressões e necessidades dos profissionais de saúde',
                                    'Comunicação: Traduzir termos técnicos para stakeholders médicos',
                                    'Responsabilidade: Consciência do impacto em vidas humanas',
                                    'Escuta Ativa: Capturar feedback de usuários não-técnicos'
                                ],

                                'refletir': [
                                    'Como você adaptaria o Scrum para um ambiente altamente regulado?',
                                    'Quais habilidades de comunicação são essenciais ao trabalhar com stakeholders não-técnicos?',
                                    'Como equilibrar velocidade ágil com segurança crítica?'
                                ]
                            }
                            
                         ],
                        'icon': 'bi bi-heart',
                        'modal_icon': 'bi bi-heart',
                        'bg_color': "#0078D4",
                        'modal_icon_color': '#0078D4'
                    }, 
                    {
                        'titulo': 'Banco Digital',
                        'subtitulo': 'Fintech / Serviços Financeiros',
                        'texto': [
                            {'text': 'Contexto:', 'bold': True},
                            {'text': 'Uma fintech nascida digital competindo contra bancos tradicionais, usando agilidade como principal diferencial competitivo desde o primeiro dia.'},
                            {'text': 'Aplicação do Scrum:', 'bold': True},
                            {'text': 'Scrum como DNA organizacional - todos os times (produto, marketing, operações, tecnologia) trabalham com práticas ágeis. Sprints sincronizadas, reviews compartilhadas entre áreas, e cultura de experimentação rápida.'},
                            {'text': 'Desafios enfrentados:', 'bold': True},
                            {'text': 'Estabelecer cultura ágil desde o início'},
                            {'text': 'Estender Scrum além de TI para toda empresa'},
                            {'text': 'Manter qualidade em ritmo acelerado de lançamentos'},
                            {'text': 'Competir com incumbentes usando agilidade'},
                            {'text': 'Resultados Obtidos:', 'bold': True},
                            {'text': 'Lançamento de novos produtos em semanas'},
                            {'text': 'Taxa de bugs em produção reduziu 60%'},
                            {'text': 'NPS aumentou consistentemente trimestre a trimestre'},
                            {'text': 'Time-to-market 10x mais rápido que concorrentes'},
                            {
                                'soft_skills': [
                                    'Mentalidade de Crescimento: Experimentação e aprendizado constante',
                                    'Colaboração Cross-funcional: Times de diferentes áreas trabalhando juntos',
                                    'Pensamento Crítico: Análise rápida de dados para decisões',
                                    'Comunicação: Alinhamento constante entre múltiplas áreas'
                                ],

                                'refletir': [
                                    'Como você promoveria práticas ágeis fora da área de tecnologia?',
                                    'Que soft skills são necessárias para experimentação rápida e segura?',
                                    'Como criar uma cultura de aprendizado a partir de falhas?'
                                ]
                            }
                            
                         ],
                        'icon': 'bi bi-bank',
                        'modal_icon': 'bi bi-bank',
                        'bg_color': "#9C1BD8",
                        'modal_icon_color': '#9C1BD8'
                    }, 
                ]
            }
        },
        'quiz': True,
        'primeira_secao': 'modulo5'
    }