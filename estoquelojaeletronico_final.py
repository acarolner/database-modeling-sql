# --------------------------------------------------------------------------- 
#ESTUDO DE CASO PARA A DISCIPLINA Computational Logic Using Python DA UNIFECAF 
#Sistema de Controle de Estoque com Python: Soluções para Gerenciamento em uma Loja de Eletrônicos 

#Aluna: Anna Caroline Ribeiro https://github.com/acarolner
# ---------------------------------------------------------------------------

#O que faz:
#- Produtos: adicionar, atualizar, excluir e listar.
#- Vendas: registrar (com baixa automática no estoque) e visualizar.

# Como funciona:
#- Usa duas estruturas em memória (listas de dicionários): `estoque` e `vendas`.
#- Não há persistência: ao encerrar o programa, os dados são perdidos.
# ---------------------------------------------------------------------------

from time import sleep

MENU = """
1 - Adicionar Produto
2 - Atualizar Produto
3 - Excluir Produto
4 - Visualizar Estoque
5 - Registrar Venda
6 - Visualizar Vendas
0 - Sair do Sistema
"""

# Estruturas em memória simulando um "banco de dados" simples
estoque = [] # cada item: {'nome_produto': str, 'preco': float, 'quantidade': int}
vendas = [] # cada item: {'cliente': str, 'produto': str, 'preco': float, 'quantidade': int, 'total': float}

# ---------------------------------------------------------------------------
# Utilidades de interface e validação
# ---------------------------------------------------------------------------
def titulo(txt):
print('--' * 26)
print(f"|{txt:^50}|")
print('--' * 26)

def aguardar_enter():
# Volta ao menu apenas quando o usuário apertar Enter "em branco"
while True:
resposta = input('Pressione Enter para voltar ao menu. ').strip()
if resposta == '':
break
else:
mostrar_erro('Não digite nada, apenas pressione Enter.')

def mostrar_erro(mensagem):
# Padrão de exibição de mensagens de erro
print(f'\nERRO: {mensagem}\n')

def confirmar_acao(mensagem):
# Confirmações rápidas (S/N) para evitar ações acidentais
while True:
resposta = input(f'{mensagem} [S/N] ').strip().upper()
if resposta in ['S', 'N']:
return resposta == 'S'
mostrar_erro('Escolha apenas [S] ou [N] para prosseguir.')

def pausa():
# Pequena pausa apenas para dar fluidez visual às mensagens
sleep(1)

# ---------------------------------------------------------------------------
# Encaminhamento do menu para as funções correspondentes
# ---------------------------------------------------------------------------
def operacao_selecionada(operacao):
if operacao == '1':
adicionar_produto()
elif operacao == '2':
atualizar_produto()
elif operacao == '3':
excluir_produto()
elif operacao == '4':
visualizar_estoque()
elif operacao == '5':
registrar_venda()
elif operacao == '6':
visualizar_vendas()
else:
mostrar_erro('Operação selecionada não é válida. \nTente novamente!')

# ---------------------------------------------------------------------------
# Cadastro de produtos
# ---------------------------------------------------------------------------
def adicionar_produto():
titulo('ADICIONAR NOVO PRODUTO')
while True:
nome = str(input('Nome do Produto: ')).strip().capitalize()

# Impede nomes vazios
if nome == '':
print('\n O nome não pode estar vazio!\n')
continue

# Bloqueia duplicidade pelo nome
for produto in estoque:
if produto['nome_produto'] == nome:
print('\nProduto já cadastrado no sistema! \nUtilize a opção ATUALIZAR PRODUTO.\n')
return
try:
preco = float(input('Preço do Produto: '))
quantidade = int(input('Quantidade em Estoque: '))

# Regras mínimas de validação
if preco <= 0 or quantidade <= 0:
mostrar_erro('Preço e quantidade devem ser maior que zero (0)!')
continue
except ValueError:
mostrar_erro('Digite valores numéricos válidos para preço e quantidade.')
continue

# Estrutura do novo item a ser guardado
novo_produto = {
'nome_produto': nome,
'preco': preco,
'quantidade': quantidade
}
estoque.append(novo_produto)
print(f'\nProduto: {nome} ADICIONADO com SUCESSO!\n')

if not confirmar_acao('Cadastrar outro produto?'):
pausa()
break

# ---------------------------------------------------------------------------
# Edição/atualização de dados do produto
# ---------------------------------------------------------------------------
def atualizar_produto():
titulo('ATUALIZAR PRODUTO')
while True:
nome = str(input('Nome do produto a ser atualizado: ')).strip().capitalize()
produto_encontrado = None

# Procura referência pelo nome informado
for produto in estoque:
if produto['nome_produto'] == nome:
produto_encontrado = produto
break
if not produto_encontrado:
print(f'\nProduto {nome} NÃO encontrado no estoque!\n')
break

