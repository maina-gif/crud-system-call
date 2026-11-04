PRIORIDADES = ("baixa", "média", "alta")
STATUS = ("aberto", "em atendimento", "concluído")

# Transições permitidas: status atual -> próximo status
TRANSICOES = {
    "aberto": "em atendimento",
    "em atendimento": "concluído",
}


def validar_solicitante(texto):
    texto = texto.strip()
    if len(texto) < 3:
        return None, "Solicitante deve ter pelo menos 3 caracteres."
    return texto, None


def validar_descricao(texto):
    texto = texto.strip()
    if len(texto) < 10:
        return None, "Descrição deve ter pelo menos 10 caracteres."
    return texto, None


def validar_prioridade(texto):
    texto = texto.strip().lower()
    if texto == "media":
        texto = "média"
    if texto not in PRIORIDADES:
        return None, "Prioridade inválida. Use: baixa, média ou alta."
    return texto, None


def transicao_valida(status_atual, novo_status):
    return TRANSICOES.get(status_atual) == novo_status