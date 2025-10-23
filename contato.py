from interacao import Interacao

class Contato:
    """ CLASSE BASE: Entidade principal do CRM. """
    
    # MÉTODO: Construtor
    def __init__(self, id_contato: int, nome: str, empresa: str, email: str, status: str = "Novo"):
        # ATRIBUTOS: Dados básicos.
        self.id = id_contato
        self.nome = nome
        self.empresa = empresa
        self.email = email
        self.status = status
        
        # COMPOSIÇÃO: Contato possui objetos da classe Interacao.
        self.historico_interacoes = [] 
        
    # MÉTODO: Exibe os detalhes.
    def exibir_detalhes(self):
        total_interacoes = f"Total de Interações: {len(self.historico_interacoes)}"
        print(f"| {'':<60} | {total_interacoes:<26} |") 
        
    # MÉTODO: Registra a interação no histórico.
    def registrar_interacao(self, interacao: Interacao):
        self.historico_interacoes.append(interacao)


class Lead(Contato):
    """ CLASSE HERDEIRA: Subclasse para Leads. (DEMONSTRA HERANÇA) """
    
    def __init__(self, id_contato: int, nome: str, empresa: str, email: str, fonte: str):
        # HERANÇA: Chama o construtor da classe 'mãe' (Contato).
        super().__init__(id_contato, nome, empresa, email, status="Lead - Prospecção") 
        self.fonte = fonte 
        
    # MÉTODO: Sobrescrito (DEMONSTRA POLIMORFISMO)
    def exibir_detalhes(self):
        detalhe = f"DETALHE: Fonte de Aquisição: {self.fonte}"
        print(f"| {detalhe:<60} | {'':<26} |") 
        super().exibir_detalhes() 

class ClienteFechado(Contato):
    """ CLASSE HERDEIRA: Subclasse para Clientes Ativos. (DEMONSTRA HERANÇA) """
    
    def __init__(self, id_contato: int, nome: str, empresa: str, email: str, valor_contrato: float):
        # HERANÇA: Chama o construtor da classe 'mãe'.
        super().__init__(id_contato, nome, empresa, email, status="Cliente Ativo")
        self.valor_contrato = valor_contrato

    # MÉTODO: Sobrescrito (DEMONSTRA POLIMORFISMO)
    def exibir_detalhes(self):
        valor_str = f"Contrato Fechado (Valor: R$ {self.valor_contrato:.2f})"
        detalhe = f"DETALHE: {valor_str}"
        print(f"| {detalhe:<60} | {'':<26} |") 
        super().exibir_detalhes()