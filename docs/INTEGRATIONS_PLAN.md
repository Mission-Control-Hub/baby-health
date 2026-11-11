# Integrações e assistentes — contrato de produto

2026-11-11. Fluxo: feature/* → development → main, sempre por PR. development é a branch dev existente. A revisão anterior do backlog permanece no checkout principal.

## Modelo de autorização

Cada API key e conexão MCP tem credencial, perfil/família e concessões próprias. Sem acesso por padrão. Módulos estáveis: feeding, sleep, hydration, diapers, activities, growth, health, milestones, caregivers, profile, integrations. Não usar IDs de épicos como scopes.

Read consulta; write cria/edita; delete exclui; admin inclui essas três ações e configurações do módulo. Write não implica read nem delete. Admin de alimentação não concede acesso a cuidadores. Permissões efetivas são a interseção das concessões com as permissões do usuário emissor. Revogação e expiração valem em cada chamada; revogar usuário também invalida sua integração. Usuários do sistema atual têm acesso integral ao próprio perfil; gestão de papéis humanos será necessária para restringir esse acesso no futuro.

## EP-16 — Integrações, API e webhooks

| Feature | User stories e critérios de aceite | Estado |
|---|---|---|
| FE-16.1 Credenciais | US-16.1.1: como usuário, criar chave nomeada com grants e expiração; segredo exibido apenas na criação e armazenado como hash. US-16.1.2: listar metadados e revogar imediatamente, sem expor hashes. US-16.1.3: chave não acessa login nem rotas legadas via JWT. | Primeiro incremento |
| FE-16.2 Permissões e eventos | US-16.2.1: configurar read/write/delete/admin por módulo. US-16.2.2: negar outro perfil, outro tipo de evento e autoria forjada. US-16.2.3: consultar/criar/editar/excluir eventos respeitando grants em cada chamada. | Primeiro incremento |
| FE-16.3 API documentada | US-16.3.1: abrir Swagger pelo app, autorizar com chave e consultar schemas/erros. US-16.3.2: filtros/paginação, limites de uso e versão estável. | Swagger no incremento; paginação/limites pendentes |
| FE-16.4 Administração por API | US-16.4.1: administrar perfil/cuidadores/configurações por módulo. US-16.4.2: delegar apenas subconjunto das próprias permissões; proibir autoelevação. | Pendente; módulos ainda não expostos falham fechados |
| FE-16.5 Webhooks | US-16.5.1: cadastrar endpoint HTTPS e eventos por módulo. US-16.5.2: receber created/updated/deleted com event_id, perfil e autoria. US-16.5.3: verificar assinatura HMAC e timestamp. US-16.5.4: consultar tentativas, reenviar e revogar assinatura. | Pendente |
| FE-16.6 Entrega confiável e auditoria | US-16.6.1: outbox persistente, entrega pelo menos uma vez, retries com backoff e fila de falhas. US-16.6.2: idempotency-key para não duplicar registros por retry. US-16.6.3: log de ator humano, credencial, canal, ação e recurso sem segredos/dados clínicos nos logs. | Pendente |

Webhooks: bloquear destinos privados/loopback/link-local e redirects, revalidar resolução DNS, limitar tempo/tamanho; não efetuar rede no request que salva evento. Assinatura associada ao perfil e grants; mudanças de permissões impedem novas entregas indevidas. Eventos de UI e MCP usam o mesmo serviço/outbox. Secrets de assinatura precisam de armazenamento cifrado gerenciado.

## EP-17 — MCP e administração por assistentes

| Feature | User stories e critérios de aceite | Estado |
|---|---|---|
| FE-17.1 Servidor remoto | US-17.1.1: conectar cliente compatível ao transporte HTTP padronizado; validar protocolo e lifecycle com SDK oficial. | Pendente |
| FE-17.2 Conexões e autorização | US-17.2.1: autorizar um perfil e módulos por conexão; revogar e expirar. US-17.2.2: descoberta OAuth e autorização conforme cliente, consentimento e tokens vinculados ao resource/audience; não presumir que ChatGPT aceite API key manual. | Pendente |
| FE-17.3 Operações de cuidado | US-17.3.1: perguntar última mamada e registrar 150 ml com horário/fuso explícito. US-17.3.2: corrigir registro por ID e evitar duplicação em retry. Ferramentas somente com grants efetivos; backend revalida tools/call. | Pendente |
| FE-17.4 Administração | US-17.4.1: gerenciar cuidadores, perfil e integrações com admin do módulo. US-17.4.2: exclusão apenas com delete/admin e sem elevar grants delegados. | Pendente |
| FE-17.5 Rastreabilidade | US-17.5.1: enxergar no histórico quem registrou e por qual conexão. US-17.5.2: revogação durante sessão impede a chamada seguinte; isolar famílias e ferramentas. | Pendente |

## Sequência de implementação

1. API keys + grants + eventos + UI + Swagger e testes negativos (este incremento).
2. Administração dos demais módulos, idempotência e auditoria persistente.
3. Outbox, worker e configuração/monitoramento de webhooks.
4. MCP com SDK oficial, OAuth e testes com cliente real.

Nada deste plano constitui publicação em produção. Antes de promover: testes, validação de interface e persistência GCS; staging é decisão de ambiente separada do nome development.
