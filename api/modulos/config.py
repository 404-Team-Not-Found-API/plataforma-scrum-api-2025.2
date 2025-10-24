# Centralized module configuration
MODULES_CONFIG = {
    'modulo1': {
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
                'url_proximo': 'routes.module_route',  # Next section
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
        'quiz': True
    },
    'modulo2': {
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
                        'bg_color': '#83C7E9' 
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
                        'bg_color': '#7E5DA5'   
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
                        'bg_color': '#ECC252'   
                    }
                ],
                'template': 'modulo2.html'
            },
        },
        'quiz': True
    },
    'modulo3': {
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
                'url_proximo': None,
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
                        'icon': 'bi bi-clipboard-check',
                        'modal_icon': 'bi bi-clipboard-check',
                        'bg_color': '#8c52ff',
                        'list_icon_style': 'dot'
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
                        'icon': 'bi bi-clock',
                        'modal_icon': 'bi bi-clock',
                        'bg_color': '#ff5757',
                        'list_icon_style': 'dot'
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
                        'icon': 'bi bi-calendar-week',
                        'modal_icon': 'bi bi-calendar-week',
                        'bg_color': '#ff751f',
                        'list_icon_style': 'dot'
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
                        'icon': 'bi bi-clipboard-data',
                        'modal_icon': 'bi bi-clipboard-data',
                        'bg_color': '#7ed957',
                        'list_icon_style': 'dot'
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
                        'icon': 'bi bi-arrow-clockwise',
                        'modal_icon': 'bi bi-arrow-clockwise',
                        'bg_color': '#0081cc',
                        'list_icon_style': 'dot'
                    }
                ]
            },
        },
        'quiz': True
    },
}

# Download mappings
DOWNLOADS = {
    'modulo1_secao1': 'modulo_1_secao_1.pdf',
    'modulo1_secao2': 'modulo_1_secao_2.pdf',
    'modulo2': 'modulo_2.pdf',
    'modulo3_apostila': 'modulo_3_eventos_scrum.pdf',
}
