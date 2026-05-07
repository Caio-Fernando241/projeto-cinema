class SessaoService:
    def __init__(self, repository):
        self.repository = repository

    def registrar_presenca(self, sessao_id, qtd_publico):
        sessao = self.repository.buscar_por_id(sessao_id)
        
        if not sessao:
            raise ValueError("Sessão não encontrada!")
        
        # RN02: Validação de capacidade máxima
        if qtd_publico > sessao.capacidade:
            raise ValueError(f"Capacidade excedida! Limite: {sessao.capacidade}")
        
        if qtd_publico < 0:
            raise ValueError("O público não pode ser negativo.")

        self.repository.salvar_publico(sessao_id, qtd_publico)
        return f"Sucesso! {qtd_publico} pessoas registradas no filme {sessao.filme}."