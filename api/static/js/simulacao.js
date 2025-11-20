/**
 * api/static/js/simulacao.js
 * Lógica completa do Módulo 6: Simulação Scrum
 */

const Simulacao = {
    // Configurações e Estado
    prefixo: 'sprint_',
    totalEtapas: 6,
    projetos: [], // Será preenchido pelo HTML

    init: function(listaProjetos) {
        this.projetos = listaProjetos;
        
        // 1. Verificar se já existe projeto sorteado
        this.verificarEstadoInicial();

        // 2. Configurar ouvintes de eventos globais
        this.configurarEventos();

        // 3. Restaurar dados salvos nos formulários
        this.restaurarDadosFixos();
        this.restaurarBacklog();
        
        // 4. Atualizar visual (progresso e status)
        this.atualizarInterface();
    },

    configurarEventos: function() {
        // Botão de Sorteio
        const btnSortear = document.getElementById('btn-sortear');
        if(btnSortear) btnSortear.addEventListener('click', () => this.realizarSorteio());

        // Botão Iniciar Sprint
        const btnIniciar = document.getElementById('btn-iniciar');
        if(btnIniciar) btnIniciar.addEventListener('click', () => this.mostrarFases());

        // Salvamento Automático de Inputs Fixos (Evento 'input' é mais seguro que 'change')
        document.querySelectorAll('.save-target').forEach(input => {
            input.addEventListener('input', (e) => {
                const chave = this.prefixo + 'campo_' + e.target.id;
                localStorage.setItem(chave, e.target.value);
            });
        });

        // Botões de Concluir Etapa
        document.querySelectorAll('.btn-concluir').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const faseId = e.currentTarget.dataset.faseId;
                this.marcarEtapaConcluida(faseId);
            });
        });

        // Botão Adicionar Item no Backlog
        document.querySelectorAll('.btn-add-backlog').forEach(btn => {
            btn.addEventListener('click', (e) => this.adicionarItemBacklog(e));
        });

        // Atualizar Lista do Planning quando o modal abrir
        const modalPlanning = document.getElementById('modal-sprint_planning');
        if(modalPlanning) {
            modalPlanning.addEventListener('show.bs.modal', () => this.atualizarPlanning());
        }
    },

    // --- LÓGICA DE SORTEIO ---
    realizarSorteio: function() {
        const index = Math.floor(Math.random() * this.projetos.length);
        const projeto = this.projetos[index];
        
        localStorage.setItem(this.prefixo + 'projeto_id', projeto.id);
        this.exibirProjetoSorteado(projeto);
    },

    verificarEstadoInicial: function() {
        const pid = localStorage.getItem(this.prefixo + 'projeto_id');
        if (pid) {
            const projeto = this.projetos.find(p => p.id == pid);
            if (projeto) {
                this.exibirProjetoSorteado(projeto);
                this.mostrarFases(); // Se já tem projeto, vai direto pras fases
            }
        }
    },

    exibirProjetoSorteado: function(projeto) {
        // Preenche o cabeçalho da área de fases
        const tituloAtivo = document.getElementById('projeto-titulo-ativo');
        const descAtiva = document.getElementById('projeto-desc-ativo');
        
        if(tituloAtivo) tituloAtivo.innerText = projeto.nome;
        if(descAtiva) descAtiva.innerText = projeto.descricao;
        
        // Feedback visual no Grid de Sorteio (Opcional, mas elegante)
        document.querySelectorAll('.card-projeto-opcao').forEach(card => {
            card.classList.remove('border-primary', 'bg-light');
            card.querySelector('.icon-check').classList.remove('bi-check-square-fill', 'text-primary');
            card.querySelector('.icon-check').classList.add('bi-square');
        });

        const cardSorteado = document.getElementById('proj-card-' + projeto.id);
        if(cardSorteado) {
            cardSorteado.classList.add('border-primary', 'bg-light');
            const icon = cardSorteado.querySelector('.icon-check');
            icon.classList.remove('bi-square', 'text-muted');
            icon.classList.add('bi-check-square-fill', 'text-primary');
        }
    },

    mostrarFases: function() {
        document.getElementById('area-sorteio').classList.add('d-none');
        document.getElementById('area-fases').classList.remove('d-none');
    },

    // --- LÓGICA DE PERSISTÊNCIA E UI ---
    restaurarDadosFixos: function() {
        document.querySelectorAll('.save-target').forEach(input => {
            const valor = localStorage.getItem(this.prefixo + 'campo_' + input.id);
            if (valor) input.value = valor;
        });
    },

    marcarEtapaConcluida: function(faseId) {
        // Salva status
        localStorage.setItem(this.prefixo + 'status_' + faseId, 'concluido');
        
        // Fecha modal
        const modalEl = document.getElementById('modal-' + faseId);
        const modal = bootstrap.Modal.getInstance(modalEl);
        modal.hide();

        // Atualiza UI
        this.atualizarInterface();
    },

    atualizarInterface: function() {
        let concluidos = 0;

        // Verifica cada card de fase
        document.querySelectorAll('.card-fase').forEach(card => {
            const faseId = card.dataset.faseId; // Pega do data-attribute, mais seguro
            const status = localStorage.getItem(this.prefixo + 'status_' + faseId);

            const icon = card.querySelector('.status-icon');
            
            if (status === 'concluido') {
                concluidos++;
                card.classList.add('border-concluido');
                icon.classList.remove('bi-circle', 'text-muted');
                icon.classList.add('bi-check-circle-fill', 'text-concluido');
            } else {
                card.classList.remove('border-concluido');
                icon.classList.add('bi-circle', 'text-muted');
                icon.classList.remove('bi-check-circle-fill', 'text-concluido');
            }
        });

        // Atualiza Barra de Progresso
        const pct = (concluidos / this.totalEtapas) * 100;
        document.getElementById('barra-progresso').style.width = `${pct}%`;
        document.getElementById('texto-progresso').innerText = `${concluidos}/${this.totalEtapas}`;
    },

    // --- LÓGICA DO BACKLOG DINÂMICO ---
    adicionarItemBacklog: function(e, dadosItem = null) {
        const container = e.target ? e.target.closest('.lista-dinamica-container') : document.querySelector('.lista-dinamica-container');
        const wrapper = container.querySelector('.lista-items-wrapper');
        const schema = JSON.parse(container.dataset.schema); // Schema vem do HTML
        
        // Remove mensagem de vazio
        const emptyMsg = container.querySelector('.empty-state');
        if(emptyMsg) emptyMsg.classList.add('d-none');

        // Cria Linha
        const idUnico = dadosItem ? dadosItem.id : 'item_' + Date.now();
        const div = document.createElement('div');
        div.className = 'card p-3 mb-2 shadow-sm backlog-item position-relative';
        div.dataset.id = idUnico;

        let htmlCampos = '<div class="row g-2">';
        schema.forEach(campo => {
            const valor = dadosItem ? dadosItem[campo.id] : '';
            htmlCampos += `
                <div class="col" style="min-width: ${campo.width}">
                    <label class="form-label small fw-bold text-muted">${campo.label}</label>
                    <input type="${campo.tipo === 'select' ? 'text' : campo.tipo}" 
                           class="form-control form-control-sm backlog-input" 
                           data-campo="${campo.id}" 
                           value="${valor}"
                           ${campo.tipo === 'select' ? 'list="opts-'+campo.id+'"' : ''}>
                    ${campo.tipo === 'select' ? `<datalist id="opts-${campo.id}">${campo.options.map(o=>`<option value="${o}">`).join('')}</datalist>` : ''}
                </div>
            `;
        });
        htmlCampos += '</div><button type="button" class="btn-close position-absolute top-0 end-0 m-2 btn-remove-item"></button>';
        
        div.innerHTML = htmlCampos;
        wrapper.appendChild(div);

        // Eventos da nova linha
        div.querySelector('.btn-remove-item').addEventListener('click', () => {
            div.remove();
            this.salvarBacklog();
        });
        div.querySelectorAll('input').forEach(inp => {
            inp.addEventListener('input', () => this.salvarBacklog());
        });

        if(!dadosItem) this.salvarBacklog(); // Salva logo ao criar se for novo
    },

    salvarBacklog: function() {
        const itens = [];
        document.querySelectorAll('.backlog-item').forEach(div => {
            const item = { id: div.dataset.id };
            div.querySelectorAll('.backlog-input').forEach(inp => {
                item[inp.dataset.campo] = inp.value;
            });
            itens.push(item);
        });
        localStorage.setItem(this.prefixo + 'backlog_data', JSON.stringify(itens));
        this.atualizarPlanning(); // Sincroniza em tempo real
    },

    restaurarBacklog: function() {
        const dados = JSON.parse(localStorage.getItem(this.prefixo + 'backlog_data') || '[]');
        const btnAdd = document.querySelector('.btn-add-backlog');
        
        if (dados.length > 0 && btnAdd) {
            dados.forEach(item => this.adicionarItemBacklog({ target: btnAdd }, item));
        }
    },

    // --- LÓGICA DO PLANNING (CHECKBOXES) ---
    atualizarPlanning: function() {
        const wrapper = document.querySelector('.selecao-origem-wrapper');
        if(!wrapper) return;

        const itensBacklog = JSON.parse(localStorage.getItem(this.prefixo + 'backlog_data') || '[]');
        const selecionados = JSON.parse(localStorage.getItem(this.prefixo + 'planning_selected') || '[]');

        if(itensBacklog.length === 0) {
            wrapper.innerHTML = '<div class="text-muted p-3 text-center">Nenhum item no Backlog.</div>';
            return;
        }

        let html = '<div class="list-group">';
        itensBacklog.forEach(item => {
            const isChecked = selecionados.includes(item.id) ? 'checked' : '';
            // Tenta pegar o primeiro campo como título (geralmente 'titulo')
            const titulo = Object.values(item)[1] || 'Item sem nome'; 
            
            html += `
                <label class="list-group-item d-flex gap-2">
                    <input class="form-check-input flex-shrink-0 chk-planning" type="checkbox" value="${item.id}" ${isChecked}>
                    <span>${titulo}</span>
                </label>
            `;
        });
        html += '</div>';
        wrapper.innerHTML = html;

        // Listener dos checkboxes
        wrapper.querySelectorAll('.chk-planning').forEach(chk => {
            chk.addEventListener('change', () => {
                const novosSelecionados = Array.from(wrapper.querySelectorAll('.chk-planning:checked')).map(c => c.value);
                localStorage.setItem(this.prefixo + 'planning_selected', JSON.stringify(novosSelecionados));
            });
        });
    },

    // Lógica de Geração de PDF
    gerarPDF: function() {
        // 1. PREPARAÇÃO: Salvar posição de rolagem atual e ir para o topo
        const scrollAtual = window.scrollY;
        window.scrollTo(0, 0); // Garante que a "câmera" pegue o início do documento

        // 2. CLONAGEM: Cria cópia do template
        const template = document.getElementById('template-pdf');
        const clone = template.cloneNode(true);
        
        // Configura o clone
        clone.id = 'pdf-render-temp'; 
        clone.style.display = 'block';
        // Não usamos mais position: absolute/left: -9999px para evitar bugs de renderização.
        // Vamos colocar ele SOBRE o conteúdo atual com fundo branco, depois removemos.
        clone.style.position = 'absolute';
        clone.style.top = '0';
        clone.style.left = '0';
        clone.style.zIndex = '9999';
        clone.style.backgroundColor = '#fff';
        
        document.body.appendChild(clone);

        // 3. PREENCHIMENTO (Dados Gerais)
        clone.querySelector('.pdf-data').innerText = new Date().toLocaleDateString('pt-BR');
        
        const pid = localStorage.getItem(this.prefixo + 'projeto_id');
        const projeto = this.projetos.find(p => p.id == pid);
        if (projeto) clone.querySelector('.pdf-projeto-nome').innerText = projeto.nome;

        // Preenchimento de campos fixos via data-attribute
        clone.querySelectorAll('.pdf-field').forEach(el => {
            const fieldId = el.dataset.pdfField;
            const valor = localStorage.getItem(this.prefixo + 'campo_' + fieldId);
            if (valor) el.innerText = valor;
        });

        // 4. PREENCHIMENTO DO BACKLOG (Com novos campos!)
        const backlogData = JSON.parse(localStorage.getItem(this.prefixo + 'backlog_data') || '[]');
        const ulBacklog = clone.querySelector('.pdf-lista-backlog');
        ulBacklog.innerHTML = '';

        if (backlogData.length === 0) {
            ulBacklog.innerHTML = '<li style="color:#999">Nenhum item no backlog.</li>';
        } else {
            backlogData.forEach(item => {
                const li = document.createElement('li');
                li.style.marginBottom = '10px';
                li.style.borderBottom = '1px solid #eee';
                li.style.paddingBottom = '5px';

                // Monta o HTML do item com Descrição e Critérios (se existirem)
                const prio = item.prioridade ? `<span style="font-weight:bold; color:#0d6efd">[${item.prioridade}]</span> ` : '';
                const titulo = `<strong>${item.titulo || 'Item sem título'}</strong>`;
                const est = item.estimativa ? ` <small>(${item.estimativa})</small>` : '';
                
                let htmlItem = `<div>${prio}${titulo}${est}</div>`;
                
                // Adiciona Descrição se houver
                if (item.descricao) {
                    htmlItem += `<div style="font-size:12px; color:#666; margin-top:2px;"><em>Desc: ${item.descricao}</em></div>`;
                }
                // Adiciona Critérios se houver
                if (item.aceitacao) {
                    htmlItem += `<div style="font-size:12px; color:#666;"><em>Aceite: ${item.aceitacao}</em></div>`;
                }

                li.innerHTML = htmlItem;
                ulBacklog.appendChild(li);
            });
        }

        // 5. PREENCHIMENTO DO PLANNING
        const selecionados = JSON.parse(localStorage.getItem(this.prefixo + 'planning_selected') || '[]');
        const ulPlanning = clone.querySelector('.pdf-lista-planning');
        ulPlanning.innerHTML = '';

        if (selecionados.length === 0) {
            ulPlanning.innerHTML = '<li style="color:#999">Nenhum item selecionado.</li>';
        } else {
            const itensSprint = backlogData.filter(item => selecionados.includes(item.id));
            itensSprint.forEach(item => {
                const li = document.createElement('li');
                li.innerText = item.titulo || 'Item sem título';
                ulPlanning.appendChild(li);
            });
        }

        // 6. GERAÇÃO
        const content = clone.querySelector('.pdf-container');
        const opt = {
            margin:       10,
            filename:     `Sprint_Report_${Date.now()}.pdf`,
            image:        { type: 'jpeg', quality: 0.98 },
            html2canvas:  { scale: 2, useCORS: true, scrollY: 0 }, // Força scrollY 0
            jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
        };

        html2pdf().set(opt).from(content).save()
            .then(() => {
                document.body.removeChild(clone);
                window.scrollTo(0, scrollAtual); // Devolve usuário à posição original
            })
            .catch(err => {
                console.error("Erro PDF:", err);
                if(document.body.contains(clone)) document.body.removeChild(clone);
                window.scrollTo(0, scrollAtual);
            });
    }
};