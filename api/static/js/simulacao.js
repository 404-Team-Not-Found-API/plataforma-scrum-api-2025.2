/**
 * api/static/js/simulacao.js
 * Lógica completa do Módulo 6
 */

const Simulacao = {
    prefixo: 'sprint_',
    totalEtapas: 6,
    projetos: [],

    init: function(listaProjetos) {
        this.projetos = listaProjetos;
        this.verificarEstadoInicial();
        this.configurarEventos();
        this.restaurarDadosFixos();
        this.restaurarBacklog();
        this.atualizarInterface();
    },

    configurarEventos: function() {
        // Navegação
        const btnSortear = document.getElementById('btn-sortear');
        if(btnSortear) btnSortear.addEventListener('click', () => this.realizarSorteio());

        const btnIniciar = document.getElementById('btn-iniciar');
        if(btnIniciar) btnIniciar.addEventListener('click', () => this.mostrarFases());

        // Salvamento de Inputs
        document.querySelectorAll('.save-target').forEach(input => {
            input.addEventListener('input', (e) => {
                localStorage.setItem(this.prefixo + 'campo_' + e.target.id, e.target.value);
            });
        });

        // Conclusão de Etapas
        document.querySelectorAll('.btn-concluir').forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.marcarEtapaConcluida(e.currentTarget.dataset.faseId);
            });
        });

        // Backlog
        document.querySelectorAll('.btn-add-backlog').forEach(btn => {
            btn.addEventListener('click', (e) => this.adicionarItemBacklog(e));
        });

        // Modais Específicos (Planning e Review)
        const modalPlanning = document.getElementById('modal-sprint_planning');
        if(modalPlanning) {
            modalPlanning.addEventListener('show.bs.modal', () => this.atualizarPlanning());
        }

        // NOVO: Listener para carregar itens na Review
        const modalReview = document.getElementById('modal-sprint_review');
        if(modalReview) {
            modalReview.addEventListener('show.bs.modal', () => this.atualizarReview());
        }
    },

    // --- SORTEIO E NAVEGAÇÃO ---
    realizarSorteio: function() {
        const btn = document.getElementById('btn-sortear');
        btn.disabled = true;
        btn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Sorteando...';

        setTimeout(() => {
            const index = Math.floor(Math.random() * this.projetos.length);
            const projeto = this.projetos[index];
            
            localStorage.setItem(this.prefixo + 'projeto_id', projeto.id);
            this.exibirProjetoSorteado(projeto);
            
            // CORREÇÃO: Mostrar botão de continuar
            btn.classList.add('d-none');
            document.getElementById('btn-continuar-wrapper').classList.remove('d-none');
            
            // Rola suavemente para o botão
            document.getElementById('btn-continuar-wrapper').scrollIntoView({ behavior: 'smooth' });
        }, 1000);
    },

    exibirProjetoSorteado: function(projeto) {
        // Header da área de fases
        const titulo = document.getElementById('projeto-titulo-ativo');
        const desc = document.getElementById('projeto-desc-ativo');
        if(titulo) titulo.innerText = projeto.nome;
        if(desc) desc.innerText = projeto.descricao;

        // Visual do Grid
        document.querySelectorAll('.card-projeto-opcao').forEach(card => {
            card.classList.remove('border-primary', 'bg-light');
            const icon = card.querySelector('.icon-check');
            if(icon) {
                icon.classList.remove('bi-check-square-fill', 'text-primary');
                icon.classList.add('bi-square');
            }
        });

        const cardSorteado = document.getElementById('proj-card-' + projeto.id);
        if(cardSorteado) {
            cardSorteado.classList.add('border-primary', 'bg-light');
            const icon = cardSorteado.querySelector('.icon-check');
            if(icon) {
                icon.classList.remove('bi-square', 'text-muted');
                icon.classList.add('bi-check-square-fill', 'text-primary');
            }
        }
    },

    mostrarFases: function() {
        document.getElementById('area-sorteio').classList.add('d-none');
        document.getElementById('area-fases').classList.remove('d-none');
        window.scrollTo(0, 0);
    },

    verificarEstadoInicial: function() {
        const pid = localStorage.getItem(this.prefixo + 'projeto_id');
        if (pid) {
            const projeto = this.projetos.find(p => p.id == pid);
            if (projeto) {
                this.exibirProjetoSorteado(projeto);
                this.mostrarFases();
            }
        }
    },

    // --- PERSISTÊNCIA ---
    restaurarDadosFixos: function() {
        document.querySelectorAll('.save-target').forEach(input => {
            const valor = localStorage.getItem(this.prefixo + 'campo_' + input.id);
            if (valor) input.value = valor;
        });
    },

    marcarEtapaConcluida: function(faseId) {
        localStorage.setItem(this.prefixo + 'status_' + faseId, 'concluido');
        const modalEl = document.getElementById('modal-' + faseId);
        const modal = bootstrap.Modal.getInstance(modalEl);
        modal.hide();
        this.atualizarInterface();
    },

    atualizarInterface: function() {
        let concluidos = 0;
        document.querySelectorAll('.card-fase').forEach(card => {
            const faseId = card.dataset.faseId;
            const status = localStorage.getItem(this.prefixo + 'status_' + faseId);
            const icon = card.querySelector('.status-icon');
            
            if (status === 'concluido') {
                concluidos++;
                card.classList.add('border-success'); // Visual mais sutil
                icon.classList.remove('bi-circle', 'text-muted');
                icon.classList.add('bi-check-circle-fill', 'text-success');
            }
        });

        const pct = (concluidos / this.totalEtapas) * 100;
        document.getElementById('barra-progresso').style.width = `${pct}%`;
        document.getElementById('contador-progresso').innerText = concluidos;
    },

    // --- BACKLOG & PLANNING ---
    adicionarItemBacklog: function(e, dadosItem = null) {
        const container = e.target ? e.target.closest('.lista-dinamica-container') : document.querySelector('.lista-dinamica-container');
        const wrapper = container.querySelector('.lista-items-wrapper');
        const schema = JSON.parse(container.dataset.schema);
        
        const emptyMsg = container.querySelector('.empty-state');
        if(emptyMsg) emptyMsg.classList.add('d-none');

        const idUnico = dadosItem ? dadosItem.id : 'item_' + Date.now();
        const div = document.createElement('div');
        div.className = 'card p-3 mb-2 shadow-sm backlog-item position-relative';
        div.dataset.id = idUnico;

        let html = '<div class="row g-2">';
        schema.forEach(campo => {
            const valor = dadosItem ? dadosItem[campo.id] : '';
            // Placeholder adicionado aqui
            const placeholder = campo.placeholder || ''; 
            
            html += `
                <div class="col" style="min-width: ${campo.width}">
                    <label class="form-label small fw-bold text-muted">${campo.label}</label>
                    <input type="${campo.tipo === 'select' ? 'text' : campo.tipo}" 
                           class="form-control form-control-sm backlog-input" 
                           data-campo="${campo.id}" 
                           value="${valor}"
                           placeholder="${placeholder}" 
                           ${campo.tipo === 'select' ? 'list="opts-'+campo.id+'"' : ''}>
                    ${campo.tipo === 'select' ? `<datalist id="opts-${campo.id}">${campo.options.map(o=>`<option value="${o}">`).join('')}</datalist>` : ''}
                </div>
            `;
        });
        html += '</div><button type="button" class="btn-close position-absolute top-0 end-0 m-2 btn-remove-item"></button>';
        
        div.innerHTML = html;
        wrapper.appendChild(div);

        div.querySelector('.btn-remove-item').addEventListener('click', () => {
            div.remove();
            this.salvarBacklog();
        });
        div.querySelectorAll('input').forEach(inp => inp.addEventListener('input', () => this.salvarBacklog()));

        if(!dadosItem) this.salvarBacklog();
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
    },

    restaurarBacklog: function() {
        const dados = JSON.parse(localStorage.getItem(this.prefixo + 'backlog_data') || '[]');
        const btnAdd = document.querySelector('.btn-add-backlog');
        if (dados.length > 0 && btnAdd) {
            dados.forEach(item => this.adicionarItemBacklog({ target: btnAdd }, item));
        }
    },

    atualizarPlanning: function() {
        const wrapper = document.querySelector('.selecao-origem-wrapper');
        if(!wrapper) return;

        const itens = JSON.parse(localStorage.getItem(this.prefixo + 'backlog_data') || '[]');
        const sel = JSON.parse(localStorage.getItem(this.prefixo + 'planning_selected') || '[]');

        if(itens.length === 0) {
            wrapper.innerHTML = '<div class="text-muted p-3 text-center">Nenhum item no Backlog.</div>';
            return;
        }

        let html = '<div class="list-group">';
        itens.forEach(item => {
            const checked = sel.includes(item.id) ? 'checked' : '';
            html += `
                <label class="list-group-item d-flex gap-2">
                    <input class="form-check-input flex-shrink-0 chk-planning" type="checkbox" value="${item.id}" ${checked}>
                    <span>${item.titulo || 'Item sem nome'} <small class="text-muted">(${item.estimativa || '-'})</small></span>
                </label>
            `;
        });
        html += '</div>';
        wrapper.innerHTML = html;

        wrapper.querySelectorAll('.chk-planning').forEach(chk => {
            chk.addEventListener('change', () => {
                const novos = Array.from(wrapper.querySelectorAll('.chk-planning:checked')).map(c => c.value);
                localStorage.setItem(this.prefixo + 'planning_selected', JSON.stringify(novos));
            });
        });
    },

    // --- NOVO: ATUALIZAR REVIEW COM ITENS SELECIONADOS ---
    atualizarReview: function() {
        const container = document.getElementById('review-itens-selecionados');
        if(!container) return;

        const backlog = JSON.parse(localStorage.getItem(this.prefixo + 'backlog_data') || '[]');
        const selecionadosIds = JSON.parse(localStorage.getItem(this.prefixo + 'planning_selected') || '[]');
        const itensSprint = backlog.filter(i => selecionadosIds.includes(i.id));

        if(itensSprint.length === 0) {
            container.innerHTML = '<div class="text-muted small fst-italic">Nenhum item foi selecionado no Planning.</div>';
            return;
        }

        let html = '<ul class="list-group list-group-flush mb-3 border rounded">';
        itensSprint.forEach(item => {
            html += `<li class="list-group-item bg-light small"><i class="bi bi-check2-square me-2"></i>${item.titulo || 'Sem título'}</li>`;
        });
        html += '</ul>';
        container.innerHTML = html;
    },

    // --- GERAÇÃO DE PDF COMPLETA ---
    gerarPDF: function() {
        const scrollAtual = window.scrollY;
        window.scrollTo(0, 0);

        const template = document.getElementById('template-pdf');
        const clone = template.cloneNode(true);
        
        clone.id = 'pdf-render-temp';
        clone.style.display = 'block';
        clone.style.position = 'absolute';
        clone.style.top = '0';
        clone.style.left = '0';
        clone.style.zIndex = '9999';
        clone.style.backgroundColor = '#fff';
        
        document.body.appendChild(clone);

        // 1. Cabeçalho
        clone.querySelector('.pdf-data').innerText = new Date().toLocaleDateString('pt-BR');
        const pid = localStorage.getItem(this.prefixo + 'projeto_id');
        const proj = this.projetos.find(p => p.id == pid);
        if(proj) clone.querySelector('.pdf-projeto-nome').innerText = proj.nome;

        // 2. Campos Fixos (Automático via data-pdf-field)
        // Isso cobre: Visão, Meta, Datas do Planning, Campos do Daily, Review e Retro
        clone.querySelectorAll('.pdf-field').forEach(el => {
            const val = localStorage.getItem(this.prefixo + 'campo_' + el.dataset.pdfField);
            if(val) el.innerText = val;
        });

        // 3. Listas (Backlog e Planning)
        const backlog = JSON.parse(localStorage.getItem(this.prefixo + 'backlog_data') || '[]');
        const selIds = JSON.parse(localStorage.getItem(this.prefixo + 'planning_selected') || '[]');
        
        // Render Backlog
        const ulBacklog = clone.querySelector('.pdf-lista-backlog');
        ulBacklog.innerHTML = '';
        if(backlog.length === 0) ulBacklog.innerHTML = '<li>Vazio</li>';
        else {
            backlog.forEach(i => {
                let txt = `<strong>[${i.prioridade||'-'}]</strong> ${i.titulo||'Item'}`;
                if(i.estimativa) txt += ` <em>(${i.estimativa})</em>`;
                if(i.descricao) txt += `<br><span style="font-size:11px; color:#555; display:block; margin-top:2px;">${i.descricao}</span>`;
                if(i.aceitacao) txt += `<span style="font-size:11px; color:#888; display:block;">Critérios: ${i.aceitacao}</span>`;
                
                const li = document.createElement('li');
                li.innerHTML = txt;
                li.style.marginBottom = '10px'; // Aumentei o espaçamento
                li.style.borderBottom = '1px solid #eee';
                li.style.paddingBottom = '5px';
                ulBacklog.appendChild(li);
            });
        }

        // Render Planning List
        const ulPlanning = clone.querySelector('.pdf-lista-planning');
        ulPlanning.innerHTML = '';
        const itensSprint = backlog.filter(i => selIds.includes(i.id));
        if(itensSprint.length === 0) ulPlanning.innerHTML = '<li>Vazio</li>';
        else {
            itensSprint.forEach(i => {
                const li = document.createElement('li');
                li.innerText = i.titulo;
                ulPlanning.appendChild(li);
            });
        }

        // Geração
        const content = clone.querySelector('.pdf-container');
        const opt = {
            margin: 10,
            filename: `Sprint_Scrum_${Date.now()}.pdf`,
            image: { type: 'jpeg', quality: 0.98 },
            html2canvas: { scale: 2, useCORS: true, scrollY: 0 },
            jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
        };

        html2pdf().set(opt).from(content).save()
            .then(() => {
                document.body.removeChild(clone);
                window.scrollTo(0, scrollAtual);
            })
            .catch(err => {
                console.error(err);
                if(document.body.contains(clone)) document.body.removeChild(clone);
                window.scrollTo(0, scrollAtual);
            });
    }
};