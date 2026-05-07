class Sessao:
    """Entidade que representa uma sessão no cinema."""
    def __init__(self, id_sessao, filme_titulo, cinema_nome, capacidade_sala, publico_presente=0):
        self.id = id_sessao
        self.filme = filme_titulo
        self.cinema = cinema_nome
        self.capacidade = capacidade_sala
        self.publico = publico_presente