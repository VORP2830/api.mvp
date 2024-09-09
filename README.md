# Stock Trading API

## Descrição

Esta é uma API para gerenciamento de ações, desenvolvida em Flask e documentada com Swagger (OpenAPI). A API permite criar, ler, atualizar e deletar registros de ações no banco de dados SQLite. O projeto segue uma arquitetura modular e simples, facilitando a integração e manutenção.

## Instruções de Instalação

### 1. Configurando o Ambiente Local

Siga as etapas abaixo para configurar o ambiente local:

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/VORP2830/stock-trading-api.git
    ```

2. **Navegue até o diretório do projeto**:

    ```bash
    cd stock-trading-api
    ```

3. **Instale as dependências necessárias**:

    ```bash
    pip install -r requirements.txt
    ```

### 2. Executando a Aplicação

Para rodar a aplicação localmente, utilize o seguinte comando:

```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5001`.

### 3. Acessando a Documentação da API

Após iniciar o projeto, você pode acessar a documentação interativa da API via Swagger, navegando até:

```
http://localhost:5001/openapi/swagger
```

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
├── app.py                # Arquivo principal onde a aplicação Flask é executada
├── database.py           # Configuração e inicialização do banco de dados
├── models/               # Diretório que contém os modelos de dados
│   └── stock.py          # Modelo da tabela Stock
├── config.py             # Configurações do projeto (como credenciais do banco de dados)
└── README.md             # Este arquivo README com as instruções do projeto
```