// Este script transforma o questionário em uma aplicação dinâmica
// Ele intercepta as ações do usuário, comunica-se com o backend via AJAX, e atualiza apenas a seção do quiz, sem recarregar a página.

// Armazena os dados da próxima questão recebidos da API para evitar chamadas desnecessárias.
let nextQuestionData = null;

// Dados dos desafios para o Mini Desafio Prático
const challenges = {
    scrumMaster: {
        title: "Desafio de Comunicação na Sprint",
        description: "Você é o Scrum Master de um time que está enfrentando sérios problemas: os desenvolvedores reclamam que os requisitos não estão claros, o Product Owner se sente frustrado porque as entregas não atendem às expectativas, e nas Daily Scrums as pessoas mal se comunicam. A sprint está atrasada e a tensão está alta.",
        question: "❓ Qual seria sua primeira ação como Scrum Master para resolver essa situação?",
        options: [
            {
                id: 'a', 
                text: '1. Facilitar uma Retrospectiva de Emergência.', 
                subtitle: [
                    "Soft Skills:",
                    "Pensamento Crítico: questionar e esclarecer requisitos",
                    "Colaboração: envolver devs na anáise",
                    "Comunicação: alinhar entendimento"
                ],
                feedback: 'Excelente escolha! A retrospectiva de emergência é uma ferramenta poderosa para criar um espaço seguro onde todos podem expressar suas frustrações. Ao usar empatia e escuta ativa, você permite que o time identifique a raiz dos problemas. Esta abordagem demonstra maturidade em resolução de conflitos e foco no fator humano.',
                outcome: 'O time identifica que falta refinamento adequado e alinhamento de expectativas'
            },
            {
                id: 'b', 
                text: '2. Reorganizar as Daily Scrums com foco em colaboração.', 
                subtitle: [
                    "Soft Skills:",
                    "Comunicação: estabelecer formato claro",
                    "Facilitação: garantir que todos participem",
                    "Foco: manter conversas objetivas"
                ],
                feedback: 'Boa abordagem! Melhorar as Daily Scrums pode realmente ajudar na identificação precoce de problemas. Ao estabelecer um formato claro e garantir participação de todos, você está atacando diretamente o problema de comunicação. Porém, pode ser que os problemas sejam mais profundos e exijam uma conversa mais ampla primeiro.',
                outcome: 'Impedimentos são identificados mais cedo e o time colabora nas soluções'
            },
            {
                id: 'c', 
                text: '3. Implementar sessões de Refinamento Estruturadas.', 
                subtitle: [
                    "Soft Skills",
                    "Pensamento Crítico: queestionar e esclarecer requisitos", 
                    "Colaboração: envolver devs na análise",
                    "Comunicação: alinhar entendimento"
                    ], 
                feedback: 'Ótima escolha técnica! O refinamento estruturado resolve diretamente o problema de requisitos não claros. Ao envolver desenvolvedores na análise desde o início, você promove colaboração e alinhamento. Esta é uma solução preventiva excelente, mas talvez seja necessário resolver primeiro as tensões existentes no time.',
                outcome: 'Product Owner e desenvolvedores chegam a entendimento comum antes da sprint'
            },
            {
                id: 'd', 
                text: '4. Realizar coaching individual com PO e membros do time.', 
                subtitle: [
                    "Soft Skills",
                    "Empatia: entender pressões individuais", 
                    "Mentoria: desenvolver habilidades", 
                    "Confiança: criar relação de apoio"
                ], 
                feedback: 'Abordagem válida e demonstra preocupação com as pessoas! O coaching individual pode revelar problemas pessoais ou de entendimento de papéis que afetam o time. Porém, em uma situação de crise com o time todo, pode ser mais eficaz primeiro reunir todos para uma conversa coletiva, e depois partir para conversas individuais se necessário.',
                outcome: 'Relacionamentos melhoram e cada pessoa entende melhor seu papel'
            }
        ],
        correct: 'a'
    },
    developer: {
        title: "Desafio Técnico e Colaboração",
        description: "Você é desenvolvedor(a) em um time Scrum. Durante a sprint, você percebe que uma funcionalidade crítica tem requisitos ambíguos e pode ser implementada de três formas diferentes. O prazo está apertado, o PO está em reuniões o dia todo, e outros desenvolvedores estão sobrecarregados com suas próprias tasks.",
        question: "❓ Como você procede nesta situação?",
        options: [
            {
                id: 'a',
                text: '1. implementar baseado no seu melhor entendimento e ajustar depois no feedback ', 
                subtitle: [
                    "Soft Skills", 
                    "Autonomia: tomar decisões técnicas", 
                    "Adaptabilidade: estar pronto para ajustar", 
                    "Proatividade: não esperar para agir"
                ], 
                feedback: 'Demonstra iniciativa, mas pode gerar retrabalho. Em Scrum, é melhor buscar clareza antes de implementar, mesmo que isso signifique esperar um pouco. A autonomia é importante, mas deve vir acompanhada de alinhamento com o time e PO.', 
                outcome: 'Você entrega algo, mas pode não ser exatamente o esperado, gerando retrabalho'
            },
            {
                id: 'b', 
                text: '2. Documentar as três opções e pedir uma reunião rápida de 15 minutos com o PO', 
                subtitle: [
                    "Soft Skills", 
                    "Comunicação: apresentar opções claramente", 
                    "Pensamento Crítico: analisar alternativas", 
                    "Assertividade: buscar o alinhamento necessário"
                ], 
                feedback: 'Excelente escolha! Você demonstra pensamento crítico ao analisar as opções, comunicação ao documentá-las, e assertividade ao buscar o alinhamento necessário. Esta abordagem evita retrabalho e mostra maturidade profissional. Em times ágeis, comunicação proativa é fundamental.', 
                outcome: 'O PO agradece a análise, escolhe a melhor opção, e você implementa com confiança'
            },
            {
                id: 'c', 
                text: '3. Compartilha a dúvida na Daily Scrum do dia seguinte e aguardar orientação', 
                subtitle: [
                    "Soft Skills", 
                    "Transparência: expor impedimentos", 
                    "Paciência: esperar momento certo", 
                    "Colaborção: envolver o time"
                ], 
                feedback: 'A transparência é positiva, mas esperar até a próxima Daily pode atrasar desnecessariamente. Em situações críticas, é melhor buscar alinhamento imediato. Scrum valoriza comunicação frequente, não apenas nas cerimônias formais. Considere comunicação assíncrona ou uma conversa rápida.', 
                outcome: 'Você perde um dia de trabalho, mas eventualmente consegue clareza'
            },
            {
                id: 'd', 
                text: '4. Pedir ajuda a outro desenvolvedor do time para decidir juntos', 
                subtitle: [
                    "Soft Skills", 
                    "Colaboração: buscar apoio dos pares", 
                    "Humildade: reconhecer a necessidade de ajuda", 
                    "Confiança: apoiar-se no time"
                ], 
                feedback: 'Boa iniciativa de colaboração! Pair programming e decisões conjuntas são práticas ágeis valiosas. Porém, para questões de requisitos e priorização, o PO é quem tem a visão do produto. O ideal seria envolver o colega na análise E buscar validação com o PO.', 
                outcome: 'Vocês decidem juntos, mas ainda existe risco de não estar alinhado com a visão do PO'
            }
        ],
        correct: 'b'
    },
    productOwner: {
        title: "Desafio de Priorização sob Pressão",
        description: "Você é o Product Owner. Faltam 3 dias para o fim da sprint e o time está conseguindo entregar 70% do planejado. O CEO liga pedindo uma funcionalidade urgente para uma demo com investidores daqui a 2 dias. O time já está no limite e expressa preocupação com qualidade se adicionar mais trabalho.",
        question: "❓ Qual sua decisão como Product Owner?",
        options: [
            {
                id: 'a', 
                text: '1. Adicionar a funcionalidade urgente e pedir ao time que "dê um jeito"', 
                subtitle: [
                    "Soft Skills", 
                    "Assertividade: defender a necessidade do negócio", 
                    "Coragem: tomar decisões difíceis"
                ], 
                feedback: 'Esta decisão pode prejudicar a relação de confiança com o time e comprometer a qualidade. Como PO, seu papel não é apenas trazer demandas, mas proteger o time de sobrecarga. Scrum valoriza entregas sustentáveis. Há melhores formas de lidar com urgências.', 
                outcome: 'O time se sobrecarrega, qualidade cai, e a confiança entre PO e time é prejudicada'
            },
            {
                
                id: 'b', 
                text: '2. Negociar com o CEO: explica a situação, oferece uma versão simplificada ou adia a demo.', 
                subtitle: [
                    "Soft Skills", 
                    "Comunicação: gerenciar expectativas", 
                    "Negociaçâo: buscar alternativas",
                    "Coragem: dizer não quando necessário",
                    "Pensamento Crítico: analisar opções"
                ], 
                feedback: 'Excelente decisão! Você demonstra coragem ao gerenciar expectativas do CEO, pensamento crítico ao buscar alternativas viáveis, e respeito pelo time. Um PO maduro sabe que proteger a sustentabilidade do time é proteger a empresa no longo prazo. Esta é a essência do papel de PO em Scrum.', 
                outcome: 'CEO entende, aceita versão simplificada, time entrega com qualidade'
            },
            {
                id: 'c', 
                text: '3. Remover itens do backlog atual e adicionar funcionalidade urgente no lugar', 
                subtitle: [
                    "Soft Skills", 
                    "Priorização: ajustar o escopo conforme necessidade", 
                    "Flexibilidade: adaptar planos", 
                    "Comunicação: realinhar expectativas"
                ], 
                feedback: 'Abordagem válida em termos de gestão de escopo, mas você precisa comunicar melhor com todos os stakeholders. Mudanças de última hora devem ser exceção, não regra. Considere também que há uma razão pela qual aqueles itens estavam priorizados - removê-los tem impacto no produto.', 
                outcome: 'A funcionalidade urgente é entregue, mas outros stakeholders ficam frustrados com mudanças'
            },
            {
                id: 'd', 
                text: '4. Reunir time, CEO e stakeholders para decisão transparente e colaborativa', 
                subtitle: [
                    "Soft Skills", 
                    "Facilitação: mediar conversas difíceis", 
                    "Transparência: expor realidade", 
                    "Colaboração: decisões em conjunto",
                    "Empatia: entender todas as expectativas"
                ], 
                feedback: 'Muito boa abordagem! Você promove transparência, que é um valor Scrum fundamental. Envolver todos na decisão cria alinhamento e comprometimento compartilhado. No entanto, cuidado para não levar muito tempo nessa reunião - em situações urgentes, você como PO precisa ser capaz de decidir rapidamente também, após ouvir o time.', 
                outcome: 'Todos entendem os trade-offs e decidem juntos o melhor caminho'
            }
        ],
        correct: 'd'
    }
};

