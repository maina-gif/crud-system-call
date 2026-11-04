import database as db
import validacoes as v


def pedir_id():
    """Lê um ID do teclado. Retorna None se não for número."""
    entrada = input("ID do chamado: ").strip()
    if not entrada.isdigit():
        print("⚠ ID inválido. Digite apenas números.")
        return None
    return int(entrada)


def mostrar_chamado(c):
    print(f"[#{c['id']}] {c['solicitante']} | {c['prioridade'].upper()} "
          f"| {c['status']} | aberto em {c['data_abertura']}")
    print(f"     {c['descricao']}")


def mostrar_lista(chamados):
    if not chamados:
        print("Nenhum chamado encontrado.")
        return
    for c in chamados:
        mostrar_chamado(c)


def cadastrar():
    print("\n--- Novo chamado ---")
    solicitante, erro = v.validar_solicitante(input("Solicitante: "))
    if erro:
        print("⚠", erro); return
    descricao, erro = v.validar_descricao(input("Descrição: "))
    if erro:
        print("⚠", erro); return
    prioridade, erro = v.validar_prioridade(input("Prioridade (baixa/média/alta): "))
    if erro:
        print("⚠", erro); return

    novo_id = db.inserir_chamado(solicitante, descricao, prioridade)
    print(f"✔ Chamado #{novo_id} cadastrado com status 'aberto'.")


def listar():
    print("\n--- Todos os chamados ---")
    mostrar_lista(db.listar_chamados())


def consultar():
    id_chamado = pedir_id()
    if id_chamado is None:
        return
    chamado = db.buscar_por_id(id_chamado)
    if chamado is None:
        print(f"⚠ Chamado #{id_chamado} não encontrado.")
        return
    mostrar_chamado(chamado)


def atualizar():
    id_chamado = pedir_id()
    if id_chamado is None:
        return
    chamado = db.buscar_por_id(id_chamado)
    if chamado is None:
        print(f"⚠ Chamado #{id_chamado} não encontrado.")
        return

    atual = chamado["status"]
    proximo = v.TRANSICOES.get(atual)
    if proximo is None:
        print(f"⚠ Chamado #{id_chamado} já está '{atual}' e não pode mudar.")
        return

    print(f"Status atual: {atual}")
    novo = input(f"Novo status ({proximo}): ").strip().lower()
    if not v.transicao_valida(atual, novo):
        print(f"⚠ Transição recusada. De '{atual}' só é possível ir para '{proximo}'.")
        return

    db.atualizar_status(id_chamado, novo)
    print(f"✔ Chamado #{id_chamado} agora está '{novo}'.")


def filtrar():
    print("1. Por prioridade\n2. Por status")
    opcao = input("Escolha: ").strip()
    if opcao == "1":
        valor, erro = v.validar_prioridade(input("Prioridade: "))
        if erro:
            print("⚠", erro); return
        mostrar_lista(db.filtrar_por_prioridade(valor))
    elif opcao == "2":
        valor = input("Status (aberto/em atendimento/concluído): ").strip().lower()
        if valor not in v.STATUS:
            print("⚠ Status inválido."); return
        mostrar_lista(db.filtrar_por_status(valor))
    else:
        print("⚠ Opção inválida.")


def resumo():
    print("\n--- Resumo por status ---")
    for status, total in db.resumo_por_status().items():
        print(f"{status}: {total}")


def menu():
    acoes = {
        "1": cadastrar, "2": listar, "3": consultar,
        "4": atualizar, "5": filtrar, "6": resumo,
    }
    while True:
        print("\n===== TECHSERV - CHAMADOS DE TI =====")
        print("1. Cadastrar chamado\n2. Listar chamados\n3. Consultar por ID")
        print("4. Atualizar status\n5. Filtrar chamados\n6. Resumo por status\n0. Sair")
        escolha = input("Escolha: ").strip()
        if escolha == "0":
            print("Até logo!")
            break
        acao = acoes.get(escolha)
        if acao:
            acao()
        else:
            print("⚠ Opção inválida.")


if __name__ == "__main__":
    db.inicializar_banco()
    menu()