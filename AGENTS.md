# Instruções para agentes

Este repositório é o segundo cérebro da Audens Edu: a fonte da verdade sobre contexto, termos, processos e decisões das gerências de Marketing, Produto e CRM/Receita. Quando o que está aqui divergir de outra fonte (um Project, uma memória, uma conversa antiga), vale o que está aqui. O repositório é público, então tudo o que você escreve fica visível na internet.

## Mapa

- `glossario.md`: termos internos. Leia sempre que a pergunta usar um termo da casa.
- `contexto/`: empresa, formações, públicos e marca. Leia o arquivo do assunto antes de produzir qualquer peça ou análise.
- `processos/<area>/`: um arquivo por processo, nas áreas `marketing`, `produto` e `crm`. Processos que cruzam áreas ficam na área dona e citam as outras.
- `decisoes/`: ADRs numerados (`0001-titulo.md`). O status diz se a decisão vale.
- `processos/_modelo.md` e `decisoes/_modelo.md`: os modelos que todo arquivo novo segue.

## Ler

Comece pelo glossário e pelo arquivo de contexto do assunto, depois vá aos processos e decisões. Ao responder, cite o caminho do arquivo que sustenta cada afirmação. Quando um ADR estiver com status `superado`, siga o ADR que o substitui. Quando `revisado_em` estiver vencido (90 dias para processo, 180 para contexto e glossário), use o conteúdo e avise o usuário de que ele pode estar desatualizado.

## Escrever

Toda mudança entra por pull request a partir de uma branch nomeada `<tipo>/<slug>` (por exemplo `processo/boas-vindas-turma` ou `decisao/0007-preco-early-bird`). Um assunto por PR, exceto as decisões de uma mesma reunião semanal, que vão juntas num PR chamado "Decisões da reunião de DD/MM/AAAA".

Todo arquivo de conteúdo começa com este cabeçalho:

```yaml
---
titulo: Nome legível
tipo: contexto | processo | decisao | glossario
dono: marketing | produto | crm | todos
revisado_em: AAAA-MM-DD
---
```

Ao revisar um arquivo sem mudar o sentido, atualize só o `revisado_em`. Nomes de arquivo em minúsculas, sem acento, com hífen.

Decisões não se editam depois de aceitas. Quando uma decisão muda, crie um ADR novo que explique a mudança, e no antigo troque o status para `superado por NNNN`. O número do ADR novo é o maior número existente em `decisoes/` mais um; confira também os PRs abertos para não repetir número.

## O que pode entrar

Conhecimento sobre como trabalhamos: contexto, termos, processos, critérios e o raciocínio das decisões. Pessoas aparecem pelo papel ("a SDR", "o closer", "a coordenação pedagógica"), nunca pelo nome quando forem alunos, leads ou candidatos. Dados ficam onde já vivem (CRM, Salesforce, Supabase): aqui entra o apontador para o sistema, nunca a cópia do dado. CPF, e-mail, telefone, tokens e senhas são bloqueados pela verificação automática; quando ela acusar um falso positivo, acrescente `<!-- verificacao:ignorar -->` na mesma linha e explique no PR.

## Estilo

Português do Brasil, texto corrido e direto, frases que façam sentido sozinhas para quem chega sem contexto.
