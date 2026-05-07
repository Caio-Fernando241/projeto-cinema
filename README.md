# 🎬 Sistema de Gestão - Rede de Cinemas

Este projeto foi desenvolvido para a disciplina de **Engenharia de Software**. O objetivo é gerenciar uma rede de cinemas, controlando o catálogo de filmes, as sessões e o registro de público, aplicando padrões arquiteturais modernos e modelagem UML.

## 🎯 Objetivos do Projeto
- Centralizar o controle de filmes e unidades de cinema.
- Gerenciar sessões respeitando a capacidade das salas.
- **Registrar e validar o público presente** (Regra de Negócio principal).
- Garantir a persistência dos dados de forma local e segura.

---

## 🏗️ Arquitetura do Sistema
O sistema segue o padrão **MVC (Model-View-Controller)** reforçado com as camadas de **Service** e **Repository**:

* **Model:** Define as entidades de domínio (ex: `Sessao.py`).
* **Repository:** Camada de persistência que utiliza **SQLite** para salvar os dados em um arquivo `.db`.
* **Service:** Onde reside a **Lógica de Negócio** (ex: validação se o público excede a capacidade).
* **Controller:** Responsável por mediar a comunicação entre a interface e os serviços.



---

## 📊 Modelagem UML
A documentação visual foi implementada utilizando a sintaxe **Mermaid**, permitindo a renderização direta no repositório.

Os diagramas detalhados podem ser encontrados na pasta `/docs`:
1. **Diagrama de Casos de Uso:** Interações entre Admin, Espectadores e o sistema.
2. **Diagrama de Classes:** Estrutura e relacionamentos entre Cinema, Filme e Sessão.
3. **Diagrama de Atividade:** Fluxo lógico do registro de público.
4. **Diagrama de Sequência:** Comunicação entre as camadas do software.

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Banco de Dados:** SQLite
- **Documentação:** Markdown + Mermaid UML

---

## 🚀 Como Executar
1. Certifique-se de ter o Python instalado.
2. Clone o repositório:
   ```bash
   git clone [https://github.com/Caio-Fernando241/projeto-cinema.git](https://github.com/Caio-Fernando241/projeto-cinema.git)
