# BabyHealth — Backlog Index

> Hierarquia completa: **14 Epics → 48 Features → 57 Stories → 201 Tasks**

---

## EP-01 — Fundação do Produto `P0`

| Feature | Stories | Tasks | Priority |
|---------|---------|-------|----------|
| [FE-01.1 — Arquitetura de Informação](features/FE-01.1-arquitetura-de-informacao.md) | [US-01.1.1](stories/US-01.1.1-navegacao-clara.md), [US-01.1.2](stories/US-01.1.2-nomes-abas-coerentes.md) | [TK-01.1.1](tasks/TK-01.1.1-mapa-navegacao.md), [TK-01.1.2](tasks/TK-01.1.2-acao-global-registrar.md), [TK-01.1.3](tasks/TK-01.1.3-hierarquia-home-detalhe-bottom-sheet.md), [TK-01.1.4](tasks/TK-01.1.4-navegacao-mobile-first.md) | P0 |
| [FE-01.2 — Design System Visual](features/FE-01.2-design-system-visual.md) | [US-01.2.1](stories/US-01.2.1-interface-bonita-suave.md), [US-01.2.2](stories/US-01.2.2-inspiracao-samsung-health.md) | [TK-01.2.1](tasks/TK-01.2.1-paleta-pastel.md), [TK-01.2.2](tasks/TK-01.2.2-tipografia-escala-espacamento.md), [TK-01.2.3](tasks/TK-01.2.3-linguagem-icones.md), [TK-01.2.4](tasks/TK-01.2.4-padroes-componentes.md), [TK-01.2.5](tasks/TK-01.2.5-estados-visuais.md) | P0 |
| [FE-01.3 — Shell do Aplicativo](features/FE-01.3-shell-do-aplicativo.md) | [US-01.3.1](stories/US-01.3.1-app-estrutura-pronta.md) | [TK-01.3.1](tasks/TK-01.3.1-layout-base-mobile-first.md), [TK-01.3.2](tasks/TK-01.3.2-bottom-navigation.md), [TK-01.3.3](tasks/TK-01.3.3-header-global.md), [TK-01.3.4](tasks/TK-01.3.4-floating-action-registrar.md), [TK-01.3.5](tasks/TK-01.3.5-transicoes-entre-telas.md) | P0 |

---

## EP-02 — Modelo de Dados e Motor de Logs `P0`

| Feature | Stories | Tasks | Priority |
|---------|---------|-------|----------|
| [FE-02.1 — Entidade Genérica de Evento](features/FE-02.1-entidade-generica-evento.md) | [US-02.1.1](stories/US-02.1.1-registros-consistentes.md), [US-02.1.2](stories/US-02.1.2-timeline-unificada.md) | [TK-02.1.1](tasks/TK-02.1.1-schema-generico-evento.md), [TK-02.1.2](tasks/TK-02.1.2-campos-base.md), [TK-02.1.3](tasks/TK-02.1.3-normalizacao-categoria.md), [TK-02.1.4](tasks/TK-02.1.4-utilitario-ordenacao-tempo.md), [TK-02.1.5](tasks/TK-02.1.5-cores-homogeneas-tipo-evento.md) | P0 |
| [FE-02.2 — Persistência Local](features/FE-02.2-persistencia-local.md) | [US-02.2.1](stories/US-02.2.1-registros-salvos.md) | [TK-02.2.1](tasks/TK-02.2.1-estrategia-persistencia.md), [TK-02.2.2](tasks/TK-02.2.2-camada-leitura-escrita.md), [TK-02.2.3](tasks/TK-02.2.3-seed-data-demo.md), [TK-02.2.4](tasks/TK-02.2.4-versionamento-dados.md) | P0 |
| [FE-02.3 — Quick Log Engine](features/FE-02.3-quick-log-engine.md) | [US-02.3.1](stories/US-02.3.1-registrar-poucos-toques.md), [US-02.3.2](stories/US-02.3.2-atualizar-home-timeline.md) | [TK-02.3.1](tasks/TK-02.3.1-dispatcher-generico-logs.md), [TK-02.3.2](tasks/TK-02.3.2-atualizar-timeline-insert.md), [TK-02.3.3](tasks/TK-02.3.3-atualizar-cards-resumo.md), [TK-02.3.4](tasks/TK-02.3.4-presets-rapidos.md), [TK-02.3.5](tasks/TK-02.3.5-botao-log-manual.md) | P0 |