document.addEventListener('DOMContentLoaded', function () {
    // Adiciona 'event listeners' aos botões de controle do quiz assim que a página carrega.
    const confirmBtn = document.getElementById('confirm-btn');
    const nextBtn = document.getElementById('next-btn');
    const prevBtn = document.getElementById('prev-btn');

    if (confirmBtn) {
        confirmBtn.addEventListener('click', handleConfirm); // Lida com a verificação da resposta.
    }
    if (nextBtn) {
        nextBtn.addEventListener('click', handleNext); // Carrega a próxima questão.
    }
    if (prevBtn) {
        prevBtn.addEventListener('click', handlePrev); // Volta para a questão anterior.
    }
});

// Função chamada ao clicar em "Confirmar".
function handleConfirm() {
    const form = document.getElementById('quiz-form');
    const formData = new FormData(form);
    const moduleName = formData.get('module_name');
    const questionIndex = parseInt(formData.get('question_index'));
    const answer = formData.get('answer');

    // Validação no frontend para garantir que uma resposta foi selecionada.
    if (!answer) {
        alert('Por favor, selecione uma resposta.');
        return;
    }

    // Desabilita os inputs para prevenir múltiplas respostas.
    document.querySelectorAll('input[name="answer"]').forEach(input => input.disabled = true);
    const confirmBtn = document.getElementById('confirm-btn');
    confirmBtn.disabled = true;
    confirmBtn.textContent = 'Verificando...';

    // Requisição AJAX (fetch) para a API de verificação.
    fetch(`/verificar-resposta/${moduleName}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question_index: questionIndex, answer: answer }),
    })
    .then(response => response.json())
    .then(data => {
        confirmBtn.disabled = false;
        confirmBtn.textContent = 'Confirmar';

        // Armazena os dados da próxima questão para uso posterior.
        nextQuestionData = data;

        if (moduleName === 'modulo5') {
            // Para o módulo 5, não há feedback, avança diretamente
            if (data.resultado) {
                // Última pergunta, mostra o resultado do diagnóstico
                displayDiagnosticResult(data.resultado);
            } else {
                // Avança para a próxima pergunta
                handleNext();
            }
        } else {
            // Lógica para outros módulos
            // Se a resposta da API indica que não há próxima questão, finaliza o quiz.
            if (data.next_question === null) { // Esta foi a última questão
                displayFinalScore(data.score, data.total);
            } else {
                displayFeedback(data); // Mostra o feedback de Certo/Errado.
                toggleButtons(true); // Esconde "Confirmar" e mostra "Próxima"/"Anterior".
            }
        }
    })
    .catch(error => {
        console.error('Erro ao verificar a resposta:', error);
        // Removido o alert para não mostrar a mensagem de erro
        document.querySelectorAll('input[name="answer"]').forEach(input => input.disabled = false);
        confirmBtn.disabled = false;
        confirmBtn.textContent = 'Confirmar';
    });
}

// Funções para lidar com a navegação.
// A lógica agora é mais simples: se os dados da próxima questão existem, atualiza a tela.
function handleNext() {
    if (nextQuestionData && nextQuestionData.next_question) {
        updateQuestion(nextQuestionData.next_question, nextQuestionData.next_question_index, nextQuestionData.total_questions);
        toggleButtons(false); // Mostra "Confirmar" e esconde os botões de navegação.
        nextQuestionData = null; // Limpa os dados após o uso.
    }
}

// Função para lidar com a navegação para a questão anterior.
function handlePrev() {
    const currentIndex = parseInt(document.getElementById('question_index').value);
    const totalQuestions = parseInt(document.getElementById('total_questions').value);
    const moduleName = document.getElementById('quiz-form').elements['module_name'].value;

    if (currentIndex > 0) {
        const prevIndex = currentIndex - 1;

        // Para módulos 1-4, precisamos buscar a pergunta anterior do backend
        if (moduleName !== 'modulo5') {
            fetch(`/verificar-resposta/${moduleName}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question_index: prevIndex, answer: null, action: 'prev' }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.prev_question) {
                    updateQuestion(data.prev_question, data.prev_question_index, data.total_questions);
                    toggleButtons(false); // Mostra "Confirmar" e esconde os botões de navegação.
                }
            })
            .catch(error => {
                console.error('Erro ao carregar a questão anterior:', error);
            });
        } else {
            // Para módulo 5, as perguntas estão no frontend, então podemos navegar diretamente
            if (window.modulo5Questions && window.modulo5Questions[prevIndex]) {
                const prevQuestion = window.modulo5Questions[prevIndex];
                updateQuestion(prevQuestion, prevIndex, totalQuestions);
                toggleButtons(false); // Mostra "Confirmar" e esconde os botões de navegação.
            }
        }
    }
}

