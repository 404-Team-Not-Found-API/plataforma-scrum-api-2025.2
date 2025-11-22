def get_modulo6():
#     """     Retorna a configuração completa para a Simulação da Sprint.#     """
     return {
         "sections": {
             "modulo6": {
                 "titulo_modulo": "Módulo Final: Sua Primeira Sprint",
                 "numero_modulo": 6,
                 "descricao_secao": "Projeto simulado para você praticar e vivenciar o Scrum na prática.",
                 "template": "modulo6.html",
                 'url_anterior': 'routes.module_route',
                 'url_anterior_params': {'module_name': 'modulo5', 'section_name': 'modulo5'},
                 'url_proximo': None,
                 'url_proximo_params': {'module_name': 'modulo1', 'section_name': 'modulo1s2'},
                
                # Lista de Projetos para Sorteio
                "projetos_simulados": [
                    {
                        "id": 1,
                        "nome": "Sistema de Sustentabilidade",
                        "descricao": "Plataforma que ajuda usuários a monitorar seus hábitos de consumo (energia, transporte) e oferece metas para reduzir a pegada de carbono.",
                        "texto": "Plataforma que ajuda usuários a monitorar seus hábitos de consumo — como uso de energia, transporte e descarte de resíduos — e oferece metas personalizadas para reduzir sua pegada de carbono. O desafio é desenvolver uma solução simples e engajante que traduza dados ambientais complexos em ações práticas do dia a dia. O produto deve incentivar o comportamento sustentável com recompensas, notificações e relatórios visuais de progresso.",
                        "icone": "bi bi-globe"
                    },
                    {
                        "id": 2,
                        "nome": "Plataforma de Educação Digital",
                        "descricao": "Ambiente online de cursos com foco em metodologias ativas, onde alunos acompanham progresso de forma gamificada.",
                        "texto": "Plataforma online de cursos e trilhas de aprendizado com foco em metodologias ativas e ensino personalizado. O desafio consiste em criar um ambiente intuitivo onde alunos possam acompanhar o progresso de forma gamificada, interagir com colegas e receber recomendações inteligentes de conteúdos com base em seu desempenho. A proposta deve equilibrar tecnologia, acessibilidade e experiência do usuário para tornar o aprendizado mais engajante e eficiente.",
                        "icone": "bi bi-laptop"
                    },
                    {
                        "id": 3,
                        "nome": "Sistema de Alimentação Saudável",
                        "descricao": "Sistema para registrar refeições, acompanhar nutrientes e receber planos alimentares ajustados às metas do usuário.",
                        "texto": "Plataforma voltada para quem busca uma alimentação mais equilibrada e personalizada. O desafio é desenvolver um sistema que permita ao usuário registrar refeições, acompanhar nutrientes e receber planos alimentares ajustados às suas metas (emagrecimento, ganho de massa, reeducação alimentar etc.). O produto deve priorizar uma interface amigável, notificações inteligentes e integração com dispositivos de monitoramento de saúde.",
                        "icone": "bi bi-apple"
                    },
                    {
                        "id": 4,
                        "nome": "Gestor de Finanças Pessoais",
                        "descricao": "Plataforma para gerenciar gastos, criar orçamentos e categorizar despesas, gerando relatórios financeiros.",
                        "texto": "Plataforma que ajuda usuários a gerenciar seus gastos, criar orçamentos e acompanhar metas financeiras. O desafio é desenvolver um sistema simples, seguro e visualmente claro para categorizar despesas, gerar relatórios e propor melhorias com base nos hábitos de consumo. O diferencial está na personalização: o app deve aprender com o comportamento do usuário e sugerir ajustes automáticos no planejamento financeiro.",
                        "icone": "bi bi-pie-chart"
                    },
                    {
                        "id": 5,
                        "nome": "Organizador de Estudos",
                        "descricao": "Plataforma que auxilia estudantes a planejar rotinas, organizar matérias e tarefas conforme o tempo disponível.",
                        "texto": "Plataforma que auxilia estudantes a planejar e acompanhar sua rotina de estudos de forma inteligente. O desafio consiste em criar uma plataforma que permita organizar matérias, distribuir tarefas conforme o tempo disponível e gerar relatórios de desempenho. O sistema deve oferecer lembretes, integração com calendários e ferramentas de foco, ajudando o usuário a manter a disciplina e alcançar seus objetivos acadêmicos.",
                        "icone": "bi bi-mortarboard"
                    },
                    {
                        "id": 6,
                        "nome": "Sistema de Reservas para Restaurantes",
                        "descricao": "Sistema online para clientes visualizarem horários e reservarem mesas em tempo real.",
                        "texto": "Sistema de reservas online voltado para restaurantes, bares e cafés. O desafio é criar uma plataforma intuitiva para que clientes possam visualizar horários disponíveis, reservar mesas em tempo real e receber confirmações automáticas. Do lado do restaurante, o sistema deve permitir a gestão de reservas, controle de fluxo e comunicação direta com os clientes. O objetivo é reduzir o tempo de espera, aumentar a satisfação do público e otimizar a operação dos estabelecimentos.",
                        "icone": "bi bi-cup-straw"
                    }
                ],

                # Definição das Etapas (Usando 'cards' para compatibilidade)
                "cards": [
                    # ETAPA 1: VISÃO
                    {
                        "id": "visao_produto",
                        "step_index": 1,
                        "icon": "bi bi-clipboard",
                        "titulo": "1. Defina a Visão do Produto",
                        "subtitulo": "Preencha o template de visão do produto para deixar claro o propósito do seu projeto.",
                        "descricao": "Defina claramente a visão do seu produto respondendo às perguntas orientadoras abaixo.",
                        "modo_exibicao": "modal",
                        "tipo_conteudo": "formulario_fixo", 
                        "dicas": ["Comece pequeno - um projeto que possa completar em 1-2 semanas", "Escolha algo com valor real, não apenas um exercício.", "Se for um projeto pessoal, pense em quem se beneficiará", "Seja específico sobre o público-alvo e o problema a resolver"],
                        "campos": [
                            {"id": "nome_projeto", "label": "Nome do Projeto *", "tipo": "input", "placeholder": "Ex: Sistema de Gestão..."},
                            {"id": "publico_alvo", "label": "Para quem? (Público-alvo) *", "tipo": "textarea", "placeholder": "Quem são os usuários?"},
                            {"id": "problema", "label": "Qual a necessidade? *", "tipo": "textarea", "placeholder": "Qual dor o produto resolve?"},
                            {"id": "solucao", "label": "O que é o produto? *", "tipo": "input", "placeholder": "Ex: App Mobile, Plataforma Web..."},
                            {"id": "diferencial", "label": "Diferencial *", "tipo": "textarea", "placeholder": "Por que é único?"},
                            {"id": "objetivo", "label": "Objetivo de Longo Prazo *", "tipo": "textarea", "placeholder": "Qual o impacto esperado?"}
                        ]
                    },
                    # ETAPA 2: BACKLOG
                    {
                        "id": "product_backlog",
                        "step_index": 2,
                        "icon": "bi bi-clipboard-data",
                        "titulo": "2. Crie o Product Backlog",
                        "subtitulo": "Liste funcionalidades e priorize por valor.",
                        "descricao": "Qual será o impacto final do produto?",
                        "modo_exibicao": "modal",
                        "tipo_conteudo": "lista_dinamica",
                        "dicas": ["Use post-its físicos ou ferramenta digital (Trello, Notion, etc.)", "Priorize os itens por valor para o cliente/usuário", "Seja claro e específico nos títulos", "Defina critérios de aceitação mensuráveis", "Quebre itens grandes em tarefas menores" ],
                        "item_schema": [
                            {"id": "titulo", "label": "Título do Item", "tipo": "input", "width": "50%"},
                            {"id": "estimativa", "label": "Esforço Estimado", "tipo": "input", "width": "50%", "placeholder": "Ex: 3 dias"},
                            {"id": "descricao", "label": "Descrição", "tipo": "textarea", "width": "100%", "placeholder": "Detalhes da história..."},
                            {"id": "aceitacao", "label": "Critérios de Aceitação", "tipo": "textarea", "width": "100%", "placeholder": "Deve fazer X, Y e Z..."},
                        ]
                    },
                    # ETAPA 3: PLANNING
                    {
                        "id": "sprint_planning",
                        "step_index": 3,
                        "icon": "bi bi-graph-up",
                        "titulo": "3. Planeje a Sprint",
                        "subtitulo": "Defina a Meta e selecione itens.",
                        "descricao": "Selecione os itens do backlog e defina o objetivo da sua Sprint.",
                        "modo_exibicao": "modal",
                        "tipo_conteudo": "selecao_origem",
                        "origem_dados": "product_backlog",
                        "dicas": ["Cada item deve ser completável em 1-3 dias", "O Sprint deve ser inspirador e claro", "Não se comprometa com demais - melhor entregar menos com qualidade", "Divida os itens selecionados em tarefas menores", "Considere sua capacidade real de trabalho na semana"],
                        "campos_fixos": [
                            {"id": "data-inicio", "label": "Data de Início *", "tipo": "date", "placeholder": "dd/mm/aaaa"},
                            {"id": "data-fim", "label": "Data Final *", "tipo": "date", "placeholder": "dd/mm/aaaa"},
                            {"id": "meta_sprint", "label": "Meta da Sprint (Sprint Goal) *", "tipo": "textarea", "placeholder": "Objetivo principal..."}
                        ]
                    },
                    # ETAPA 4: DAILY
                    {
                        "id": "daily_scrum",
                        "step_index": 4,
                        "icon": "bi bi-clock",
                        "titulo": "4. Daily Scrum",
                        "subtitulo": "Simule o acompanhamento diário.",
                        "descricao": "Registre suas Daily Scrums diariamente. Responda as 3 perguntas principais todos os dias.",
                        "modo_exibicao": "modal",
                        "tipo_conteudo": "formulario_fixo",
                        "dicas": ["Seja breve e objetivo (máximo 5 minutos por dia)", "Mantenha o foco no objetivo da sprint", "Se algo bloquear, busque alternativas rapidamente", "Documentação pode esperar - foco na entrega!", "Foque em completar itens, não em começar muitos"],
                        "campos": [
                            {"titulo_grupo": f"Dia {i}", "campos": [
                                {"id": f"dia{i}_fez", "label": "O que fiz ontem?", "tipo": "input"},
                                {"id": f"dia{i}_fara", "label": "O que farei hoje?", "tipo": "input"},
                                {"id": f"dia{i}_imp", "label": "Impedimentos?", "tipo": "input"}
                            ]} for i in range(1, 8) ## List comprehension. Simples é melhor do que complexo!
                        ]
                    },
                    # ETAPA 5: REVIEW
                    {
                        "id": "sprint_review",
                        "step_index": 5,
                        "icon": "bi bi-check-circle",
                        "titulo": "5. Sprint Review",
                        "subtitulo": "Inspecione o incremento.",
                        "descricao": "Documente o que foi entregue e colete feedback sobre o incremento do produto.",
                        "modo_exibicao": "modal",
                        "tipo_conteudo": "formulario_fixo",
                        "dicas": ["Mostre apenas o que está 'Pronto' (funcional)", "Seja transparente sobre o que não foi completado", "Colete feedback de stakeholders ou usuários", "Atualize o Product Backlog com novos insights", "Celebre as conquistas, mesmo que pequenas!"],
                        "campos": [
                            {"id": "entregaveis", "label": "O que foi entregue?", "tipo": "textarea"},
                            {"id": "feedback", "label": "Feedback recebido", "tipo": "textarea"},
                            {"id": "nao_entregue", "label": "O que não foi concluído e por quê?", "tipo": "textarea"}
                        ]
                    },
                    # ETAPA 6: RETROSPECTIVA
                    {
                        "id": "sprint_retro",
                        "step_index": 6,
                        "icon": "bi bi-arrow-90deg-left",
                        "titulo": "6. Sprint Retrospective",
                        "subtitulo": "Melhoria contínua.",
                        "descricao": "Momento de reflexão e melhoria contínua. Seja honesto e identifique ações concretas.",
                        "modo_exibicao": "modal",
                        "tipo_conteudo": "formulario_fixo",
                        "dicas": ["Seja honesto consigo mesmo - é para seu aprendizado", "Foque em ações específicas, não em generalidades", "Uma melhoria pequena e aplicada vale mais que várias ideias não executadas", "Revise suas anotações antes da próxima Sprint","Considere buscar certificação Scrum (PSM ou CSM)"],
                        "campos": [
                            {"id": "positivo", "label": "O que funcionou bem?", "tipo": "textarea", "placeholder": "Liste os pontos positivos da Sprint..."},
                            {"id": "melhorar", "label": "O que pode melhorar?", "tipo": "textarea", "placeholder": "Identifique oportunidades de melhoria..."},
                            {"id": "acoes", "label": "Ações para a próxima Sprint", "tipo": "textarea", "placeholder": "Defina 1-3 ações concretas e específicas..."}
                        ]
                    }
                ]
            }
        },
        "quiz": False,
        "primeira_secao": "modulo6"
    }
