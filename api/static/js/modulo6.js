/**
 * Gera um relatório em PDF a partir do conteúdo do formulário de planejamento da Sprint.
 * Esta versão solicita o PDF diretamente do servidor (backend), que o gera com WeasyPrint.
 */
function gerarPDFConsolidado() {
    const button = document.querySelector('button[onclick="gerarPDFConsolidado()"]');
    const originalButtonText = button.innerHTML;
    button.disabled = true;
    button.innerHTML = 'Gerando PDF...';

    // 1. Coleta os dados do formulário.
    const metaSprint = document.getElementById('sprint_goal').value;
    const backlogItens = document.getElementById('sprint_backlog').value;
    const riscos = document.getElementById('riscos_identificados').value;

    // 2. Envia os dados para o backend.
    fetch('/gerar-relatorio-pdf-modulo6', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            meta_sprint: metaSprint,
            backlog_itens: backlogItens,
            riscos: riscos
        })
    })
    .then(response => {
        if (response.ok) {
            return response.blob(); // Pega o arquivo PDF retornado pelo servidor.
        }
        throw new Error('Falha ao gerar o PDF no servidor.');
    })
    .then(blob => {
        // 3. Cria um link temporário para o arquivo e simula um clique para iniciar o download.
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = 'relatorio_planejamento_sprint.pdf';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
    })
    .catch(error => {
        console.error('Erro ao gerar relatório:', error);
        alert('Ocorreu um erro ao gerar o relatório. Tente novamente.');
    })
    .finally(() => {
        // 4. Restaura o botão ao estado original.
        button.disabled = false;
        button.innerHTML = originalButtonText;
    });
}
