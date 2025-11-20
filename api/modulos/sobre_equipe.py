# Arquivo de configuração para o módulo "Sobre a Equipe"

def get_sobre_equipe():
    """Retorna a configuração para o módulo da equipe."""
    return {
        'sections': {
            'sobre-equipe': {
                'titulo_modulo': 'Conheça a Equipe',
                'numero_modulo': '🏆',
                'descricao_secao': 'Conheça os desenvolvedores por trás deste projeto.',
                'template': 'sobre-equipe.html'
            }
        },
        'quiz': False,
        'primeira_secao': 'sobre-equipe'
    }