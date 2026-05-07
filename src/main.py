from repositories.sessao_repository import SessaoRepository
from services.sessao_service import SessaoService
from controllers.sessao_controller import SessaoController

def main():
    # Injeção de Dependências
    repo = SessaoRepository()
    service = SessaoService(repo)
    controller = SessaoController(service)

    print("=== SISTEMA DE GESTÃO DE CINEMA ===")
    
    try:
        id_sessao = int(input("Informe o ID da Sessão (Ex: 1): "))
        publico = int(input("Informe o público presente: "))
        
        resultado = controller.fechar_sessao(id_sessao, publico)
        
        if resultado["status"] == "OK":
            print(f"✅ {resultado['msg']}")
        else:
            print(f"❌ {resultado['msg']}")
            
    except ValueError:
        print("❌ Erro: Por favor, digite apenas números.")

if __name__ == "__main__":
    main()