---

## EP-03 — Home "Hoje" `P0`

| Feature | Stories | Tasks | Priority |
|---------|---------|-------|----------|
| [FE-03.1 — Hero Card do Dia](features/FE-03.1-hero-card-do-dia.md) | [US-03.1.1](stories/US-03.1.1-estado-geral-bebe.md) | [TK-03.1.1](tasks/TK-03.1.1-metricas-hero-card.md), [TK-03.1.2](tasks/TK-03.1.2-resumo-textual-dia.md), [TK-03.1.3](tasks/TK-03.1.3-status-badge.md), [TK-03.1.4](tasks/TK-03.1.4-visual-principal-card.md) | P0 |
| [FE-03.2 — Cards dos Trackers](features/FE-03.2-cards-trackers-obrigatorios.md) | [US-03.2.1](stories/US-03.2.1-acompanhar-trackers.md) | [TK-03.2.1](tasks/TK-03.2.1-card-alimentacao.md) .. [TK-03.2.6](tasks/TK-03.2.6-card-atividades.md) | P0 |
| [FE-03.3 — Linha do Tempo](features/FE-03.3-linha-do-tempo-do-dia.md) | [US-03.3.1](stories/US-03.3.1-timeline-cronologica.md) | [TK-03.3.1](tasks/TK-03.3.1-lista-cronologica-reversa.md) .. [TK-03.3.4](tasks/TK-03.3.4-filtro-por-tipo.md) | P0 |
| [FE-03.4 — Registro Inline](features/FE-03.4-registro-inline.md) | [US-03.4.1](stories/US-03.4.1-registrar-direto-card.md) | [TK-03.4.1](tasks/TK-03.4.1-cta-inline-por-card.md) .. [TK-03.4.5](tasks/TK-03.4.5-corrigir-sonner-next-themes.md) | P0 |

---

## EP-04 — Alimentação e Hidratação `P0`

| Feature | Stories | Tasks | Priority |
|---------|---------|-------|----------|
| [FE-04.1 — Mamadeira/Leite](features/FE-04.1-mamadeira-leite.md) | [US-04.1.1](stories/US-04.1.1-registrar-mamadeira.md), [US-04.1.2](stories/US-04.1.2-ultima-mamada.md) | [TK-04.1.1](tasks/TK-04.1.1-tipos-mamadeira.md) .. [TK-04.1.7](tasks/TK-04.1.7-spike-multiplas-modalidades-alimentacao.md), [TK-04.4.7](tasks/TK-04.4.7-grafico-semanal-alimentacao.md) | P0 |
| [FE-04.2 — Amamentação](features/FE-04.2-amamentacao-basica-avancada.md) | [US-04.2.1](stories/US-04.2.1-modo-simples-amamentacao.md), [US-04.2.2](stories/US-04.2.2-modo-avancado-amamentacao.md) | [TK-04.2.1](tasks/TK-04.2.1-modo-basico.md) .. [TK-04.2.7](tasks/TK-04.2.7-sessoes-compostas.md) | P0 |
| [FE-04.3 — Sólidos/Papinhas](features/FE-04.3-solidos-papinhas-refeicoes.md) | [US-04.3.1](stories/US-04.3.1-registrar-solidos.md), [US-04.3.2](stories/US-04.3.2-primeira-exposicao.md) | [TK-04.3.1](tasks/TK-04.3.1-tipos-solidos.md) .. [TK-04.3.6](tasks/TK-04.3.6-reacao-alergia.md) | P0 |
| [FE-04.4 — Hidratação](features/FE-04.4-hidratacao.md) | [US-04.4.1](stories/US-04.4.1-registrar-hidratacao.md) | [TK-04.4.1](tasks/TK-04.4.1-presets-volume.md) .. [TK-04.4.6](tasks/TK-04.4.6-grafico-semanal-hidratacao.md) | P0 |

---

## EP-05 — Sono e Tempo Acordado `P0`

