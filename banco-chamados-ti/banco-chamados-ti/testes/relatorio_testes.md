# Relatório de testes - Sistema de Chamados de TI

- **Estudante:** _______________________________
- **Data dos testes:** ___/___/_____
- **Ambiente:** Python ______ | SQLite | Windows
- **Como executar:** `python main.py`

> **Como usar este relatório:** execute cada teste no programa, anote o que realmente aconteceu na coluna "Resultado obtido", marque Aprovado ou Reprovado e salve o print da tela na pasta `testes/evidencias/` (ex.: `T01.png`). Se um teste falhar, descreva o problema e a correção na seção 3.

---

## 1. Resultados

| Teste | Procedimento | Resultado esperado | Resultado obtido | Aprovado / Reprovado | Evidência ou correção |
|---|---|---|---|---|---|
| T01 | Cadastrar chamado com dados válidos (opção 1) | Registro criado com ID, data e status `aberto` | | | |
| T02 | Informar solicitante só com espaços (`"     "`) | Cadastro recusado com orientação | | | |
| T03 | Informar descrição com menos de 10 caracteres (ex.: `curta`) | Cadastro recusado | | | |
| T04 | Informar prioridade não permitida (ex.: `urgente`) | Operação recusada | | | |
| T05 | Consultar ID inexistente (ex.: `999`) | Mensagem "chamado não encontrado" e programa continua | | | |
| T06 | Alterar chamado de `aberto` para `em atendimento` | Status atualizado | | | |
| T07 | Tentar alterar de `aberto` direto para `concluído` | Alteração recusada | | | |
| T08 | Concluir chamado que está `em atendimento` | Status atualizado para `concluído` | | | |
| T09 | Fechar (opção 0) e reabrir o programa, depois listar | Registros preservados | | | |
| T10 | Filtrar chamados e conferir o resumo por status | Listagem e contagens correspondem aos dados cadastrados | | | |

---

## 2. Roteiro dos dados de demonstração

Cadastre os quatro chamados abaixo e execute as ações em seguida.

| Solicitante | Descrição | Prioridade |
|---|---|---|
| Ana Souza | Computador não inicia ao pressionar o botão. | Alta |
| Bruno Lima | Impressora do setor não imprime documentos. | Média |
| Carla Santos | Solicitação de instalação de editor de texto. | Baixa |
| Diego Alves | Sistema de estoque apresenta erro no acesso. | Alta |

Ações:

1. Colocar o chamado de Ana em atendimento.
2. Colocar o chamado de Bruno em atendimento e, depois, concluí-lo.
3. Manter os outros dois chamados abertos.
4. Consultar os chamados de prioridade alta (esperado: Ana e Diego).
5. Exibir o resumo por status.

**Resumo esperado:** 2 abertos, 1 em atendimento, 1 concluído.

| Item | Resultado obtido | Confere? |
|---|---|---|
| Filtro por prioridade alta | | |
| Resumo: abertos | | |
| Resumo: em atendimento | | |
| Resumo: concluídos | | |

---

## 3. Falhas encontradas e correções

Registre aqui **qualquer** problema que apareceu durante o desenvolvimento ou os testes, mesmo que já tenha sido corrigido. Use o modelo abaixo para cada falha.

### Falha 1

- **Teste/situação em que apareceu:** ____________________
- **O que aconteceu:** ____________________
- **Causa:** ____________________
- **Correção realizada:** ____________________
- **Arquivo e função alterados:** ____________________
- **Reteste após a correção:** ( ) Aprovado ( ) Reprovado

### Falha 2

- **Teste/situação em que apareceu:** ____________________
- **O que aconteceu:** ____________________
- **Causa:** ____________________
- **Correção realizada:** ____________________
- **Arquivo e função alterados:** ____________________
- **Reteste após a correção:** ( ) Aprovado ( ) Reprovado

---

## 4. Testes extras sugeridos (opcional)

Casos fora do plano oficial que costumam revelar falhas reais:

| Situação | O que observar | Resultado |
|---|---|---|
| Digitar letras no lugar do ID (ex.: `abc`) | Mensagem de erro, sem fechar o programa | |
| Apertar Enter sem digitar nada em cada campo | Recusa com orientação | |
| Digitar `media` sem acento na prioridade | Aceita como `média` | |
| Tentar atualizar chamado já `concluído` | Recusa, informando que não pode mudar | |
| Filtrar por status sem nenhum chamado naquele status | Mensagem "Nenhum chamado encontrado" | |
| Opção inválida no menu (ex.: `9`) | Mensagem de opção inválida | |

---

## 5. Conclusão

Total de testes: 10 | Aprovados: ____ | Reprovados: ____

Observações finais: ______________________________________________