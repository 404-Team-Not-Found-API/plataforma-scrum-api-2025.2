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
        document.getElementById('projeto-titulo').innerText = projeto.nome;
        document.getElementById('projeto-desc').innerText = projeto.texto;
        document.getElementById('projeto-icone').className = projeto.icone + ' fs-1';
        
        // Alterna visibilidade das áreas
        document.getElementById('intro-sorteio').classList.add('d-none');
        document.getElementById('resultado-sorteio').classList.remove('d-none');
    },

    mostrarFases: function() {
        // document.getElementById('area-sorteio').classList.add('d-none'); // Linha removida para manter a área de sorteio visível
        document.getElementById('area-fases').classList.remove('d-none');
        document.getElementById('funcionamento').classList.remove('d-none');

        // Esconde o botão "Iniciar Sprint" para evitar cliques repetidos
        document.getElementById('btn-iniciar').classList.add('d-none');
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

        let htmlCampos = '';
        schema.forEach(campo => {
            const valor = dadosItem ? dadosItem[campo.id] : '';
            let inputHtml;
            if (campo.tipo === 'textarea') {
                inputHtml = `<textarea class="form-control form-control-sm backlog-input" data-campo="${campo.id}" placeholder="${campo.placeholder || ''}">${valor}</textarea>`;
            } else if (campo.tipo === 'select') {
                inputHtml = `<input type="text" class="form-control form-control-sm backlog-input" data-campo="${campo.id}" value="${valor}" placeholder="${campo.placeholder || ''}" list="opts-${campo.id}">
                             <datalist id="opts-${campo.id}">${campo.options.map(o=>`<option value="${o}">`).join('')}</datalist>`;
            } else {
                inputHtml = `<input type="${campo.tipo}" class="form-control form-control-sm backlog-input" data-campo="${campo.id}" value="${valor}" placeholder="${campo.placeholder || ''}">`;
            }

            htmlCampos += `
                <div class="mb-3">
                    <label class="form-label small fw-bold text-muted">${campo.label}</label>
                    ${inputHtml}
                </div>
            `;
        });
        htmlCampos += '<button type="button" class="btn-close position-absolute top-0 end-0 m-2 btn-remove-item"></button>';
        
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
    }
};