# Modelo de dados - Sistema de Chamados de TI

**Banco de dados:** SQLite (arquivo `chamados.db`)
**Tabela:** `chamados` (única tabela do sistema)

## Estrutura da tabela

| Campo | Tipo | Chave | Restrições | Descrição |
|---|---|---|---|---|
| `id` | INTEGER | **PK** | AUTOINCREMENT | Identificador único, gerado automaticamente |
| `solicitante` | TEXT | | NOT NULL; `length(trim(solicitante)) >= 3` | Nome de quem abriu o chamado |
| `descricao` | TEXT | | NOT NULL; `length(trim(descricao)) >= 10` | Descrição do problema |
| `prioridade` | TEXT | | NOT NULL; apenas `baixa`, `média` ou `alta` | Urgência do chamado |
| `status` | TEXT | | NOT NULL; DEFAULT `aberto`; apenas `aberto`, `em atendimento` ou `concluído` | Situação atual do atendimento |
| `data_abertura` | TEXT | | NOT NULL; DEFAULT data/hora local atual | Registrada automaticamente na criação |

## Justificativa das escolhas

- **`id` como chave primária com AUTOINCREMENT:** garante identificador único e gerado automaticamente, sem depender do usuário.
- **`CHECK` nas colunas:** o próprio banco recusa dados inválidos. É uma segunda camada de proteção, além das validações feitas no código (`validacoes.py`).
- **`DEFAULT 'aberto'`:** todo chamado nasce aberto, mesmo que o código não informe o status.
- **`DEFAULT` na data:** a data de abertura é preenchida pelo banco, sem possibilidade de esquecimento.
- **Tipo TEXT para datas:** o SQLite não possui tipo de data próprio; o padrão é guardar em texto no formato `AAAA-MM-DD HH:MM:SS`.
- **Tabela única:** o enunciado pede apenas o controle de chamados, então não há necessidade de normalizar em outras tabelas.

## Diagrama

```
┌────────────────────────────────────────┐
│               chamados                 │
├────────────────────────────────────────┤
│ PK  id             INTEGER             │
│     solicitante    TEXT     NOT NULL   │
│     descricao      TEXT     NOT NULL   │
│     prioridade     TEXT     NOT NULL   │
│     status         TEXT     NOT NULL   │
│     data_abertura  TEXT     NOT NULL   │
└────────────────────────────────────────┘
```

## Máquina de estados do campo `status`

```
 [criação] ──► aberto ──► em atendimento ──► concluído
                                              (final)
```

Não é permitido pular etapas (`aberto` → `concluído`) nem voltar (`concluído` → qualquer outro).

## Script de criação

```sql
CREATE TABLE IF NOT EXISTS chamados (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    solicitante   TEXT NOT NULL
                  CHECK (length(trim(solicitante)) >= 3),
    descricao     TEXT NOT NULL
                  CHECK (length(trim(descricao)) >= 10),
    prioridade    TEXT NOT NULL
                  CHECK (prioridade IN ('baixa', 'média', 'alta')),
    status        TEXT NOT NULL DEFAULT 'aberto'
                  CHECK (status IN ('aberto', 'em atendimento', 'concluído')),
    data_abertura TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
);
```

## Principais consultas (todas parametrizadas)

| Operação | SQL |
|---|---|
| Cadastrar | `INSERT INTO chamados (solicitante, descricao, prioridade) VALUES (?, ?, ?)` |
| Listar | `SELECT * FROM chamados ORDER BY id` |
| Consultar | `SELECT * FROM chamados WHERE id = ?` |
| Atualizar status | `UPDATE chamados SET status = ? WHERE id = ?` |
| Filtrar por prioridade | `SELECT * FROM chamados WHERE prioridade = ? ORDER BY id` |
| Filtrar por status | `SELECT * FROM chamados WHERE status = ? ORDER BY id` |
| Resumo | `SELECT status, COUNT(*) AS total FROM chamados GROUP BY status` |