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
                'titulo_complementar': 'APOSTILA MÓDULO 2',
                'url_download_complementar': 'routes.download',
                'url_download_key': 'modulo2_apostila',
                'url_anterior': 'routes.module_route',
                'url_anterior_params': {'module_name': 'modulo1', 'section_name': 'modulo1s2'},
                'url_proximo': 'routes.module_route',
                'url_proximo_params': {'module_name': 'modulo3', 'section_name': 'modulo3'},
                'mostrar_exercicios': True,
                'cards': [
                    {
                        'titulo': 'Product Owner',
                        'subtitulo': 'O guardião da visão do produto',
                        'texto': 'Responsável por maximizar o valor do trabalho realizado pelo time. Gerencia o backlog do produto e toma decisões estratégicas.'
                    },
                    {
                        'titulo': 'Scrum Master',
                        'subtitulo': 'O facilitador do processo',
                        'texto': 'Garante que o Scrum seja aplicado corretamente, facilita eventos e remove impedimentos para o time.'
                    },
                    {
                        'titulo': 'Equipe de Desenvolvimento',
                        'subtitulo': 'Os criadores do produto',
                        'texto': 'Time auto-organizado responsável por transformar o backlog em incrementos funcionais de alta qualidade.'
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
    'modulo3_apostila': 'Módulo 3 Eventos do Scrum.pdf',
    'modulo2_apostila': 'Apostila Módulo 2.pdf' # Assumindo que o nome do arquivo é este
}