| Feature | Stories | Tasks | Priority |
|---------|---------|-------|----------|
| [FE-05.1 — Registro de Sono](features/FE-05.1-registro-de-sono.md) | [US-05.1.1](stories/US-05.1.1-iniciar-encerrar-sono.md) | [TK-05.1.1](tasks/TK-05.1.1-tipos-sono.md) .. [TK-05.1.5](tasks/TK-05.1.5-edicao-posterior.md) | P0 |
| [FE-05.2 — Tempo Acordado](features/FE-05.2-tempo-acordado.md) | [US-05.2.1](stories/US-05.2.1-tempo-acordado.md) | [TK-05.2.1](tasks/TK-05.2.1-calcular-awake-window.md) .. [TK-05.2.4](tasks/TK-05.2.4-comportamento-sem-dados.md) | P0 |
| [FE-05.3 — Resumo Diário de Sono](features/FE-05.3-resumo-diario-sono.md) | [US-05.3.1](stories/US-05.3.1-resumo-diario-sono.md) | [TK-05.3.1](tasks/TK-05.3.1-somar-sono-diurno.md) .. [TK-05.3.5](tasks/TK-05.3.5-grafico-semanal-sono.md) | P0 |

---

## EP-06 — Fraldas e Atividades `P0`

| Feature | Stories | Tasks | Priority |
|---------|---------|-------|----------|
| [FE-06.1 — Fraldas](features/FE-06.1-fraldas.md) | [US-06.1.1](stories/US-06.1.1-registrar-fralda.md) | [TK-06.1.1](tasks/TK-06.1.1-tipos-fralda.md) .. [TK-06.1.4](tasks/TK-06.1.4-total-diario-fraldas.md) | P0 |
| [FE-06.2 — Atividades](features/FE-06.2-atividades.md) | [US-06.2.1](stories/US-06.2.1-registrar-atividades.md) | [TK-06.2.1](tasks/TK-06.2.1-catalogo-atividades.md) .. [TK-06.2.4](tasks/TK-06.2.4-total-dia-atividade.md) | P0 |
| [FE-06.3 — Resumo de Atividades](features/FE-06.3-resumo-atividades.md) | [US-06.3.1](stories/US-06.3.1-estimulos-dia.md) | [TK-06.3.1](tasks/TK-06.3.1-card-atividades.md) .. [TK-06.3.4](tasks/TK-06.3.4-ultima-atividade.md) | P0 |

---

## EP-07 — Cuidadores `P0`

| Feature | Stories | Tasks | Priority |
|---------|---------|-------|----------|
| [FE-07.1 — Identidade de Cuidador](features/FE-07.1-identidade-de-cuidador.md) | [US-07.1.1](stories/US-07.1.1-saber-quem-registrou.md), [US-07.1.2](stories/US-07.1.2-saber-quem-esta-usando.md) | [TK-07.1.1](tasks/TK-07.1.1-modelar-entidade-cuidador.md) .. [TK-07.1.4](tasks/TK-07.1.4-associar-cuidador-log.md) | P0 |
| [FE-07.2 — Feed Compartilhado](features/FE-07.2-feed-compartilhado.md) | [US-07.2.1](stories/US-07.2.1-feed-comum.md) | [TK-07.2.1](tasks/TK-07.2.1-tela-cuidadores.md) .. [TK-07.2.4](tasks/TK-07.2.4-ultimos-registros-pessoa.md) | P0 |
| [FE-07.3 — Filtro por Cuidador](features/FE-07.3-filtro-por-cuidador.md) | [US-07.3.1](stories/US-07.3.1-filtrar-por-pessoa.md) | [TK-07.3.1](tasks/TK-07.3.1-chips-filtro.md) .. [TK-07.3.3](tasks/TK-07.3.3-clear-filter.md) | P1 |

---

## EP-08 — Relatórios e Insights `P0/P1`

| Feature | Stories | Tasks | Priority |
|---------|---------|-------|----------|
| [FE-08.1 — Resumo Diário](features/FE-08.1-resumo-diario.md) | [US-08.1.1](stories/US-08.1.1-leitura-rapida-dia.md) | [TK-08.1.1](tasks/TK-08.1.1-kpis-resumo-diario.md) .. [TK-08.1.4](tasks/TK-08.1.4-comparativo-dias-anteriores.md) | P0 |
| [FE-08.2 — Relatório Semanal](features/FE-08.2-relatorio-semanal.md) | [US-08.2.1](stories/US-08.2.1-relatorio-semanal-elegante.md) | [TK-08.2.1](tasks/TK-08.2.1-layout-relatorio-semanal.md) .. [TK-08.2.4](tasks/TK-08.2.4-destaques-positivos-quedas.md) | P0 |
| [FE-08.3 — Insights Automáticos](features/FE-08.3-insights-automaticos.md) | [US-08.3.1](stories/US-08.3.1-insights-legiveis.md) | [TK-08.3.1](tasks/TK-08.3.1-regras-simples-insight.md) .. [TK-08.3.5](tasks/TK-08.3.5-exibir-insights-cards.md) | P1 |

