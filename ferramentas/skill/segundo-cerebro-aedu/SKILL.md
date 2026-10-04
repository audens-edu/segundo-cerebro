---
name: segundo-cerebro-aedu
description: Consulta e alimenta o segundo cérebro da Audens Edu (repositório audens-edu/segundo-cerebro). Use ao precisar de contexto, termos, processos ou decisões da Audens Edu, ao registrar uma decisão ou as decisões da reunião semanal, ou ao documentar ou atualizar um processo.
---

# Segundo cérebro da Audens Edu

O repositório público `https://github.com/audens-edu/segundo-cerebro` é a fonte da verdade sobre contexto, glossário, processos e decisões das gerências da Audens Edu. O mapa de pastas, o cabeçalho obrigatório, os modelos e a regra do que pode entrar vivem no `AGENTS.md` do próprio repositório; esta skill diz como chegar lá e qual fluxo seguir.

## Acessar o repositório

Use o primeiro caminho que funcionar:

1. Um clone local já existente, atualizado com `git pull`.
2. `gh repo clone audens-edu/segundo-cerebro`.
3. Leitura pública sem autenticação: a árvore de arquivos em `https://api.github.com/repos/audens-edu/segundo-cerebro/git/trees/main?recursive=1` e cada arquivo em `https://raw.githubusercontent.com/audens-edu/segundo-cerebro/main/<caminho>`.

Leia o `AGENTS.md` antes de qualquer outro arquivo, em toda sessão. Pronto quando você conhece o mapa e as regras de escrita.

## Consultar

Leia o glossário e os arquivos do assunto, siga as regras de leitura do `AGENTS.md` e responda citando o caminho de cada arquivo usado. Pronto quando cada afirmação sobre a Audens Edu tem um arquivo por trás, ou quando você disse ao usuário que o repositório não cobre o assunto e sugeriu documentá-lo.

## Propor uma mudança

Vale para documentar ou atualizar um processo ou contexto, registrar uma decisão e registrar as decisões da reunião semanal. Na reunião semanal, o usuário dita o que foi decidido: cada decisão vira um ADR e todos vão num único PR chamado "Decisões da reunião de DD/MM/AAAA".

1. **Redigir.** Escreva a partir do modelo da pasta e com o cabeçalho do `AGENTS.md`. Para ADR, pergunte o porquê e as alternativas se o usuário não disser, porque é a parte que mais se perde. Mostre o texto e ajuste até o usuário aprovar. Pronto quando o usuário aprovou o conteúdo.
2. **Conferir o que é publicável.** O repositório é público. Releia o texto procurando nome de aluno, lead ou candidato, CPF, e-mail, telefone, link de painel interno, token ou senha, e troque pessoas pelo papel. Pronto quando a releitura não acha nada.
3. **Abrir o PR.** Se o `gh` estiver autenticado com escrita no repositório: crie a branch `<tipo>/<slug>`, faça o commit, envie e rode `gh pr create` preenchendo o modelo de PR. Se não houver escrita, entregue ao usuário o caminho e o conteúdo final do arquivo e o link `https://github.com/audens-edu/segundo-cerebro/new/main/<pasta>` (arquivo novo) ou `https://github.com/audens-edu/segundo-cerebro/edit/main/<caminho>` (arquivo existente): ao colar o texto e clicar em "Propose changes", o próprio GitHub abre o PR. Pronto quando você tem o link do PR ou o usuário confirmou que o criou.
4. **Fechar.** Entregue o link do PR e lembre que outro gerente precisa aprovar antes de entrar.
