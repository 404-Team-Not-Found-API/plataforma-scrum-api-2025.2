// Este script transforma o questionário em uma aplicação dinâmica
// Ele intercepta as ações do usuário, comunica-se com o backend via AJAX, e atualiza apenas a seção do quiz, sem recarregar a página.

// Armazena os dados da próxima questão recebidos da API para evitar chamadas desnecessárias.
let nextQuestionData = null;

document.addEventListener('DOMContentLoaded', function () {
    // Adiciona 'event listeners' aos botões de controle do quiz assim que a página carrega.
    const confirmBtn = document.getElementById('confirm-btn');
    const nextBtn = document.getElementById('next-btn');

    if (confirmBtn) {
        confirmBtn.addEventListener('click', handleConfirm); // Lida com a verificação da resposta.
    }
    if (nextBtn) {
        nextBtn.addEventListener('click', handleNext); // Carrega a próxima questão.
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

        // Se a resposta da API indica que não há próxima questão, finaliza o quiz.
        if (data.next_question === null) { // Esta foi a última questão
            displayFinalScore(data.score, data.total);
        } else {
            displayFeedback(data); // Mostra o feedback de Certo/Errado.
            toggleButtons(true); // Esconde "Confirmar" e mostra "Próxima"/"Anterior".
        }
    })
    .catch(error => {
        console.error('Erro ao verificar a resposta:', error);
        alert("Erro ao verificar a resposta. Tente novamente.");
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

    nextQuestion.alternativas.forEach((alt, index) => {
        const alternativeHTML = `
            <div>
                <label class="flex items-center space-x-3 p-3 rounded-lg border hover:bg-gray-100 cursor-pointer">
                    <input type="radio" name="answer" value="${index + 1}" class="form-radio h-5 w-5 text-emerald-500" required>
                    <span>${alt}</span>
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
    const currentIndex = parseInt(document.getElementById('question_index').value);
    const totalQuestions = parseInt(document.getElementById('total_questions').value);

    if (showNav) { // Se for para mostrar os botões de navegação (após confirmar).
        confirmBtn.classList.add('d-none');
        
        if (currentIndex + 1 < totalQuestions) {
            nextBtn.classList.remove('d-none');
        } else {
            nextBtn.classList.add('d-none');
        }
    } else { // Se for para mostrar o botão de confirmar (ao carregar uma nova questão).
        confirmBtn.classList.remove('d-none');
        nextBtn.classList.add('d-none');
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