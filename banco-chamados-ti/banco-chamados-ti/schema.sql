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