// Função para exibir o feedback (Certo/Errado) e a explicação.
function displayFeedback(data) {
    const feedbackBox = document.getElementById('feedback-box');
    const feedbackText = document.getElementById('feedback-text');
    const feedbackExplanation = document.getElementById('feedback-explanation');

    // Limpa classes antigas e adiciona as novas com base na resposta.
    feedbackBox.classList.remove('d-none', 'bg-emerald-100', 'text-emerald-800', 'bg-red-100', 'text-red-800');

    if (data.correct) {
        feedbackBox.classList.add('bg-emerald-100', 'text-emerald-800');
        feedbackText.innerHTML = '<strong>Correto!</strong>';
    } else {
        feedbackBox.classList.add('bg-red-100', 'text-red-800');
        feedbackText.innerHTML = `<strong>Incorreto.</strong>`;
    }

    feedbackExplanation.textContent = data.explanation;
}

// Função para atualizar dinamicamente a interface com os dados da nova pergunta.
function updateQuestion(nextQuestion, nextIndex, total) {
    document.getElementById('question-counter').textContent = `Questão ${nextIndex + 1} de ${total}`;

    // Atualiza a barra de progresso dinamicamente.
    const progressBar = document.getElementById('progress-bar');
    const progressPercentage = ((nextIndex + 1) / total) * 100;
    progressBar.style.width = `${progressPercentage}%`;

    document.getElementById('question-title').textContent = nextQuestion.pergunta;

    // Limpa as alternativas antigas e cria o HTML para as novas.
    const alternativesContainer = document.querySelector('.alternatives-container');
    alternativesContainer.innerHTML = '';

    const moduleName = document.getElementById('quiz-form').elements['module_name'].value;

    nextQuestion.alternativas.forEach((alt, index) => {
        let value, text;
        if (moduleName === 'modulo5') {
            // Para módulo 5, alt é um objeto {id, text}
            value = alt.id;
            text = alt.text;
        } else {
            // Para outros módulos, alt é uma string
            value = index + 1;
            text = alt;
        }
        const alternativeHTML = `
            <div>
                <label class="flex items-center space-x-3 p-3 rounded-lg border hover:bg-gray-100 cursor-pointer">
                    <input type="radio" name="answer" value="${value}" class="form-radio h-5 w-5 text-emerald-500" required>
                    <span>${text}</span>
                </label>
            </div>
        `;
        alternativesContainer.insertAdjacentHTML('beforeend', alternativeHTML);
    });

    // Garante que os inputs de resposta estejam habilitados para a nova questão.
    document.querySelectorAll('input[name="answer"]').forEach(input => input.disabled = false);

    document.getElementById('question_index').value = nextIndex;
    document.getElementById('feedback-box').classList.add('d-none');
}

