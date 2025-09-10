# Estrutura das Branches

```
main: Branch principal e estável.
feature/<nome-da-feature>: Para adição de funcionalidades.
```

## Processo de Code Review

- Todo código deve passar por revisão de pelo menos 1 (um) dev antes de ser aceito o Pull Request na branch `main`.
- O revisor deve fornecer feedback detalhado para o Dev responsável pela Task avaliada.
- **Responsabilidade:** O dono da task é responsável por testar e corrigir problemas no seu código. Pull Requests que “quebrarem” o sistema terão como responsáveis tanto o dono da task quanto quem aprovou.

## Processo de Pull Request

- Os Pull Requests devem estar detalhados com as principais funcionalidades adicionadas, bem como problemas encontrados no código e como foram resolvidos/contornados.
- Fotos caso trabalhado no frontend.

### Checklist obrigatório antes de abrir um PR:

- [ ] Código foi revisado
- [ ] Testes foram executados
- [ ] Documentação foi atualizada

## Tempo Esperado para Aprovação

- O tempo esperado para aprovação de um PR é de **48 horas**.
- Qualquer Dev pode aprovar um PR, mas é necessário que siga as responsabilidades.
- Preferencialmente não aprove o seu próprio PR (Pull Request),