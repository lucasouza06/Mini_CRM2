# 🚀 Mini-CRM em Orientação a Objetos (POO) em Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Feito em Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)

## 📝 Descrição do Projeto

Este projeto consiste na implementação de um **Mini Sistema de Gerenciamento de Relacionamento com o Cliente (Mini-CRM)**. O objetivo principal é demonstrar a aplicação sólida e prática dos pilares da **Programação Orientada a Objetos (POO)** em uma estrutura modular em Python.

O sistema simula o cadastro de diferentes tipos de clientes (Contatos e Leads) e o registro de suas interações (ligações, reuniões), mantendo um visual de listagem profissional no terminal.

---

## 💡 Conceitos de POO Aplicados

Este projeto serve como uma excelente demonstração dos seguintes conceitos:

### 1. Classes, Atributos e Métodos
* **Classes:** Estrutura modular em `Contato`, `Interacao` e `GerenciadorCRM`.
* **Atributos:** Utilizados para definir o estado de cada objeto (ex: `nome`, `status`, `historico_interacoes`).
* **Métodos:** Definem o comportamento e as ações (ex: `adicionar_contato()`, `registrar_interacao()`, `exibir_detalhes()`).

### 2. Composição
* A classe **`Contato`** utiliza Composição ao possuir uma lista de objetos da classe **`Interacao`** (`self.historico_interacoes`). Isso modela a relação de que "o Contato TEM várias Interações".

### 3. Herança e Polimorfismo
* **Herança:** As classes **`Lead`** e **`ClienteFechado`** herdam da classe base **`Contato`**, reutilizando código e atributos básicos (`nome`, `email`) e adicionando atributos específicos (`fonte`, `valor_contrato`).
* **Polimorfismo:** Implementado no método `exibir_detalhes()`. A listagem geral chama este método, e cada objeto (seja `Lead` ou `ClienteFechado`) executa sua própria versão, exibindo o detalhe pertinente (fonte ou valor do contrato).

---

## 📂 Estrutura do Projeto

Para garantir a organização e a modularidade (Separação de Responsabilidades), o projeto está estruturado da seguinte forma:
Mini-CRM-Orientacao-Objetos/
 ├── app.py # Ponto de execução e fluxo de demonstração (o main) 
 ├── contato.py # Classes Contato, Lead e ClienteFechado (Herança/Polimorfismo) 
 ├── interacao.py # Classe Interacao (Usada para Composição) 
 ├── gerenciador_crm.py # Classe que gerencia a coleção de Contatos e a lógica 
 ├── .gitignore # Ignora arquivos de cache e ambiente virtual 
 └── README.md 
 ---

## ▶️ Como Executar o Projeto

1.  **Clone o Repositório:**
    ```bash
    git clone [https://www.youtube.com/watch?v=351MZvGXpnY](https://www.youtube.com/watch?v=351MZvGXpnY)
    cd Mini-CRM-Orientacao-Objetos
    ```
2.  **Execute o Arquivo Principal:**
    Abra o Terminal na pasta raiz do projeto e use o comando `python` ou `py`:
    ```bash
    python app.py
    # OU
    py app.py 
    ```

A saída será uma listagem formatada em tabela, demonstrando a criação dos objetos e o log de interações.

---

## 🧑‍💻 Autor

* **GitHub:** lucasouza06
* **LinkedIn:** www.linkedin.com/in/lucas-andrade-souza-01b87a2b1



---

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).# Mini_CRM2