---

## EP-09 — Rotinas e Conteúdo `P1`

| Feature | Stories | Tasks | Priority |
|---------|---------|-------|----------|
| [FE-09.1 — Biblioteca de Conteúdo](features/FE-09.1-biblioteca-de-conteudo.md) | [US-09.1.1](stories/US-09.1.1-acessar-conteudo-util.md) | [TK-09.1.1](tasks/TK-09.1.1-tela-rotinas.md) .. [TK-09.1.4](tasks/TK-09.1.4-organizar-conteudo-tema-idade.md) | P1 |
| [FE-09.2 — Rotinas Guiadas](features/FE-09.2-rotinas-guiadas.md) | [US-09.2.1](stories/US-09.2.1-seguir-rotinas-guiadas.md) | [TK-09.2.1](tasks/TK-09.2.1-modelo-rotina-guiada.md) .. [TK-09.2.5](tasks/TK-09.2.5-exibir-passo-a-passo.md) | P1 |
| [FE-09.3 — Curadoria Externa](features/FE-09.3-curadoria-externa.md) | [US-09.3.1](stories/US-09.3.1-acessar-conteudos-externos.md) | [TK-09.3.1](tasks/TK-09.3.1-fontes-externas.md) .. [TK-09.3.3](tasks/TK-09.3.3-aviso-saida-app.md) | P2 |

---

## EP-10 — Meu Bebê e Crescimento `P1`

| Feature | Stories | Tasks | Priority |
|---------|---------|-------|----------|
| [FE-10.1 — Perfil do Bebê](features/FE-10.1-perfil-do-bebe.md) | [US-10.1.1](stories/US-10.1.1-area-propria-bebe.md) | [TK-10.1.1](tasks/TK-10.1.1-perfil-base.md) .. [TK-10.1.4](tasks/TK-10.1.4-modulos-ativos.md) | P1 |
| [FE-10.2 — Crescimento](features/FE-10.2-crescimento.md) | [US-10.2.1](stories/US-10.2.1-registrar-peso-altura-cc.md) | [TK-10.2.1](tasks/TK-10.2.1-formulario-medidas.md) .. [TK-10.2.4](tasks/TK-10.2.4-ultima-medicao-destaque.md) | P1 |
| [FE-10.3 — Observações e Marcos](features/FE-10.3-observacoes-e-marcos.md) | [US-10.3.1](stories/US-10.3.1-registrar-marcos-observacoes.md) | [TK-10.3.1](tasks/TK-10.3.1-entidade-observacao.md) .. [TK-10.3.3](tasks/TK-10.3.3-associar-observacao-data.md) | P2 |

---

## EP-11 — Saúde, Vitaminas e Remédios `P1`

| Feature | Stories | Tasks | Priority |
|---------|---------|-------|----------|
| [FE-11.1 — Vitaminas e Remédios](features/FE-11.1-vitaminas-e-remedios.md) | [US-11.1.1](stories/US-11.1.1-registrar-vitamina-remedio.md), [US-11.1.2](stories/US-11.1.2-confirmacao-administracao.md) | [TK-11.1.1](tasks/TK-11.1.1-schema-medicacao.md) .. [TK-11.1.4](tasks/TK-11.1.4-confirmacao-administracao.md) | P1 |
| [FE-11.2 — Histórico de Saúde Leve](features/FE-11.2-historico-saude-leve.md) | [US-11.2.1](stories/US-11.2.1-registrar-eventos-saude.md) | [TK-11.2.1](tasks/TK-11.2.1-tipo-temperatura.md) .. [TK-11.2.4](tasks/TK-11.2.4-exibir-historico.md) | P2 |

---

## EP-12 — Autenticação e Controle de Acesso `P0`

