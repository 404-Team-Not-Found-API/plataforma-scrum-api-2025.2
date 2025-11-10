/**
 * Gera um relatório em PDF a partir do conteúdo do formulário de planejamento da Sprint.
 */
function gerarPDFConsolidado() {
    // 1. Seleciona o formulário.
    const formElement = document.getElementById('formSprintPlanning');

    // 2. Constrói o HTML do relatório.
    const reportHTML = construirHTMLRelatorio(formElement);

    // 3. Cria um elemento temporário visível na viewport para garantir que o html2canvas possa capturá-lo.
    const tempContainer = document.createElement('div');
    tempContainer.innerHTML = reportHTML;
    tempContainer.style.position = 'fixed';
    tempContainer.style.top = '0';
    tempContainer.style.left = '0';
    tempContainer.style.width = '800px';
    tempContainer.style.minHeight = '600px';
    tempContainer.style.backgroundColor = 'white';
    tempContainer.style.zIndex = '9999';
    tempContainer.style.fontFamily = 'Arial, sans-serif';
    tempContainer.style.color = '#333';
    tempContainer.style.padding = '20px';
    tempContainer.style.boxSizing = 'border-box';
    tempContainer.style.overflow = 'hidden';

    // Adiciona ao body para que seja renderizado na viewport
    document.body.appendChild(tempContainer);

    // 4. Usa múltiplos setTimeout para garantir renderização completa
    setTimeout(() => {
        // Força reflow para garantir que o elemento foi renderizado
        tempContainer.offsetHeight;

        setTimeout(() => {
            const pdfOptions = {
                margin: 15,
                filename: 'relatorio_planejamento_sprint.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: {
                    scale: 2,
                    logging: true,
                    allowTaint: true,
                    useCORS: true,
                    backgroundColor: '#ffffff',
                    width: 800,
                    height: tempContainer.scrollHeight,
                    windowWidth: 800,
                    windowHeight: tempContainer.scrollHeight
                },
                jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
            };

            // 5. Gera o PDF e remove o elemento temporário
            html2pdf().set(pdfOptions).from(tempContainer).save().then(() => {
                document.body.removeChild(tempContainer);
            }).catch(error => {
                console.error('Erro ao gerar PDF:', error);
                document.body.removeChild(tempContainer);
            });
        }, 500);
    }, 1000);
}

/**
 * Constrói uma string HTML formatada com os dados do formulário.
 * @param {HTMLFormElement} formElement - O elemento do formulário.
 * @returns {string} - A string HTML do relatório.
 */
function construirHTMLRelatorio(formElement) {
    const dataAtual = new Date().toLocaleDateString('pt-BR');
    let perguntasRespostasHTML = '';

    // Itera sobre cada bloco de pergunta/resposta no formulário.
    formElement.querySelectorAll('.campo-formulario').forEach(bloco => {
        const perguntaEl = bloco.querySelector('label');
        const campoEl = bloco.querySelector('input, textarea');

        if (perguntaEl && campoEl) {
            const pergunta = perguntaEl.textContent.trim();
            // Converte quebras de linha do textarea para <br> para que apareçam no PDF.
            const resposta = (campoEl.value || "Não preenchido").replace(/\n/g, '<br>');

            perguntasRespostasHTML += `
                <div style="margin-bottom: 20px; page-break-inside: avoid;">
                    <h3 style="font-size: 16px; font-weight: bold; color: #0056b3; border-bottom: 1px solid #ccc; padding-bottom: 5px; margin-bottom: 10px;">${pergunta}</h3>
                    <div style="background-color: #f9f9f9; border-left: 4px solid #0056b3; padding: 10px; font-size: 14px; color: #333;">
                        ${resposta}
                    </div>
                </div>
            `;
        }
    });

    // Retorna o HTML completo, incluindo cabeçalho e o conteúdo coletado.
    return `
        <div style="font-family: Arial, sans-serif; color: #333; margin: 20px;">
            <header style="text-align: center; border-bottom: 2px solid #0056b3; padding-bottom: 10px; margin-bottom: 20px;">
                <h1 style="color: #0056b3; margin: 0;">Relatório de Planejamento da Sprint</h1>
                <p style="color: #555; font-size: 14px; margin-top: 5px;">Gerado em: ${dataAtual}</p>
            </header>
            <div>${perguntasRespostasHTML}</div>
        </div>
    `;
}
