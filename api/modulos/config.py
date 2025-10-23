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
                'descricao_secao': 'Descubra os três papéis fundamentais do Scrum e como eles trabalham juntos para criar valor.<br>Clique nos cards abaixo para descobrir mais sobre cada um:',
                'conteudo_complementar': True,
                'titulo_complementar': 'PAPÉIS DO SCRUM E SUAS INTERAÇÕES',
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
                            
                            'Principais Responsabilidades:',
                            'Gerenciar e priorizar o Backlog do Produto.',
                            'Garantir que o time entenda os itens do backlog.',
                            'Tomar decisões sobre o produto.',
                            'Aceitar ou rejeitar incrementos de trabalho.',
                            'Garantir que todo o backlog do produto seja visível, transparente e claro para todos os interessados, mostrando o que o time scrum deve buscar.',
                            'Habilidades essenciais:',
                            'Visão estratégica do produto.',
                            'Excelente comunicação.',
                            'Tomada de decisões.',
                            'Conhecimento do negócio.',
                            'Habilidades de negociação.'
                        ],
                        'icon': 'File_Search.png',
                        'modal_icon': 'File_Search_az.png',
                        'bg_color': '#83C7E9' 
                    },
                    {


                        'titulo': 'Scrum Master',
                        'subtitulo': 'O scrum master é o responsável por garantir que o Scrum seja entendido e aplicado, para que o time scrum esteja aderindo aos valores do scrum, às práticas e às regras e aos princípios.',
                        'texto': [
                            'Principais Responsabilidade:',
                            'Facilitar eventos do scrum.', 
                            'Orientar o time em práticas ágeis.',
                            'Planejar implementações de scrum dentro da organização.',
                            'Treinar o time para ser mais produtivo.',
                            'Promover melhoria contínua.',
                            'Habilidades Essenciais:',
                            'Facilitação das reuniões.',
                            'Resolução de conflitos.',
                            'Mentor do time.',
                            'Conhecimento profundo do scrum.', 
                            'Liderança.'
                        ],
                        'icon': 'User_Voice.png',
                        'modal_icon': 'User_Voice_rx.png',
                        'bg_color': '#7E5DA5'   
                    },
                    {


                        'titulo': 'Equipe de Desenvolvimento',
                        'subtitulo': 'O time de desenvolvimento é responsável por executar o desenvolvimento e transformar o backlog do produto em incrementos de funcionalidade, criando um sistema pronto que possa ser entregue ao cliente.',
                        'texto': [
                            'Principais Responsabilidades:',
                            'Criar incrementos de produto de alta qualidade.',
                            'Auto-organização das tarefas.',
                            'Estimar itens do backlog.',
                            'Colaborar para atingir os objetivos da Sprint.', 
                            'Manter padrões técnicos elevados.',
                            'Habilidades Essenciais:',
                            'Habilidades técnicas variadas:',
                            'multidisciplinariedade e interdisciplinariedade.',
                            'Trabalho em equipe.',
                            'Auto-organização.',
                            'Comprometimento com qualidade.',
                            'Comunicação efetiva.'
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
                'titulo_modulo': 'Os Eventos do Scrum',
                'numero_modulo': 3,
                'descricao_secao': 'Conheça os cinco eventos essenciais que estruturam o framework Scrum.',
                'conteudo_complementar': True,
                'titulo_complementar': 'OS EVENTOS DO SCRUM',
                'url_download_complementar': 'routes.download',
                'url_download_key': 'modulo3_apostila',
                'url_anterior': 'routes.module_route',
                'url_anterior_params': {'module_name': 'modulo2', 'section_name': 'modulo2'},
                'url_proximo': None,
                'mostrar_exercicios': True,
                'template': 'modulo3.html'
            }
        },
        'quiz': True
    }
}

# Download mappings
DOWNLOADS = {
    'modulo1_secao1': 'Módulo 1 - Seção 1.pdf',
    'modulo1_secao2': 'Módulo 1 - Seção 2.pdf',
    'modulo2':'Apostila Módulo 2.pdf',
    'modulo3_apostila': 'Módulo 3 Eventos do Scrum.pdf',
}
