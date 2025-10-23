# Arquivo: app.py (ou Fluxo.py) - Ponto de Execução

from gerenciador_crm import GerenciadorCRM
from interacao import Interacao
from contato import ClienteFechado 


def rodar_aplicacao():
    print("=" * 90)
    print("💼 SISTEMA MINI-CRM | RELACIONAMENTO E VENDAS (POO) 🚀")
    print("=" * 90)
    
    # CRIAÇÃO DO OBJETO principal de gerenciamento.
    crm = GerenciadorCRM() 

    # CRIAÇÃO DE OBJETOS: Instâncias das Classes Contato, Lead e ClienteFechado.
    c1 = crm.adicionar_contato("Charles do Bronx", "Octagon Fighters", "charles@ufc.com")
    l1 = crm.adicionar_lead("Louro José", "Mais Você S.A.", "louro@anamaria.com", "Indicação da Anamaria")
    c3 = crm.adicionar_contato("Alexandre Russi", "FIAP Educa", "alexandre@fiap.com.br") 

    # DEMONSTRAÇÃO DE POLIMORFISMO E HERANÇA: Cria o ClienteFechado.
    c3_final = ClienteFechado(c3.id, c3.nome, c3.empresa, c3.email, 10000.00) 
    crm.contatos[c3.id] = c3_final 

    # CRIAÇÃO DE OBJETOS da Classe Interacao
    i1 = Interacao("Reunião", "2025-10-20", "Reunião para fechar o patrocínio. Tema: 'Finalização'!")
    i2 = Interacao("Whatsapp", "2025-10-21", "Louro José mandou um áudio dizendo: 'Acorda, menina!'")
    i3 = Interacao("E-mail", "2025-10-22", "E-mail enviado sobre a nota máxima no projeto de POO.")

    # CHAMADA DE MÉTODO: Chamando o método em diferentes objetos (demonstra Comportamento).
    c1.registrar_interacao(i1)       
    l1.registrar_interacao(i2)       
    c3_final.registrar_interacao(i3) 

    # CHAMADA DE MÉTODO: Lista e demonstra o Polimorfismo no visual profissional.
    crm.listar_todos_contatos()
        
    print("\n" + "📌" * 45)
    print(f"HISTÓRICO COMPLETO DE INTERAÇÕES: {c3_final.nome}")
    print("📌" * 45)
    # Exibição do histórico (DEMONSTRAÇÃO DA COMPOSIÇÃO: acesso aos objetos Interacao).
    for interacao in c3_final.historico_interacoes:
        print("-" * 90) 
        interacao.exibir_informacoes()


if __name__ == "__main__":
    rodar_aplicacao()