from pathlib import Path

# Conteúdo do README em Markdown
readme_content = """# 📦 Sistema de Controle de Estoque e Vendas  

Um sistema simples em **Python** para gerenciamento de estoque e vendas em uma loja de eletrônicos.  

Projeto desenvolvido como **Estudo de Caso** para a disciplina *Computational Logic Using Python* da **UNIFECAF**.  

---

## 👩‍💻 Autora
- **Anna Caroline Ribeiro**  
- GitHub: [acarolner](https://github.com/acarolner)

---

## 🚀 Funcionalidades  

- **Produtos**  
  - Adicionar novo produto  
  - Atualizar produto existente  
  - Excluir produto  
  - Listar estoque atual  

- **Vendas**  
  - Registrar venda (com baixa automática no estoque)  
  - Listar vendas realizadas  

---

## 🛠️ Como funciona  

- Estruturas de dados utilizadas:  
  - `estoque` → lista de dicionários para os produtos.  
  - `vendas` → lista de dicionários para as vendas.  

- Não possui persistência em banco de dados:  
  - Ao encerrar o programa, os dados são perdidos.  

---

## 📋 Menu do Sistema  

```text
1 - Adicionar Produto
2 - Atualizar Produto
3 - Excluir Produto
4 - Visualizar Estoque
5 - Registrar Venda
6 - Visualizar Vendas
0 - Sair do Sistema
