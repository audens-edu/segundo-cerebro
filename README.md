# Segundo cérebro da Audens Edu

Base de conhecimento compartilhada entre as gerências de Marketing, Produto e CRM/Receita da Audens Edu. Ela foi escrita para ser lida tanto por pessoas quanto pelas IAs que usamos no dia a dia: aqui ficam o contexto da empresa, o glossário, os processos de cada área e as decisões que tomamos, sempre com o porquê.

## Como está organizado

| Pasta ou arquivo | O que guarda |
|---|---|
| `contexto/` | Quem somos, formações, públicos e marca |
| `glossario.md` | Os termos internos e o que cada um significa |
| `processos/` | Como cada área faz o que faz, separado em `marketing/`, `produto/` e `crm/` |
| `decisoes/` | Registros de decisão (ADRs), numerados e nunca apagados |
| `AGENTS.md` | As instruções que qualquer IA segue para ler e escrever aqui |
| `ferramentas/` | A skill do Claude e o guia de configuração |

## Como contribuir

Toda mudança entra por pull request e precisa da aprovação de um gerente que não seja o autor. Na prática, quem escreve é a IA: com a skill `segundo-cerebro-aedu` instalada, basta pedir ao Claude para registrar uma decisão ou documentar um processo, e ele abre o PR.

Este repositório guarda conhecimento, nunca dados pessoais. Uma verificação automática bloqueia PRs com CPF, e-mail, telefone ou chaves de acesso.