// Função para gerenciar a visibilidade dos botões
function toggleButtons(showNav) {
    const confirmBtn = document.getElementById('confirm-btn');
    const nextBtn = document.getElementById('next-btn');
    const prevBtn = document.getElementById('prev-btn');
    const currentIndex = parseInt(document.getElementById('question_index').value);
    const totalQuestions = parseInt(document.getElementById('total_questions').value);
    const moduleName = document.getElementById('quiz-form').elements['module_name'].value;

    if (showNav) { // Se for para mostrar os botões de navegação (após confirmar).
        confirmBtn.classList.add('d-none');

        if (currentIndex + 1 < totalQuestions) {
            nextBtn.classList.remove('d-none');
        } else {
            nextBtn.classList.add('d-none');
        }

        // Mostra o botão anterior apenas se não for a primeira questão e não for módulo 5
        if (currentIndex > 0 && moduleName !== 'modulo5') {
            prevBtn.classList.remove('d-none');
        } else {
            prevBtn.classList.add('d-none');
        }
    } else { // Se for para mostrar o botão de confirmar (ao carregar uma nova questão).
        confirmBtn.classList.remove('d-none');
        nextBtn.classList.add('d-none');
        // Mostra o botão anterior apenas se não for a primeira questão
        if (currentIndex > 0) {
            prevBtn.classList.remove('d-none');
        } else {
            prevBtn.classList.add('d-none');
        }
    }
}

