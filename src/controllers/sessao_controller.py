class SessaoController:
    def __init__(self, service):
        self.service = service

    def fechar_sessao(self, sessao_id, qtd):
        try:
            mensagem = self.service.registrar_presenca(sessao_id, qtd)
            return {"status": "OK", "msg": mensagem}
        except ValueError as e:
            return {"status": "ERRO", "msg": str(e)}