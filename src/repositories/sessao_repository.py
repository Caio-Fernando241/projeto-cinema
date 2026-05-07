import sqlite3
import os

class SessaoRepository:
    def __init__(self, db_path="database/cinema.db"):
        self.db_path = db_path
        self._inicializar_db()

    def _inicializar_db(self):
        # Cria a pasta database se não existir
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS sessoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filme TEXT NOT NULL,
                    cinema TEXT NOT NULL,
                    capacidade INTEGER NOT NULL,
                    publico INTEGER DEFAULT 0
                )
            """)
            # Insere dados de teste apenas se a tabela estiver vazia
            cursor = conn.cursor()
            cursor.execute("SELECT count(*) FROM sessoes")
            if cursor.fetchone()[0] == 0:
                conn.execute("INSERT INTO sessoes (filme, cinema, capacidade) VALUES ('Batman', 'Cine Centro', 100)")
                conn.execute("INSERT INTO sessoes (filme, cinema, capacidade) VALUES ('Avatar 2', 'Cine Norte', 150)")

    def buscar_por_id(self, sessao_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sessoes WHERE id = ?", (sessao_id,))
            row = cursor.fetchone()
            if row:
                from models.sessao import Sessao
                return Sessao(row[0], row[1], row[2], row[3], row[4])
            return None

    def salvar_publico(self, sessao_id, qtd):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("UPDATE sessoes SET publico = ? WHERE id = ?", (qtd, sessao_id))