# 📚 Sistema de Gerenciamento de Livraria 

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![JSON Server](https://img.shields.io/badge/JSON%20Server-Latest-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Sistema completo de gerenciamento de livraria desenvolvido em Python com API RESTful utilizando JSON Server. Implementa operações CRUD, transações de vendas com controle de estoque, pesquisa avançada e visualizações gráficas em ASCII.

## 📋 Índice

- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [API Endpoints](#-api-endpoints)
- [Demonstração](#-demonstração)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

## ✨ Funcionalidades

### 🔹 CRUD Completo de Livros
- ✅ Criar novos livros no sistema
- ✅ Listar todos os livros cadastrados
- ✅ Atualizar informações de livros existentes
- ✅ Remover livros do sistema
- ✅ Suporte a IDs alfanuméricos

### 🔹 Gerenciamento de Vendas
- ✅ Realizar vendas com controle automático de estoque
- ✅ Listar histórico de vendas
- ✅ Atualizar informações de vendas
- ✅ Cancelar vendas (restaura estoque automaticamente)
- ✅ Validação de estoque antes da venda

### 🔹 Pesquisa Avançada
- 🔍 Busca por autor
- 🔍 Filtro por categoria
- 🔍 Filtro por preço máximo
- 🔍 Combinação de múltiplos filtros

### 🔹 Visualizações Gráficas
- 📊 Gráfico de livros por categoria (ASCII art)
- 📈 Gráfico de vendas por livro (ASCII art)
- 📉 Análise visual diretamente no terminal

## 🛠 Tecnologias

- **Python 3.8+** - Linguagem de programação
- **JSON Server** - Servidor REST API fake
- **Requests** - Biblioteca HTTP para Python
- **Collections** - Manipulação de dados

## 📦 Pré-requisitos

Antes de começar, você precisará ter instalado:

- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/) (para o JSON Server)
- pip (gerenciador de pacotes Python)

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/livraria-api-system.git
cd livraria-api-system
```

### 2. Instale o JSON Server

```bash
npm install -g json-server
```

### 3. Instale as dependências Python

```bash
pip install requests
```

## 💻 Como Usar

### Passo 1: Iniciar o JSON Server

```bash
json-server --watch db.json --port 3000
```

Você verá:
```
Resources
http://localhost:3000/livros
http://localhost:3000/vendas

Home
http://localhost:3000
```

### Passo 2: Executar a Aplicação

Em outro terminal:

```bash
python livraria_api.py
```

### Menu Principal

```
============================================================
    SISTEMA DE GERENCIAMENTO DE LIVRARIA
============================================================

[1] Gerenciar Livros (CRUD)
[2] Gerenciar Vendas (CRUD)
[3] Pesquisa Avançada de Livros
[4] Gráfico: Livros por Categoria
[5] Gráfico: Vendas por Livro
[0] Sair
```

## 📂 Estrutura do Projeto

```
livraria-api-system/
│
├── livraria_api.py      # Aplicação principal
├── db.json              # Banco de dados JSON
├── README.md            # Este arquivo
└── .gitignore           # Arquivos ignorados pelo Git
```

## 🔌 API Endpoints

### Livros

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/livros` | Lista todos os livros |
| GET | `/livros/:id` | Busca livro por ID |
| POST | `/livros` | Cria novo livro |
| PUT | `/livros/:id` | Atualiza livro |
| DELETE | `/livros/:id` | Deleta livro |

### Vendas

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/vendas` | Lista todas as vendas |
| GET | `/vendas/:id` | Busca venda por ID |
| POST | `/vendas` | Cria nova venda |
| PUT | `/vendas/:id` | Atualiza venda |
| DELETE | `/vendas/:id` | Deleta venda |

## 🎬 Demonstração

### Exemplo: Cadastrar um Livro

```
[1] Criar Livro
Título: Design Patterns
Autor: Gang of Four
Preço: R$ 105.00
Estoque: 10
Categoria: Programação

✓ Livro 'Design Patterns' criado com sucesso!
```

### Exemplo: Realizar uma Venda

```
[1] Realizar Venda
ID do livro: 1
Quantidade: 2
Nome do cliente: João Silva

✓ Venda realizada com sucesso! Total: R$ 179.80
```

### Exemplo: Gráfico no Terminal

```
======================================================================
           GRÁFICO: LIVROS POR CATEGORIA
======================================================================

Programação          | ████████████████████████████████████████████ 12
Ficção               | ████████████████████████████████ 8
História             | ████████████████ 4

======================================================================
Total de livros: 24
Total de categorias: 3
======================================================================
```

## 🎯 Recursos Especiais

### Controle Inteligente de Estoque
- ✅ Redução automática ao realizar venda
- ✅ Restauração automática ao cancelar venda
- ✅ Validação de estoque insuficiente
- ✅ Mensagens de feedback claras

### Validações Robustas
- ✅ Suporte a IDs alfanuméricos (ex: `LIV-001`, `520a`)
- ✅ Validação de entrada de dados
- ✅ Tratamento de erros de conexão
- ✅ Confirmação antes de deletar

### Interface Intuitiva
- ✅ Menus organizados e claros
- ✅ Tabelas formatadas para visualização
- ✅ Ícones visuais (✓ sucesso / ✗ erro)
- ✅ Navegação fácil entre menus

## 📊 Estrutura dos Dados

### Livro
```json
{
  "id": "LIV-001",
  "titulo": "Clean Code",
  "autor": "Robert C. Martin",
  "preco": 89.90,
  "estoque": 15,
  "categoria": "Programação"
}
```

### Venda
```json
{
  "id": "VND-001",
  "livro_id": "LIV-001",
  "titulo_livro": "Clean Code",
  "quantidade": 2,
  "preco_unitario": 89.90,
  "total": 179.80,
  "cliente": "João Silva",
  "data": "2025-11-24 14:30:00"
}
```

## ⚠️ Solução de Problemas

### Erro: Módulo 'requests' não encontrado
```bash
pip install requests
```

### Erro: JSON Server não encontrado
```bash
npm install -g json-server
```

### Erro: Conexão recusada
Verifique se o JSON Server está rodando:
```bash
json-server --watch db.json --port 3000
```

### Porta 3000 já em uso
Use outra porta:
```bash
json-server --watch db.json --port 3001
```
E atualize a variável `BASE_URL` no código.

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📝 Requisitos do Projeto

Este projeto foi desenvolvido para atender aos seguintes requisitos acadêmicos:

✅ **Requisito 1**: CRUD completo na tabela principal (Livros)  
✅ **Requisito 2**: CRUD com transação na tabela relacionada (Vendas com controle de estoque)  
✅ **Requisito 3**: Pesquisa avançada com 2+ atributos (autor, categoria, preço)  
✅ **Requisito 4**: Gráfico da tabela principal com agrupamento (Livros por categoria)  
✅ **Requisito 5**: Gráfico da tabela relacionada (Vendas por livro)


⭐ Se este projeto foi útil para você, considere dar uma estrela!

**Desenvolvido com ❤️ usando Python + JSON Server**
