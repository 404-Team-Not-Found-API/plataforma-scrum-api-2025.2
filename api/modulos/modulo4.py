# api/modulos/modulo4.py

modulo4_perguntas = [
    {
        "pergunta": "Qual artefato do Scrum tem a 'Meta do Produto' como seu compromisso?",
        "alternativas": [
            "O Product Backlog",
            "O Sprint Backlog",
            "O Incremento",
            "A Definição de Pronto"
        ],
        "correta": 1,
        "explicacao": "O Compromisso do Product Backlog é a Meta do Produto."
    },
    {
        "pergunta": "Qual característica deve ser obrigatoriamente satisfeita para que um item do Product Backlog se torne parte de um Incremento?",
        "alternativas": [
            "Ter sido estimado pelo Time de Desenvolvimento",
            "Ter sido apresentado na Daily Scrum",
            "Ter atendido à Definição de Pronto (Definition of Done)",
            "Ter sido liberado para os Stakeholders"
        ],
        "correta": 3,
        "explicacao": "A DoD (Definição de Pronto) é o Compromisso do Incremento."
    },
    {
        "pergunta": "O que o Sprint Backlog representa para Desenvolvedores durante uma Sprint?",
        "alternativas": [
            "O plano de longo prazo para o produto.",
            "A soma de todos os itens completados nas Sprints anteriores.",
            "O plano de trabalho em tempo real para alcançar a Meta da Sprint.",
            "A lista de impedimentos e riscos técnicos."
        ],
        "correta": 3,
        "explicacao": "O Sprint Backlog é o plano de trabalho dos Desenvolvedores para alcançar a Meta da Sprint."
    },
    {
        "pergunta": "O que a Meta da Sprint (Sprint Goal) representa em relação ao Sprint Backlog?",
        "alternativas": [
            "O que será entregue no final de cada dia.",
            "O padrão de qualidade que deve ser atingido pelo Incremento.",
            "O propósito singular que fornece coerência aos itens selecionados.",
            "O estado futuro de longo prazo para o produto."
        ],
        "correta": 3,
        "explicacao": "A Meta da Sprint é o compromisso do Sprint Backlog e define o objetivo único que fornece coerência ao trabalho."
    },
    {
        "pergunta": "Qual o principal objetivo dos Artefatos do Scrum (Product Backlog, Sprint Backlog e Incremento) em sua totalidade?",
        "alternativas": [
            "Garantir que o Product Owner nunca mude a ordem do Product Backlog.",
            "Definir os papéis do Scrum Team e suas responsabilidades diárias.",
            "Maximizar a transparência das informações.",
            "Servir como um contrato formal entre o Time de Desenvolvimento e os Stakeholders."
        ],
        "correta": 3,
        "explicacao": "Conforme o Scrum Guide, os artefatos são concebidos para maximizar a transparência das informações chave."
    },
    {
        "pergunta": "Quem é o principal responsável por garantir que o Incremento atenda à Definição de Pronto (Definition of Done)?",
        "alternativas": [
            "O Scrum Master, pois ele facilita o processo.",
            "O Product Owner, pois ele aceita o produto final.",
            "O Time de Desenvolvimento (Developers).",
            "Os Stakeholders, pois eles validam a entrega."
        ],
        "correta": 3,
        "explicacao": "Os Desenvolvedores são responsáveis pela qualidade e por garantir que cada Incremento atenda à Definição de Pronto."
    }
]

