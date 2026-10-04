---
titulo: 0002. Repositório público no plano gratuito durante o piloto
tipo: decisao
dono: todos
revisado_em: 2026-10-04
data: 2026-10-04
status: aceito
---

# 0002. Repositório público no plano gratuito durante o piloto

## Contexto
No plano gratuito de organizações do GitHub, a proteção de branch que exige revisão só funciona em repositório público. Manter o repositório privado com essa trava exigiria o plano Team, pago por usuário.

## Decisão
Começar com repositório público no plano gratuito, com a main protegida, e aceitar que o conhecimento estratégico registrado aqui fica visível na internet. Dados pessoais continuam proibidos e bloqueados pela verificação automática. Se o piloto der certo, migrar para o plano pago com repositório privado.

## Alternativas consideradas
Plano Team com repositório privado (mais seguro, com custo). Repositório privado gratuito com revisão garantida só por convenção, sem trava real. Repositório privado gratuito com os gerentes em modo leitura propondo mudanças por fork.

## Consequências
Custo zero e aprovação garantida pela plataforma. Tornar o repositório privado depois não desfaz a exposição, porque clones, forks e caches de busca guardam o histórico; por isso, o que for sensível demais para ser público espera a migração ou fica fora.