// Função para exibir a tela de resultado final.
function displayFinalScore(score, total) {
    const quizContainer = document.getElementById('secao-exercicios');
    quizContainer.innerHTML = `
        <h3 class="text-2xl font-bold mb-6 text-center">Questionário Finalizado!</h3>
        <p class="text-xl text-center mb-4">Sua pontuação: <strong>${score} de ${total}</strong></p>
        <div class="mt-6 flex justify-center gap-4">
            <a href="${window.location.href}" class="bg-gray-300 hover:bg-gray-600 text-black px-6 py-3 rounded-full font-semibold">
                Refazer Exercícios
            </a>
        </div>
    `;
}

// Função para exibir o resultado do diagnóstico do módulo 5
function displayDiagnosticResult(resultado) {
    const resultSection = document.getElementById('result-section');
    const resultFeedback = document.getElementById('result-feedback');
    const resultDetails = document.getElementById('result-details');

    resultFeedback.textContent = resultado.feedback_geral;
    resultDetails.textContent = resultado.feedback_detalhado;

    resultSection.classList.remove('d-none');

    // Esconde o formulário do quiz
    document.getElementById('quiz-form').style.display = 'none';
}

// Funções para o Mini Desafio Prático
function selectRole(role) {
    document.getElementById('role-selection').classList.add('d-none');
    document.getElementById('challenge-section').classList.remove('d-none');

    const challenge = challenges[role];
    document.getElementById('challenge-title').textContent = challenge.title;
    document.getElementById('challenge-description').textContent = challenge.description;
    document.getElementById('challenge-question').textContent = challenge.question;

    const optionsContainer = document.getElementById('challenge-options');
    optionsContainer.innerHTML = '';

    challenge.options.forEach(option => {
        // Cria o HTML para a lista de subtítulos, se existir
        let subtitleHTML = '';
        if (option.subtitle && Array.isArray(option.subtitle)) {
            subtitleHTML = `
                <div class="challenge-subtitle-container mt-2">
                    <ul class="challenge-subtitle-list">
                        ${option.subtitle.map(line => `<li>${line}</li>`).join('')}
                    </ul>
                </div>
            `;
        }

        const optionHTML = `
            <div class="challenge-option" onclick="selectOption('${option.id}')">
                <input type="radio" name="challenge-answer" id="option-${option.id}" value="${option.id}">
                <label for="option-${option.id}" style="cursor: pointer; margin-bottom: 0;">${option.text}</label>
                ${subtitleHTML}
            </div>
        `;
        optionsContainer.insertAdjacentHTML('beforeend', optionHTML);
    });

    // Adiciona event listener para habilitar o botão de envio
    document.querySelectorAll('input[name="challenge-answer"]').forEach(radio => {
        radio.addEventListener('change', () => {
            document.getElementById('submit-challenge').disabled = false;
        });
    });
}

