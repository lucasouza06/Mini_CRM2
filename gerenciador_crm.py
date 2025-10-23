# Arquivo: gerenciador_crm.py

from contato import Contato, Lead, ClienteFechado 

class GerenciadorCRM:
    """ CLASSE: Gerencia a coleção de objetos Contato e a lógica de negócio. """
    
    # MÉTODO: Construtor
    def __init__(self):
        # ATRIBUTO: Coleção principal de objetos Contato.
        self.contatos = {} 
        self.proximo_id = 1

    # MÉTODO: Cria e adiciona um OBJETO Contato.
    def adicionar_contato(self, nome: str, empresa: str, email: str) -> Contato:
        # CRIAÇÃO DE OBJETO (instância da Classe Contato)
        novo_contato = Contato(self.proximo_id, nome, empresa, email) 
        self.contatos[self.proximo_id] = novo_contato
        self.proximo_id += 1
        return novo_contato

    # MÉTODO: Cria e adiciona um OBJETO Lead (usa a classe herdada).
    def adicionar_lead(self, nome: str, empresa: str, email: str, fonte: str) -> Lead:
        novo_lead = Lead(self.proximo_id, nome, empresa, email, fonte)
        self.contatos[self.proximo_id] = novo_lead
        self.proximo_id += 1
        return novo_lead
        
    # MÉTODO: Comportamento para listar todos.
    def listar_todos_contatos(self):
        TOTAL_LARGURA = 100 
        
        print("\n" + "=" * TOTAL_LARGURA)
        print("📊 RELATÓRIO PROFISSIONAL DE CONTATOS | VISÃO GERAL")
        print("=" * TOTAL_LARGURA)
        
        # Cabeçalho da Tabela
        header = f"| {'ID':<3} | {'NOME DO CONTATO':<20} | {'EMPRESA':<20} | {'STATUS':<25} | {'EMAIL':<20} |"
        print(header)
        print("-" * TOTAL_LARGURA)
            
        for contato_id in self.contatos:
            contato = self.contatos[contato_id]
            
            # Linha Principal da Tabela (Dados Comuns)
            linha_dados = f"| {contato.id:<3} | {contato.nome:<20} | {contato.empresa:<20} | {contato.status:<25} | {contato.email:<20} |"
            print(linha_dados)
            
            # POLIMORFISMO: Chama o método exibir_detalhes() de cada objeto.
            contato.exibir_detalhes() 
            print("-" * TOTAL_LARGURA) 
            
    # MÉTODO: Comportamento para buscar um objeto.
    def buscar_contato(self, id_contato: int) -> Contato | None:
        return self.contatos.get(id_contato)