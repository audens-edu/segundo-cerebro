# Configuração

Guia único para colocar o segundo cérebro de pé. A primeira parte é feita uma vez, por quem cria a organização; a segunda, por cada gerente.

## Uma vez, por quem cria

1. **Organização.** Em github.com, crie uma organização no plano Free com o nome `audens-edu`. Convide os outros dois gerentes e dê o papel de Owner a mais uma pessoa, para que a organização não dependa de uma só conta.
2. **Repositório.** Crie o repositório público `segundo-cerebro` e suba o conteúdo desta pasta (pela web, em "Add file > Upload files", ou por git).
3. **Permissões.** Em Settings > Collaborators and teams, dê o papel Write aos três gerentes.
4. **Trava da main.** Em Settings > Rules > Rulesets, crie um branch ruleset ativo para a branch padrão com: "Require a pull request before merging" com 1 aprovação e "Dismiss stale pull request approvals when new commits are pushed"; "Require status checks to pass" com o check `verificacao`; "Block force pushes". Deixe a lista de bypass vazia, assim nem os owners entram sem revisão. O GitHub já impede que alguém aprove o próprio PR.
5. **Segredos.** Em Settings > Code security, ative Secret scanning e Push protection.
6. **Teste.** Abra um PR qualquer e confira que o check `verificacao` roda e que o merge exige aprovação. Em Actions, rode o `revisao-mensal` manualmente uma vez.
7. **Registro.** No dia em que o piloto começar, marque na agenda dos três a retrospectiva de 30 dias.

## Cada gerente

1. **Conta.** Crie ou use sua conta no GitHub e aceite o convite da organização.
2. **Skill do Claude.** Compacte a pasta `ferramentas/skill/segundo-cerebro-aedu` num zip e envie na área de Skills das configurações do Claude.
3. **Escrita pelo Claude.** Para a IA abrir PRs sozinha, ela precisa de acesso de escrita ao GitHub no ambiente onde roda (o `gh` autenticado no seu computador ou um conector do GitHub com escrita). Sem isso a skill continua funcionando: ela prepara o texto e entrega o link para você clicar em "Propose changes", e basta estar logado no github.com.
4. **ChatGPT, só leitura.** Crie um Projeto no ChatGPT com esta instrução: "Antes de responder sobre a Audens Edu, leia https://raw.githubusercontent.com/audens-edu/segundo-cerebro/main/AGENTS.md e os arquivos relevantes do repositório audens-edu/segundo-cerebro, e cite os caminhos usados. Não proponha mudanças por aqui; elas são feitas pelo Claude."
5. **Seus Projects.** No conteúdo compartilhável dos seus Projects do Claude, troque o texto por um apontador para o arquivo correspondente no repositório e mantenha lá só o que for pessoal.