try:
novo_preco = float(input('Novo Preço: '))
nova_quantidade = int(input('Nova Quantidade: '))
if novo_preco <= 0 or nova_quantidade <= 0:
mostrar_erro('Preço e quantidade devem ser maior que zero (0)!')
continue
else:
produto_encontrado['preco'] = novo_preco
produto_encontrado['quantidade'] = nova_quantidade
print(f'\nProduto: {nome} ATUALIZADO com SUCESSO!\n')
except ValueError:
mostrar_erro('Preço e Quantidade devem ser valores numéricos')
continue

if not confirmar_acao('Atualizar outro produto?'):
pausa()
break

# ---------------------------------------------------------------------------
# Remoção de produtos do catálogo
# ---------------------------------------------------------------------------
def excluir_produto():
titulo('EXCLUIR PRODUTO')
while True:
nome = str(input('Nome do produto a ser excluído: ')).strip().capitalize()

# Localiza e remove o item do estoque
for produto in estoque:
if produto['nome_produto'] == nome:
estoque.remove(produto)
print(f'\nProduto: {nome} REMOVIDO com SUCESSO!\n')
break
else:
print('\nProduto não encontrado!\n')
return
if not confirmar_acao('Excluir outro produto?'):
pausa()
break

# ---------------------------------------------------------------------------
# Listagem do estoque atual
# ---------------------------------------------------------------------------
def visualizar_estoque():
titulo('ESTOQUE')
if not estoque:
print('Estoque vazio!')
else:
for produto in estoque:
print(f"Produto: {produto['nome_produto']}")
print(f"Preço: {produto['preco']:.2f}")
print(f"Quantidade: {produto['quantidade']}")
print('--'*26)
pausa()
aguardar_enter()

# ---------------------------------------------------------------------------
# Emissão/registro de uma venda
# ---------------------------------------------------------------------------
def registrar_venda():
titulo('REGISTRAR VENDA')
while True:
nome_cliente = str(input('Nome do Cliente: ')).strip().capitalize()
nome_produto_venda = str(input('Produto: ')).strip().capitalize()
produto_encontrado = None

# Protege contra cliente sem nome
if nome_cliente == '':
mostrar_erro('O nome não pode estar vazio!')
continue

# Tenta localizar o produto ofertado
for produto in estoque:
if produto['nome_produto'] == nome_produto_venda:
produto_encontrado = produto
break
if not produto_encontrado:
print(f'Produto: {nome_produto_venda} NÃO encontrado no estoque!')
break
if produto_encontrado['quantidade'] == 0:
print(f'Produto {produto_encontrado["nome_produto"]} está sem estoque!')
break

print(f'Preço: R$ {produto_encontrado["preco"]:.2f}')
print(f'Estoque disponível: {produto_encontrado["quantidade"]}')

# Validação da quantidade comprada
while True:
try:
quantidade_compra = int(input('Quantidade de produtos comprados: '))
if quantidade_compra <= 0:
mostrar_erro('A quantidade deve ser maior que zero.')
elif quantidade_compra > produto_encontrado['quantidade']:
mostrar_erro('A quantidade solicitada excede o estoque disponével.')
else:
break
except ValueError:
mostrar_erro('Insira um número válido para a quantidade.')
continue
# Atualiza estoque e lança a venda
if confirmar_acao('Finalizar Compra?'):
produto_encontrado['quantidade'] -= quantidade_compra
total_compra = produto_encontrado['preco'] * quantidade_compra
nova_venda = {
'cliente': nome_cliente,
'produto': produto_encontrado['nome_produto'],
'preco': produto_encontrado['preco'],
'quantidade': quantidade_compra,
'total': total_compra
}
vendas.append(nova_venda)
print('\nCompra realizada com SUCESSO!\n')
else:
print('\nCompra cancelada!\n')

if not confirmar_acao('REGISTRAR outra venda?'):
pausa()
break

# ---------------------------------------------------------------------------
# Relatório simples de vendas já efetuadas
# ---------------------------------------------------------------------------
def visualizar_vendas():
titulo('VENDAS REALIZADAS')
if not vendas:
print('Nenhuma venda realizada!')
else:
for venda in vendas:
print(f'Cliente: {venda["cliente"]}')
print(f'Produto: {venda["produto"]}')
print(f'Preço: {venda["preco"]:.2f}')
print(f'Quantidade: {venda["quantidade"]}')
print(f'Total: {venda["total"]:.2f}')
print('--'*26)
pausa()
aguardar_enter()

# ---------------------------------------------------------------------------
# Laço principal do aplicativo (menu interativo)
# ---------------------------------------------------------------------------
def main():
while True:
titulo('CONTROLE DE ESTOQUE E VENDAS')
print(f"{'SERVIÇOS DISPONÍVEIS':^50}")
print(MENU)
operacao = input('Escolha um dos serviços: ')

if operacao in ['1', '2', '3', '4','5', '6', '0']:
if operacao == '0':
print('\nSaindo do sistema...\n')
break
else:
operacao_selecionada(operacao)
else:
mostrar_erro('Operação selecionada não é válida. \nTente novamente!')

main()