| Feature | Stories | Tasks | Priority |
|---------|---------|-------|----------|
| [FE-12.1 — Modelo de Usuário e Credenciais](features/FE-12.1-modelo-usuario-credenciais.md) | [US-12.1.1](stories/US-12.1.1-cadastro-usuarios-json.md) | [TK-12.1.1](tasks/TK-12.1.1-modelo-pydantic-user.md), [TK-12.1.2](tasks/TK-12.1.2-criar-users-json.md), [TK-12.1.3](tasks/TK-12.1.3-user-service.md), [TK-12.1.4](tasks/TK-12.1.4-hashing-senhas-bcrypt.md) | P0 |
| [FE-12.2 — Autenticação JWT no Backend](features/FE-12.2-autenticacao-jwt-backend.md) | [US-12.2.1](stories/US-12.2.1-login-retorna-jwt.md) | [TK-12.2.1](tasks/TK-12.2.1-dependencias-auth.md), [TK-12.2.2](tasks/TK-12.2.2-config-jwt.md), [TK-12.2.3](tasks/TK-12.2.3-auth-service.md), [TK-12.2.4](tasks/TK-12.2.4-router-auth.md), [TK-12.2.5](tasks/TK-12.2.5-jwt-payload-completo.md) | P0 |
| [FE-12.3 — Middleware de Proteção de Rotas](features/FE-12.3-middleware-protecao-rotas.md) | [US-12.3.1](stories/US-12.3.1-rotas-protegidas.md) | [TK-12.3.1](tasks/TK-12.3.1-dependency-get-current-user.md), [TK-12.3.2](tasks/TK-12.3.2-dependency-get-profile-repository.md), [TK-12.3.3](tasks/TK-12.3.3-substituir-get-repository.md), [TK-12.3.4](tasks/TK-12.3.4-rotas-publicas.md), [TK-12.3.5](tasks/TK-12.3.5-http-401-tokens-invalidos.md) | P0 |
| [FE-12.4 — Tela de Login](features/FE-12.4-tela-login-frontend.md) | [US-12.4.1](stories/US-12.4.1-tela-login-credenciais.md) | [TK-12.4.1](tasks/TK-12.4.1-login-page-component.md), [TK-12.4.2](tasks/TK-12.4.2-chamada-api-login.md), [TK-12.4.3](tasks/TK-12.4.3-feedback-erro-login.md), [TK-12.4.4](tasks/TK-12.4.4-redirect-home-login.md), [TK-12.4.5](tasks/TK-12.4.5-estilizar-login-design-system.md) | P0 |
| [FE-12.5 — Contexto de Autenticação](features/FE-12.5-contexto-autenticacao-frontend.md) | [US-12.5.1](stories/US-12.5.1-sessao-usuario-frontend.md) | [TK-12.5.1](tasks/TK-12.5.1-auth-context-provider.md), [TK-12.5.2](tasks/TK-12.5.2-token-localstorage.md), [TK-12.5.3](tasks/TK-12.5.3-client-bearer-header.md), [TK-12.5.4](tasks/TK-12.5.4-protected-route.md), [TK-12.5.5](tasks/TK-12.5.5-implementar-logout.md), [TK-12.5.6](tasks/TK-12.5.6-caregiver-id-do-token.md), [TK-12.5.7](tasks/TK-12.5.7-tratar-401-global.md) | P0 |
| [FE-12.6 — Migração de Dados e Scripts](features/FE-12.6-migracao-dados-scripts.md) | [US-12.6.1](stories/US-12.6.1-dados-preservados-scripts-simples.md) | [TK-12.6.1](tasks/TK-12.6.1-renomear-davi-test.md), [TK-12.6.2](tasks/TK-12.6.2-remover-scripts-npm-perfil.md), [TK-12.6.3](tasks/TK-12.6.3-simplificar-package-json.md), [TK-12.6.4](tasks/TK-12.6.4-atualizar-local-run-md.md), [TK-12.6.5](tasks/TK-12.6.5-env-example-jwt.md), [TK-12.6.6](tasks/TK-12.6.6-config-data-dir-raiz.md) | P0 |

---

## EP-13 — Melhoria Contínua e Refatoração `P1`

