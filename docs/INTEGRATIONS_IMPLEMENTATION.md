# Primeiro incremento — API keys

Branch feature/integrations-mcp baseada em development 49e9d68. Não publicada em produção.

## Disponível nesta branch

- Tela /integrations acessível pelo link Integrações; sessão JWT para criar/listar/revogar as próprias chaves.
- Nome, grants por módulo e expiração obrigatória; segredo de alta entropia retornado apenas na criação, hash SHA-256 armazenado em registros individuais locais ou GCS. Respostas de integrações/API v1 usam Cache-Control: no-store.
- /api/v1/events: GET exige event_type e baby_id, POST cria, PATCH corrige, DELETE exclui. Chave Bearer no esquema IntegrationApiKey do Swagger em /docs.
- Backend revalida perfil e usuário emissor a cada chamada. Autor dos registros deriva do usuário, ignorando caregiver_id forjado. API keys não são aceitas nos endpoints JWT existentes.
- Permissões independentes read/write/delete; admin inclui todas dentro do módulo. Tipo de evento não pode ser alterado pelo PATCH para atravessar módulo.

## Limites explícitos

Este incremento expõe somente eventos. Grants dos outros módulos ainda não habilitam endpoints administrativos. Não implementa delegação por chave, MCP, OAuth, webhooks, idempotência, auditoria de canal nem limites/paginação. Esses itens possuem features e critérios no plano; não considerar EP-16/17 concluídos. Persistência GCS validada com cliente simulado, não com conta GCP real. A UI foi compilada, sem homologação visual.

## Validação

- Python 3.14 em venv temporário: 62 testes do backend passaram, incluindo 8 testes de integrações.
- npm ci + npm run build: compilação passou, aviso de bundle grande já existente.
- Adicionada dependência email-validator, necessária pelo onboarding existente; workflow de testes instala httpx.
- Fixtures antigas de mídia e bootstrap atualizadas para autenticação/perfil temporário, preservando a autenticação de produção.

## Fluxo Git

main/development com ruleset ativo, sem bypass: impedir exclusão e force push, exigir PR e check Gitflow. Check rejeita PR de outra origem para main e exige ancestry de development nas features. Primeira entrega deve entrar em development; promoção futura vem exclusivamente de development para main. O ruleset exige esse check também antes de a versão do workflow entrar nas branches de destino.
