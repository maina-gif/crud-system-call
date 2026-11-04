# Sistema de Controle de Chamados de TI - TechServ

Aplicação de terminal para registrar, consultar e acompanhar chamados de suporte de TI.
Desenvolvida em **Python** com banco de dados **SQLite**.

- **Estudante:** _______________________________
- **Turma:** ______________  **Data:** ___/___/_____

---

## Requisitos

- Python 3.8 ou superior
- SQLite (já incluso no Python, não precisa instalar nada)
- Nenhuma biblioteca externa

Para conferir a instalação:

```
python --version
```

(No Windows, se `python` não funcionar, use `py --version`.)

## Como executar

1. Extraia a pasta compactada.
2. Abra o terminal dentro da pasta do projeto (onde está o `main.py`).
3. Execute:

```
python main.py
```

Se o comando `python` não for reconhecido, use `py main.py`.

O arquivo `chamados.db` e a tabela `chamados` são criados automaticamente na primeira execução, a partir do `schema.sql`.

## Funcionalidades (menu)

| Opção | Função |
|---|---|
| 1 | Cadastrar chamado (solicitante, descrição, prioridade) |
| 2 | Listar todos os chamados |
| 3 | Consultar chamado por ID |
| 4 | Atualizar status |
| 5 | Filtrar por prioridade ou por status |
| 6 | Resumo com a quantidade de chamados por status |
| 0 | Sair |

## Regras de negócio

- **Solicitante:** obrigatório, mínimo de 3 caracteres (espaços nas pontas são removidos).
- **Descrição:** obrigatória, mínimo de 10 caracteres (espaços nas pontas são removidos).
- **Prioridade:** `baixa`, `média` ou `alta`.
- **Status:** `aberto`, `em atendimento` ou `concluído`.
- Todo chamado nasce com status **aberto**.
- Transições permitidas: `aberto` → `em atendimento` → `concluído`. Qualquer outra é recusada.
- Chamados concluídos continuam disponíveis para consulta.
- ID inexistente gera mensagem clara e o programa continua em execução.
- Os dados são salvos no arquivo `chamados.db` e permanecem após fechar o programa.
- Todas as consultas SQL usam parâmetros (`?`), nunca concatenação de texto.

## Estrutura da pasta

```
banco-chamados-ti/
├── main.py                    # menu e interação com o usuário
├── database.py                # conexão e consultas SQL
├── validacoes.py              # regras de negócio e validações
├── schema.sql                 # script de criação da tabela
├── chamados.db                # banco de dados (gerado automaticamente)
├── modelo_dados.md            # modelo da tabela de chamados
├── LEIA-ME.md                 # este arquivo
└── testes/
    └── relatorio_testes.md    # resultados dos testes T01 a T10
```

## Reiniciar o banco (opcional)

Para começar do zero, feche o programa, apague o arquivo `chamados.db` e execute `python main.py` novamente. A tabela será recriada vazia.

## Dados de demonstração

| Solicitante | Descrição | Prioridade |
|---|---|---|
| Ana Souza | Computador não inicia ao pressionar o botão. | Alta |
| Bruno Lima | Impressora do setor não imprime documentos. | Média |
| Carla Santos | Solicitação de instalação de editor de texto. | Baixa |
| Diego Alves | Sistema de estoque apresenta erro no acesso. | Alta |

Depois do cadastro: colocar o chamado de Ana em atendimento; colocar o de Bruno em atendimento e concluí-lo; manter os outros dois abertos.

**Resumo esperado:** 2 abertos, 1 em atendimento, 1 concluído.
