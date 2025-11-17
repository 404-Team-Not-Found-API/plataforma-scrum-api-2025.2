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