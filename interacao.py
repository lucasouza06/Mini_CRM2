class Interacao:
    """ CLASSE: Molde para registrar uma atividade de contato. """

    # MÉTODO: Construtor (Inicializa o objeto)
    def __init__(self, tipo: str, data: str, resumo: str):
        # ATRIBUTOS: Dados que definem o estado desta Interação.
        self.tipo = tipo
        self.data = data
        self.resumo = resumo

    # MÉTODO: Comportamento para exibir as informações.
    def exibir_informacoes(self):
        print(f"  Tipo: {self.tipo} | Data: {self.data}")
        print(f"  Resumo: {self.resumo}")