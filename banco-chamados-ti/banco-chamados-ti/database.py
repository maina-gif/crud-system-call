import sqlite3
from pathlib import Path 

DB_PATH = Path (__file__).parent / "chamados.db"
SCHEMA_PATH = Path (__file__).parent / "schema.sql"


def conectar():
    conexao = sqlite3.connect(DB_PATH)
    conexao.row_factory = sqlite3.Row
    return conexao

def inicializar_banco():
   with conectar() as con:
    con.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))


def inserir_chamado(solicitante, descricao, status):
    sql = """
        INSERT INTO chamados (solicitante, descricao, status)
        VALUES (?, ?, ?)
    """
    with conectar() as con:
         cursor = con.execute(sql, (solicitante, descricao, status))
         return cursor.lastrowid



def listar_chamados():
    with conectar() as con:
        return con.execute("SELECT * FROM chamados ORDER BY id").fetchall()


def buscar_por_id(id_chamado):
    with conectar() as con:
        return con.execute(
            "SELECT * FROM chamados WHERE id = ?", (id_chamado,)
        ).fetchone()


def atualizar_status(id_chamado, novo_status):
    with conectar() as con:
        con.execute(
            "UPDATE chamados SET status = ? WHERE id = ?",
            (novo_status, id_chamado),
        )


def filtrar_por_prioridade(prioridade):
    with conectar() as con:
        return con.execute(
            "SELECT * FROM chamados WHERE prioridade = ? ORDER BY id",
            (prioridade,),
        ).fetchall()


def filtrar_por_status(status):
    with conectar() as con:
        return con.execute(
            "SELECT * FROM chamados WHERE status = ? ORDER BY id",
            (status,),
        ).fetchall()


def resumo_por_status():
    with conectar() as con:
        linhas = con.execute(
            "SELECT status, COUNT(*) AS total FROM chamados GROUP BY status"
        ).fetchall()
    resumo = {"aberto": 0, "em atendimento": 0, "concluído": 0}
    for linha in linhas:
        resumo[linha["status"]] = linha["total"]
    return resumo