| Feature | Stories | Tasks | Priority |
|---------|---------|-------|----------|
| [FE-13.1 — Limpeza de Código Morto](features/FE-13.1-limpeza-codigo-morto.md) | [US-13.1.1](stories/US-13.1.1-codebase-limpo.md) | [TK-13.1.1](tasks/TK-13.1.1-remover-ui-nao-usados.md), [TK-13.1.2](tasks/TK-13.1.2-resolver-activity-v1-v2.md), [TK-13.1.3](tasks/TK-13.1.3-centralizar-constantes.md) | P1 |
| [FE-13.2 — Componentes Reutilizáveis](features/FE-13.2-componentes-reutilizaveis.md) | [US-13.2.1](stories/US-13.2.1-componentes-compartilhados.md) | [TK-13.2.1](tasks/TK-13.2.1-week-bar-chart.md), [TK-13.2.2](tasks/TK-13.2.2-tracker-drawer.md), [TK-13.2.3](tasks/TK-13.2.3-event-log-list.md) | P1 |
| [FE-13.3 — Hooks Compartilhados](features/FE-13.3-hooks-compartilhados.md) | [US-13.3.1](stories/US-13.3.1-hook-tracker-events.md) | [TK-13.3.1](tasks/TK-13.3.1-use-tracker-events.md) | P1 |
| [FE-13.4 — Quebra de Arquivos Grandes](features/FE-13.4-quebra-arquivos-grandes.md) | [US-13.4.1](stories/US-13.4.1-arquivos-menores.md) | [TK-13.4.1](tasks/TK-13.4.1-quebrar-event-mappers.md), [TK-13.4.2](tasks/TK-13.4.2-quebrar-logsheet.md), [TK-13.4.3](tasks/TK-13.4.3-quebrar-today-page.md), [TK-13.4.4](tasks/TK-13.4.4-quebrar-feeding-detail.md) | P1 |
| [FE-13.5 — Tipagem e Higiene](features/FE-13.5-tipagem-e-higiene.md) | [US-13.5.1](stories/US-13.5.1-tipos-concretos.md) | [TK-13.5.1](tasks/TK-13.5.1-substituir-any-tipos.md) | P1 |

---

## EP-14 — Feature flags e rollout `P1`

| Feature | Stories | Tasks | Priority |
|---------|---------|-------|----------|
| [FE-14.1 — Backend de feature flags](features/FE-14.1-backend-feature-flags.md) | [US-14.1.1](stories/US-14.1.1-api-feature-flags.md) | [TK-14.1.1](tasks/TK-14.1.1-router-schemas-constants.md), [TK-14.1.2](tasks/TK-14.1.2-store-json-overrides.md), [TK-14.1.3](tasks/TK-14.1.3-totp-admin-endpoints.md), [TK-14.1.4](tasks/TK-14.1.4-tests-and-main-integration.md) | P1 |
| [FE-14.2 — Rollout na Home Hoje](features/FE-14.2-frontend-rollout-hoje.md) | [US-14.2.1](stories/US-14.2.1-ui-por-perfil-hoje.md) | [TK-14.2.1](tasks/TK-14.2.1-client-api-and-utils.md), [TK-14.2.2](tasks/TK-14.2.2-uibootstrap-fetch-flags.md), [TK-14.2.3](tasks/TK-14.2.3-today-components-rollout.md) | P1 |
| [FE-14.3 — DevEx e documentação](features/FE-14.3-devex-e-documentacao.md) | [US-14.3.1](stories/US-14.3.1-guia-operacional.md) | [TK-14.3.1](tasks/TK-14.3.1-dotenv-cors-default-port.md), [TK-14.3.2](tasks/TK-14.3.2-docs-local-run-readme-legacy.md) | P1 |

---

## Resumo Quantitativo

| Nível | Quantidade |
|-------|-----------|
| Epics | 14 |
| Features | 48 |
| User Stories | 57 |
| Tasks | 201 |
| **Total de arquivos** | **307** |

### Por Prioridade

| Prioridade | Features | Descrição |
|------------|----------|-----------|
| **P0** | 31 | MVP Core (EP-01 a EP-08, EP-12) |
| **P1** | 15 | Post-MVP (EP-09 a EP-11 + filtro cuidadores + insights + EP-13 refatoração + EP-14 feature flags) |
| **P2** | 2 | Futuro (curadoria externa, observações, saúde leve) |

## Integrações e assistentes (2026-11-11)

[EP-16/EP-17: features, user stories e sequência de entrega](INTEGRATIONS_PLAN.md).