def get_modulo4():
    return {
        'sections': {
            'modulo4': {
                'titulo_modulo': 'A Caixa de Ferramentas',
                'numero_modulo': 4,
                'descricao_secao': 'Artefatos e ferramentas práticas do Scrum',
                'conteudo_complementar': True,
                'titulo_complementar': 'Artefatos do Scrum',
                'url_download_complementar': 'routes.download',
                'url_download_key': 'modulo4_apostila',
                'url_anterior': 'routes.module_route',
                'url_anterior_params': {'module_name': 'modulo3', 'section_name': 'modulo3'},
                'url_proximo': 'routes.module_route',
                'url_proximo_params': {'module_name': 'modulo6', 'section_name': 'modulo6'},
                'mostrar_exercicios': True,
                'template': 'modulo4.html',
                'cards': [
                    {
                        'titulo': 'Product Backlog',
                        'subtitulo': 'Product Backlog: É uma lista ordenada e emergente do que é necessário para melhorar o produto. É a única fonte de trabalho para o Time Scrum.',
                        'texto': [
                            {'text': 'Objetivo:', 'bold': True},
                            {'text': 'Fornecer uma visão completa e priorizada do que precisa ser desenvolvido.'},
                            {'text': 'Características:', 'bold': True},
                            {'text': 'É dinâmico, em constante mudança para identificar o que o produto precisa para ser adequado, competitivo e útil.'},
                            {'text': 'O Product Owner é responsável pelo Product Backlog, incluindo seu conteúdo, ordenação e garantia de que esteja transparente, visível e compreendido.'},
                            {'text': 'Os itens no topo do Product Backlog são geralmente mais detalhados e refinados, prontos para serem selecionados para uma Sprint.'},
                            {'text': 'Componentes:', 'bold': True},
                            {'text': 'Novas funcionalidades: Requisitos de alto nível ou funcionalidades que agregam valor ao usuário.'},
                            {'text': 'Melhorias técnicas: Inclui trabalhos para limpar e otimizar o código (refatoração), manter as ferramentas atualizadas e pagar o "débito técnico" (o custo de ter tomado atalhos no passado).'},
                            {'text': 'Correções de bugs: Itens que corrigem falhas ou comportamentos indesejados no produto'},
                            {'text': 'Requisitos não-funcionais: Qualidades do sistema, como desempenho, segurança, usabilidade e escalabilidade.'},
                            {'text': 'Pesquisa e experimentos: Atividades para aprender mais sobre o mercado, usuários ou tecnologia'},
                            {'text': 'Compromisso: Meta do Produto', 'bold': True},
                            {'text': 'A Meta do Produto é o estado futuro do produto que o Time Scrum e os Stakeholders pretendem alcançar.'},
                            {'text': 'A Meta do Produto é o objetivo de longo prazo para o Time Scrum.'},
                            {'text': 'O Product Backlog emerge para definir o que irá realizar a meta do Produto.'},
                            {'text': 'Benefícios:', 'bold': True},
                            {'text': 'Transparência sobre o que será desenvolvido: Garante que todos (Time Scrum e Stakeholders) tenham uma visão clara e unificada do trabalho a ser feito no produto.'},
                            {'text': 'Priorização clara baseada em valor: A ordenação do Backlog, de responsabilidade do Product Owner, maximiza o valor do trabalho. Itens mais importantes (e de maior valor) estão no topo.'},
                            {'text': 'Evolui continuamente conforme aprendizado: É um artefato dinâmico. Ele muda à medida que o mercado, as necessidades dos usuários e as capacidades do produto evoluem.'},
                            {'text': 'Facilita o planejamento de Sprints: Itens no topo são transparentes e detalhados o suficiente para serem selecionados no Planejamento da Sprint.'},
                            {'text': 'Dicas Práticas (Refinamento do Product Backlog):', 'bold': True},
                            {'text': 'O Refinamento do Product Backlog é o ato de quebrar e adicionar detalhes, como descrições, ordem e tamanho aos itens do Product Backlog.'},
                            {'text': 'Mantenha os itens no topo mais detalhados: Itens de maior prioridade (aqueles que serão trabalhados nas próximas Sprints) devem ser mais claros e detalhados do que os itens de baixa prioridade na parte inferior.'},
                            {'text': 'Use critérios de aceite claros: Defina as condições que um item deve satisfazer para ser considerado completo, garantindo um entendimento compartilhado.'},
                            {'text': 'Refine regularmente com o time: Os Developers que farão o trabalho são responsáveis por dimensionar (estimar) os itens. O Product Owner refina os itens com a colaboração dos Developers.'},
                            {'text': 'Priorize com base em valor de negócio: O Product Owner é responsável por maximizar o valor do produto resultante do trabalho do Time Scrum, geralmente feito através da ordenação (priorização) dos itens.'},
                         ],
                        'icon': 'product_backlog.png',
                        'modal_icon': 'backlog_color.png',
                        'bg_color': '#8FAA13'
                    }, 
                    {
                        'titulo': 'Sprint Backlog',
                        'subtitulo': [
                            'O Sprint Backlog é composto por três elementos:',
                            '(1) Meta da Sprint (o porquê).',
                            '(2) Itens do Product Backlog selecionados para a Sprint (o quê).',
                            '(3) Plano de ação para entregar o Incremento (o como).'
                        ],
                        'texto': [
                            {'text': 'Compromisso: Meta da Sprint (Sprint Goal)', 'bold': True},
                            {'text': 'O único objetivo da Sprint'},
                            {'text': 'Fornece coerência e foco ao trabalho da Sprint.'},
                            {'text': 'A equipe se compromete a fazer o melhor para alcançar este objetivo.'},
                            {'text': 'Componentes:', 'bold': True},
                            {'text':'O Sprint Backlog é um plano criado pelo time de desenvolvimento no Planejamento da Sprint.', 'bold': True},
                            {'text': 'Itens selecionados do Product Backlog: O "O Quê" será entregue para cumprir a Meta da Sprint.'},
                            {'text': 'Plano de ação para concluí-los: O "Como" a equipe transformará esses itens em um Incremento que atenda à Definição de Pronto (DoD).'},
                            {'text': 'Tarefas técnicas necessárias: O trabalho que emerge dos itens do Product Backlog, que os desenvolvedores identificam para si mesmos durante a Sprint.'},
                            {'text': 'O conhecimento emergente: O Sprint Backlog é atualizado conforme o Time Scrum aprende mais sobre o trabalho necessário.'},
                            {'text': 'Benefícios', 'bold': True},
                            {'text': 'Transparência sobre o trabalho em andamento: É uma imagem altamente visível e em tempo real do trabalho que os desenvolvedores planejam realizar na Sprint.'},
                            {'text': 'Permite auto-organização do time: São os desenvolvedores que criam, atualizam e gerenciam o Sprint Backlog, escolhendo como e quem executará o trabalho.'},
                            {'text': 'Facilita acompanhamento diário: Serve como o foco principal para a Daily Scrum (Reunião Diária), onde o progresso em direção à Meta da Sprint é inspecionado.'},
                            {'text': 'Visibilidade de progresso em tempo real: Deve ter detalhes suficientes para que o progresso possa ser inspecionado na Daily Scrum.'},
                            {'text': 'Dicas Práticas', 'bold': True},
                            {'text': 'Atualize diariamente: O Sprint Backlog é atualizado pelos desenvolvedores à medida que o trabalho é realizado e novos aprendizados surgem.'},
                            {'text': 'Detalhe em tarefas menores: Os desenvolvedores geralmente detalham os itens do Product Backlog em tarefas menores e gerenciáveis para aumentar a transparência.'},
                            {'text': 'Foque na Meta da Sprint: Se o trabalho necessário mudar, a equipe colabora com o Product Owner para negociar o escopo do Sprint Backlog para não comprometer a Meta da Sprint.'},                            
                            {'text': 'Use um quadro visual (físico ou digital): A visualização do Sprint Backlog (por exemplo, em um quadro Kanban ou plataformas digitais desenvolvidas para execução desse trabalho) ajuda a maximizar a transparência e a facilitar a inspeção diária do progresso.'},                           
                         ],
                        'icon': 'sprint_backlog.png',
                        'modal_icon': 'sprint_backlog_color.png',
                        'bg_color': '#EE671E'
                    },
                    {
                        'titulo': 'Incremento',
                        'subtitulo': 'O Incremento é um degrau concreto em direção à Meta do Produto. É a soma de todos os itens do Product Backlog concluídos durante uma Sprint, mais o valor dos Incrementos de todas as Sprints anteriores.',
                        'texto': [
                            {'text': 'Compromisso: Definição de Pronto - DoD', 'bold': True},
                            {'text': 'O Compromisso para o Incremento é a Definição de Pronto (DoD).'},
                            {'text': 'A DoD é uma descrição formal do estado do Incremento quando ele atende às medidas de qualidade exigidas para o produto.'},
                            {'text': 'Quando um item do Product Backlog atende à DoD, nasce um Incremento.'},
                            {'text': 'Benefícios:', 'bold': True},
                            {'text': 'Entrega de valor contínua: Múltiplos Incrementos podem ser criados dentro de uma Sprint, permitindo a entrega de valor aos stakeholders a qualquer momento.'},
                            {'text': 'Produto sempre utilizável e potencialmente entregável: O Incremento deve estar em condição utilizável (atender à DoD), independentemente de o Product Owner decidir liberá-lo imediatamente ou não.'},
                            {'text': 'Base para Feedback (Empirismo): O Incremento é inspecionado na Revisão da Sprint, permitindo que o Time Scrum e os Stakeholders forneçam feedback sobre o produto.'},
                            {'text': 'Transparência e Qualidade: A DoD cria transparência, fornecendo um entendimento compartilhado de qual trabalho foi concluído e qual o padrão de qualidade obrigatório para o produto.'},
                            {'text': 'Dicas Práticas:', 'bold': True},
                            {'text': 'Defina claramente sua Definition of Done: A DoD deve ser clara e rigorosa. Se um item do Product Backlog não atender à DoD, ele não pode ser liberado ou apresentado na Revisão da Sprint; ele retorna ao Product Backlog.'},
                            {'text': 'Garanta que seja funcional e testado: O Incremento deve funcionar em conjunto com todos os Incrementos anteriores e ter sido verificado, garantindo que a funcionalidade esteja completa e testada.'},
                            {'text': 'Mantenha qualidade técnica alta: O Incremento é um passo em direção à Meta do Produto, mas precisa atender aos padrões de qualidade definidos, sem atalhos que gerem débito técnico.'},
                            {'text': 'Priorize o lançamento de valor: Embora a liberação não seja obrigatória ao final da Sprint, o Product Owner deve procurar liberar o Incremento sempre que for benéfico para o negócio.'},
                            {'text': 'Ferramentas Práticas:', 'bold': True},
                            {'text': 'Ferramentas complementares que ajudam times Scrum a terem mais visibilidade e controle.', 'bold': True},   
                            {'text': 'Gráfico Burndown: Ferramenta visual que mostra o progresso da Sprint.'}                          
                         ],
                        'icon': 'incremento.png',
                        'modal_icon': 'incremento_color.png',
                        'bg_color': '#D002AB'
                    },
                    {
                        'tipo': 'texto',
                        'titulo': 'Ferramentas Práticas:',
                        'texto': [
                            {'text': 'Além dos artefatos, existem ferramentas complementares que ajudam os times Scrum a terem mais visibilidade e controle sobre o progresso.'}
                         ],
                    },
                    {
                        'titulo': 'Gráfico Burndown',
                        'subtitulo': 'O Gráfico Burndown é a ferramenta visual que funciona como um termômetro, ele mostra a relação entre o trabalho que resta versus o tempo que resta em uma Sprint.',
                        'texto': [
                            {'text': 'Objetivo:', 'bold': True},
                            {'text': 'O propósito: Acompanhar o progresso do Time Scrum para ver se estamos no caminho certo para alcançar a Meta da Sprint (o alvo) no tempo definido.'},
                            {'text': 'A função: Identificar desvios (atrasos ou adiantamentos) do plano rapidamente, permitindo que o time faça adaptações imediatas.'},                        
                            {'text': 'Benefícios:', 'bold': True},
                            {'text': 'Visibilidade Instantânea do Progresso: Com um olhar rápido, todos sabem como a Sprint está indo. É como olhar o velocímetro do carro.'},
                            {'text': 'Identifica Problemas Cedo: Se a linha de trabalho restante parar de cair (ou subir!), isso sinaliza um problema (impedimento, dificuldade técnica, ou escopo mal-entendido) antes que seja tarde demais.'},
                            {'text': 'Facilita Transparência com Stakeholders: É uma forma simples e objetiva de mostrar aos interessados o quanto falta para a entrega, sem entrar em detalhes técnicos complexos.'},
                            {'text': 'Ajuda na Previsibilidade: Ao analisar a velocidade com que o trabalho está sendo concluído (a inclinação da linha), o time consegue prever se terminará no prazo.'},
                            {'text': 'Dicas práticas', 'bold': True},
                            {'text': 'Atualize diariamente após o Daily Scrum: O gráfico só é útil se refletir a realidade. Use o Daily Scrum (Reunião Diária) para ajustar o trabalho restante, mantendo o gráfico preciso.'},
                            {'text': 'Use para identificar tendências, não apenas status: Não olhe apenas para o ponto de hoje. Olhe a inclinação da linha: se ela estiver muito reta ou subindo, a equipe precisa discutir por que o trabalho não está diminuindo.'},
                            {'text': 'Discuta desvios significativos com o time: Se a linha de progresso estiver muito acima da linha ideal (o esperado), isso não é um erro; é um sinal de alerta. Use esse sinal para inspecionar e adaptar o Sprint Backlog.'},
                            {'text': 'Combine com outras métricas: O Burndown mostra o que falta. Combine-o com o Velocidade (o quanto o time entrega por Sprint) para entender melhor a capacidade futura da equipe.'},                                                          
                         ],
                        'icon': 'burndown.png',
                        'modal_icon': 'burndown.png',
                        'bg_color': '#fff',
                        'text_color': '#FF6200',
                        'border_color': '#FF6200'
                    },
                    {
                        'tipo': 'texto',
                        'titulo': 'Tutorial de Ferramentas:',
                        'texto': [
                            {'text': 'Aprenda a usar as principais ferramentas digitais para implementar Scrum no seu time.'}
                         ],
                    },
                    {
                        'titulo': 'Jira',
                        'subtitulo': 'Ferramenta completa para gerenciamento ágil de projetos, ideal para times de desenvolvimento.',
                        'texto': [
                            {'text': 'Passo a Passo:', 'bold': True},
                            {'text':'1) Crie um novo projeto Scrum no Jira'},
                            {'text':'2) Configure o quadro com as colunas: To Do, In Progress, Done'},
                            {'text':'3) Escreva User Stories com formato: Como [usuário], eu quero [ação] para [benefício]'},
                            {'text':'4) Adicione critérios de aceite em cada história'},
                            {'text':'5 Estime usando Story Points'},
                            {'text':'6) Mova os cards entre as colunas conforme o progresso'},
                            {'text':'7) Use o Burndown Chart para acompanhar a Sprint'},
                            {'text': 'Casos de Uso no Scrum:','bold': True}, 
                            {'text':'Gerenciar Product Backlog e Sprint Backlog'},
                            {'text':'Rastrear bugs e melhorias técnicas'},
                            {'text':'Gerar relatórios de progresso automaticamente'},
                            {'text': 'Tutorial:', 'bold': True},
                            {'text':'Assista aos tutoriais do canal Jira para ver a ferramenta em ação:'},
                            {'link_text': 'Vídeo 1', 'url': 'https://youtu.be/vCNafmr4Brk?si=fwjf0_XOidGY8rpb'},
                            {'link_text': 'Vídeo 2', 'url': 'https://youtu.be/Ymf5fUkP_rE?si=I1VuT9LvT9wlpttT'},
                            {'text':'💡 Dica: Estas ferramentas têm versões gratuitas que são perfeitas para começar. Explore os templates prontos e tutoriais oficiais disponíveis em cada plataforma.'},

                        ],
                        'icon': 'jira.png',
                        'modal_icon': 'jira.png',
                        'bg_color': '#fff',
                        'text_color': '#2563EB',
                        'border_color': '#2563EB'
                    },
                    {
                        'titulo': 'Trello',
                        'subtitulo':'Ferramenta visual e intuitiva baseada em Kanban, perfeita para começar com Scrum.',
                        'texto': [
                            {'text':'Passo a passo:', 'bold': True},
                            {'text':'1) Crie um board para sua Sprint'},
                            {'text':'2) Adicione listas: Backlog, To Do, Doing, Testing, Done'},
                            {'text':'3) Crie cards para cada User Story ou tarefa'},
                            {'text':'4) Adicione descrição, checklist e etiquetas coloridas'},
                            {'text':'5) Atribua membros do time aos cards'},
                            {'text':'6) Arraste cards entre as colunas durante o Daily Scrum'},
                            {'text':'7) Use Power-Ups para adicionar funcionalidades (burndown, estimativas)'},
                            {'text':'Casos de Uso no Scrum:', 'bold': True},
                            {'text':'Times pequenos ou iniciando com Scrum'},
                            {'text':'Projetos que precisam de simplicidade visual'},
                            {'text':'Gerenciamento de tarefas pessoais da Sprint'},
                            {'text':'Colaboração rápida sem curva de aprendizado'},
                            {'text': 'Tutorial:', 'bold': True},
                            {'text': 'Assista ao tutoriais para ver a ferramenta em ação:'},
                            {'link_text': 'Vídeo 1', 'url': 'https://youtu.be/_HpsaRL9Jug?si=DQeRsCnuDrCA4B12'},
                            {'text': 'Guia Completo:', 'bold': True},
                            {'text': 'Assista ao tutoriais para ver a ferramenta em ação:'},
                            {'link_text': 'Guia', 'url': 'https://trello.com/pt-BR/guide '},
                            {'text': 'Template do Projeto:', 'bold': True},
                            {'text': 'Acesse um template disponível na ferramenta:'},
                            {'link_text': 'Template', 'url': 'https://trello.com/templates/project-management/modelo-de-projeto-(scrum)-iKkUEPyC'}

                        ],
                        'icon': 'trello.png',
                        'modal_icon': 'trello.png',
                        'bg_color': '#fff',
                        'text_color': '#0EA5E9',
                        'border_color': '#0EA5E9',
                        'break_after': True
                    },
                    {
                        'titulo': 'Miro',
                        'subtitulo':'Quadro branco digital colaborativo, ideal para cerimônias Scrum e brainstorming.',
                        'texto': [


                            {'text':'Passo a passo:', 'bold':True},
                            {'text':'1) Crie um board para a Sprint Planning ou Retrospectiva'},
                            {'text':'2) Use templates prontos para Scrum (Sprint Planning, Retro, etc.)'},
                            {'text':'3) Adicione sticky notes para ideias e histórias'},
                            {'text':'4) Organize em colunas ou use frameworks como Start-Stop-Continue'},
                            {'text':'5) Vote nas ideias com emojis ou pontos'},
                            {'text':'6) Exporte resultados para documentação'},
                            {'text':'7) Convide o time para colaborar em tempo real'},
                            {'text':'Casos de Uso no Scrum:', 'bold':True},
                            {'text':'Sprint Planning e refinamento do Backlog'},
                            {'text':'Retrospectivas interativas e dinâmicas'},
                            {'text':'Story Mapping e User Journey'},
                            {'text':'Brainstorming de soluções técnicas'},
                            {'text': 'Tutorial:', 'bold': True},
                            {'text': 'Assista ao tutoriais para ver a ferramenta em ação:'},
                            {'link_text': 'Tutorial', 'url': 'https://youtu.be/S9n8dQAG_6U?si=h9YPN3wTmYOHIey2'},
                            {'text': 'Templates:', 'bold': True},
                            {'text': 'Acesse os templates disponíveis na ferramenta:'},
                            {'link_text': 'Mapa de história do usuário', 'url': 'https://miro.com/app/dashboard/?tpTemplate=f3644964-3446-4de3-bed2-0a928639cb15&isCustom=false&share_link_id=743266210609'},
                            {'link_text': 'Product Backlog', 'url': 'hhttps://miro.com/app/dashboard/?tpTemplate=c81b811a-d5ad-4597-9646-aa8682426b15&isCustom=false&share_link_id=834743914228'},
                            {'link_text': 'Refinamento do Backlog', 'url': 'https://miro.com/app/dashboard/?tpTemplate=3b1b88ec-a574-4d8b-922a-a5ae5dd8182a&isCustom=false&share_link_id=24244301173'},
                            {'link_text': 'Template de Retrospective', 'url': 'https://miro.com/app/dashboard/?tpTemplate=fbdc8d0f-757a-48e6-af63-ef615509aeaa&isCustom=false&share_link_id=513200360576'},
                        ],
                        'icon': 'Miro.png',
                        'modal_icon': 'Miro.png',
                        'bg_color': '#fff',
                        'text_color': '#EAB308',
                        'border_color': '#EAB308'
                    },
                    {
                        'titulo': 'Figma',
                        'subtitulo': 'Ferramenta de design colaborativo para criar protótipos que atendem a Definition of Ready.',
                        'texto': [
                            {'text':'Passo a passo:', 'bold': True},
                            {'text':'1) Crie um novo projeto para o produto/feature'},
                            {'text':'2) Desenhe wireframes para as User Stories'},
                            {'text':'3) Transforme wireframes em protótipos clicáveis'},
                            {'text':'4) Adicione interações e fluxos de navegação'},
                            {'text':'5) Compartilhe com o time para feedback no Refinamento'},
                            {'text':'6) Use comentários para discutir requisitos'},
                            {'text':'7) Exporte assets para os desenvolvedores'},
                            {'text':'Casos de Uso no Scrum:', 'bold':True},
                            {'text':'Validar User Stories antes da Sprint'},
                            {'text':'Garantir que histórias atendam o DoR'},
                            {'text':'Alinhar expectativas entre PO, UX e Devs'},
                            {'text':'Criar protótipos para testes com usuários'},
                            {'text': 'Tutorial:', 'bold': True},
                            {'text': 'Assista ao tutoriais para ver a ferramenta em ação:'},
                            {'link_text': 'Tutorial', 'url': 'https://youtu.be/bYdyNEvr7ks?si=thDsQRUFRiaSzLGC'},
                            {'text': 'Assista ao tutoriais para ver a ferramenta em ação:'},
                            {'link_text': 'Curso', 'url': 'https://help.figma.com/hc/en-us/sections/30880632542743-Figma-Design-for-beginners'},
                        ],
                        'icon': 'Figma.png',
                        'modal_icon': 'Figma.png',
                        'bg_color': '#fff',
                        'text_color': '#A259FF',
                        'border_color': '#A259FF'
                    }           
                                                                                 
                ],
            },
        },
        'quiz': True,
        'primeira_secao': 'modulo4'
    }