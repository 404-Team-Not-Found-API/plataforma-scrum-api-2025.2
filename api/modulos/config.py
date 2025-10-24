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
        'quiz': True
    },
    'modulo4': {
        'sections': {
            'modulo4': {
                'titulo_modulo': 'A Caixa de Ferramentas',
                'numero_modulo': 4,
                'descricao_secao': 'Artefatos e ferramentas práticas do Scrum',
                'conteudo_complementar': False,
                'url_anterior': 'routes.module_route',
                'url_anterior_params': {'module_name': 'modulo3', 'section_name': 'modulo3'},
                'url_proximo': None,
                'mostrar_exercicios': True,
                'template': 'modulo4.html',
                'cards': [
                    {
                        'titulo': 'Product Backlog',
                        'subtitulo': 'Product Backlog: NÉ uma lista ordenada e emergente do que é necessário para melhorar o produto. É a única fonte de trabalho para o Time Scrum.',
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
                        'icon': 'planning.png',
                        'modal_icon': 'planning_rx.png',
                        'bg_color': '#8c52ff'
                    }, 
                    {
                        'titulo': 'Sprint Backlog',
                        'subtitulo': 'O Sprint Backlog é composto por três elementos:'
                        '(1) Meta da Sprint(o porquê)'
                        '(2) Conjunto de itens do Product Backlog selecionados para a Sprint (o quê), e'
                        '(3) Plano de ação para entregar o Incremento (o como).',
                        'texto': [
                            {'text': 'Compromisso: Meta da Sprint(Sprint Goal)', 'bold': True},
                            {'text': 'O único objetivo da Sprint.'},
                            {'text': 'Fornece coerência e foco ao trabalho da Sprint.'},
                            {'text': 'A equipe se compromete a fazer o melhor para alcançar este objetivo.'},
                            {'text': 'Componentes'
                            'O Sprint Backlog é um plano criado pelo time de desenvolvimento no Planejamento da Sprint.', 'bold': True},
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
                        'icon': 'planning.png',
                        'modal_icon': 'planning_rx.png',
                        'bg_color': '#8c52ff'
                    },
                    {
                        'titulo': 'Incremento',
                        'subtitulo': 'O Incremento é um degrau concreto em direção à Meta do Produto. É a soma de todos os itens do Product Backlog concluídos durante uma Sprint, mais o valor dos Incrementos de todas as Sprints anteriores.',
                        'texto': [
                            {'text': 'Compromisso: Definição de Pronto - DoD', 'bold': True},
                            {'text': 'O Compromisso para o Incremento é a Definição de Pronto (DoD).'},
                            {'text': 'A DoD é uma descrição formal do estado do Incremento quando ele atende às medidas de qualidade exigidas para o produto.'},
                            {'text': 'Quando um item do Product Backlog atende à DoD, nasce um Incremento.'},
                            {'text': 'Benefícios', 'bold': True},
                            {'text': 'Entrega de valor contínua: Múltiplos Incrementos podem ser criados dentro de uma Sprint, permitindo a entrega de valor aos stakeholders a qualquer momento.'},
                            {'text': 'Produto sempre utilizável e potencialmente entregável: O Incremento deve estar em condição utilizável (atender à DoD), independentemente de o Product Owner decidir liberá-lo imediatamente ou não.'},
                            {'text': 'Base para Feedback (Empirismo): O Incremento é inspecionado na Revisão da Sprint, permitindo que o Time Scrum e os Stakeholders forneçam feedback sobre o produto.'},
                            {'text': 'Transparência e Qualidade: A DoD cria transparência, fornecendo um entendimento compartilhado de qual trabalho foi concluído e qual o padrão de qualidade obrigatório para o produto.'},
                            {'text': 'Dicas Práticas', 'bold': True},
                            {'text': 'Defina claramente sua Definition of Done: A DoD deve ser clara e rigorosa. Se um item do Product Backlog não atender à DoD, ele não pode ser liberado ou apresentado na Revisão da Sprint; ele retorna ao Product Backlog.'},
                            {'text': 'Garanta que seja funcional e testado: O Incremento deve funcionar em conjunto com todos os Incrementos anteriores e ter sido verificado, garantindo que a funcionalidade esteja completa e testada.'},
                            {'text': 'Mantenha qualidade técnica alta: O Incremento é um passo em direção à Meta do Produto, mas precisa atender aos padrões de qualidade definidos, sem atalhos que gerem débito técnico.'},
                            {'text': 'Priorize o lançamento de valor: Embora a liberação não seja obrigatória ao final da Sprint, o Product Owner deve procurar liberar o Incremento sempre que for benéfico para o negócio.'},
                            {'text': 'Ferramentas Práticas', 'bold': True},
                            {'text': 'Ferramentas complementares que ajudam times Scrum a terem mais visibilidade e controle.'},                             
                         ],
                        'icon': 'planning.png',
                        'modal_icon': 'planning_rx.png',
                        'bg_color': '#8c52ff'
                    },
                    {
                        'titulo': 'Gráfico Bourdown',
                        'subtitulo': 'O Gráfico Burndown é a ferramenta visual que funciona como um termômetro, ele mostra a relação entre o trabalho que resta versus o tempo que resta em uma Sprint.',
                        'texto': [
                            {'text': 'Objetivo', 'bold': True},
                            {'text': 'O propósito: Acompanhar o progresso do Time Scrum para ver se estamos no caminho certo para alcançar a Meta da Sprint (o alvo) no tempo definido.'},
                            {'text': 'A função: Identificar desvios (atrasos ou adiantamentos) do plano rapidamente, permitindo que o time faça adaptações imediatas.'},                        
                            {'text': 'Benefícios', 'bold': True},
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
                        'icon': 'planning.png',
                        'modal_icon': 'planning_rx.png',
                        'bg_color': '#8c52ff'
                    }              
                                                                                 
                ],
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
