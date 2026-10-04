---
titulo: 0001. Segundo cérebro das gerências num repositório GitHub
tipo: decisao
dono: todos
revisado_em: 2026-10-04
data: 2026-10-04
status: aceito
---

# 0001. Segundo cérebro das gerências num repositório GitHub

## Contexto
Cada gerente explicava o mesmo contexto da Audens Edu para a própria IA, o conhecimento operacional ficava concentrado em poucas pessoas e decisões tomadas na reunião semanal se perdiam. As três gerências usam principalmente o Claude, no Cowork, e também o ChatGPT.

## Decisão
Criar o repositório `audens-edu/segundo-cerebro` numa organização própria do GitHub como fonte da verdade sobre contexto, glossário, processos e decisões. As IAs escrevem por pull request e qualquer gerente, exceto o autor, aprova. O Claude lê e escreve pela skill `segundo-cerebro-aedu`; o ChatGPT só lê. Depois de cada reunião semanal, as decisões viram ADRs num único PR. Skills compartilhadas ficam para uma segunda versão.

## Alternativas consideradas
Google Drive e ClickUp têm edição mais fácil para pessoas, mas não oferecem histórico e revisão no mesmo nível, nem a integração nativa com as IAs. Claude Projects compartilhados exigiriam o plano Team e não alcançam o ChatGPT.

## Consequências
O conhecimento passa a ter dono, histórico e revisão. Os Projects pessoais de cada gerente passam a apontar para cá e guardam só o que for pessoal. Uma rotina mensal sinaliza processos com mais de 90 dias e contextos com mais de 180 dias sem revisão. O piloto dura 30 dias e termina em retrospectiva com três sinais: cada gerente propõe pelo menos 2 PRs, toda reunião semanal gera ADR e cada um aponta pelo menos um caso em que a IA acertou por causa do repositório.