function backToRoleSelection() {
    document.getElementById('challenge-section').classList.add('d-none');
    document.getElementById('feedback-section').classList.add('d-none');
    document.getElementById('role-selection').classList.remove('d-none');
}

function selectOption(optionId) {
    // Remove selected class from all options
    document.querySelectorAll('.challenge-option').forEach(option => {
        option.classList.remove('selected');
    });

    // Add selected class to the clicked option
    const selectedOption = document.querySelector(`input[value="${optionId}"]`).parentElement;
    selectedOption.classList.add('selected');

    // Check the radio button
    document.querySelector(`input[value="${optionId}"]`).checked = true;

    // Enable the submit button
    document.getElementById('submit-challenge').disabled = false;
}

function submitChallenge() {
    const selectedAnswer = document.querySelector('input[name="challenge-answer"]:checked');
    if (!selectedAnswer) return;

    // Encontra o papel selecionado baseado no título do desafio
    const challengeTitle = document.getElementById('challenge-title').textContent;
    const role = Object.keys(challenges).find(key => challenges[key].title === challengeTitle);
    const challenge = challenges[role];
    const selectedOption = challenge.options.find(opt => opt.id === selectedAnswer.value);

    document.getElementById('challenge-section').classList.add('d-none');
    document.getElementById('feedback-section').classList.remove('d-none');

    document.getElementById('feedback-text').textContent = selectedOption.feedback;
    document.getElementById('feedback-outcome').textContent = selectedOption.outcome;
}
