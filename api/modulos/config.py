from .modulo1 import get_modulo1
from .modulo2 import get_modulo2
from .modulo3 import get_modulo3
from .modulo4 import get_modulo4
from .modulo5 import get_modulo5
# from .modulo6 import get_modulo6
from .sobre_equipe import get_sobre_equipe


MODULES_CONFIG = {
    'modulo1': get_modulo1(),
    'modulo2': get_modulo2(),
    'modulo3': get_modulo3(),
    'modulo4': get_modulo4(),
    'modulo5': get_modulo5(),
    # 'modulo6': get_modulo6(),
    'sobre-equipe': get_sobre_equipe(),
}

# Download mappings
DOWNLOADS = {
    'modulo1_secao1': 'modulo_1_secao_1.pdf',
    'modulo1_secao2': 'modulo_1_secao_2.pdf',
    'modulo2': 'modulo_2.pdf',
    'modulo3_apostila': 'modulo_3_eventos_scrum.pdf',
    'modulo4_apostila':'modulo_4_artefatos.pdf',
    'modulo5_apostila':'Apostila_modulo5.pdf'
}
