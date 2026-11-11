# BabyHealth — desenvolvimento

- Criar branches de feature a partir de origin/development atualizado.
- PRs de feature têm development como base. Apenas development pode abrir promoção para main.
- Não fazer push direto, force push ou excluir main/development.
- Não confundir integração em development com deploy em produção.
- Aplicar permissões de integração no backend, por perfil e módulo, falhando fechado.
- Não registrar segredos nem retornar hashes de API keys.
