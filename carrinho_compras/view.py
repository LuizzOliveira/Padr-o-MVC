
#Cliente
def exibir_cliente(cliente):
    print(f'Cliente (nome: {cliente.nome})')



def exibir_lista_clientes(clientes):
    print('-'*20, 'CLIENTES', '-'*20)

    for cliente in clientes:
        exibir_cliente(cliente)

    print()



def exibir_menu_cliente():
    print('\n','-'*20, f'MENU CLIENTE', '-'*20)
    print('[1] CADASTRAR')
    print('[2] LISTAR')
    print('[3] EDITAR')
    print('[4] EXCLUIR')
    print('[5] MENU CARRINHO')
    # print('[5] VER CARRINHO')
    # print('[6] ADICIONAR CARRINHO')
    # print('[7] REMOVER CARRINHO')
    print('[0] VOLTAR')
    print()

def exibir_menu_carrinho():
    print('\n','-'*20, f'MENU CARRINHO', '-'*20)
    print('[1] ADICIONAR CARRINHO')
    print('[2] VER CARRINHO')
    print('[3] REMOVER CARRINHO')
    print('[0] VOLTAR')


def exibir_menu_principal():
    print('\n','-'*20, f'MENU PRINCIPAL', '-'*20)
    print('[1] CLIENTE')
    print('[2] PRODUTO')
    print('[0] SAIR')
    print()



def receber_opcao():
    try:
        return int(input('Informe: '))
    except: 
        # Desafio: interromper o programa quando digitar CTRL+C
        print('Opção inválida!')



def input_nome_cliente():
    return input('Nome do cliente: ')

def input_novo_nome():
    return input('Informe o novo nome do cliente: ')



def mensagem_cliente_encontrado():
    print('Cliente encontrado!')



def mensagem_cliente_nao_encontrado():
    print('Cliente não encontrado!')



def mensagem_excluido_cliente(tipo):
    if tipo == 'sucesso':
        print('Cliente removido com sucesso!')
    elif tipo == 'erro':
        print('Cliente não encontrado!')



def mensagem_encerrar_programa():
    print('Finalizando Programa...')



#produto
def exibir_produto(produto):
    print(f'Nome: {produto.get_nome()} | Quantidade: {produto.get_quantidade()}')



def exibir_lista_produtos(produtos):
    print('-'*20, 'PRODUTOS', '-'*20)

    if not produtos:
        
        print('   (Lista Vazia)')
    
    else:
        for produto in produtos:
            exibir_produto(produto)

    print()






def lista_vazia():
    print('   (Lista Vazia)')



def exibir_menu_produto():
    print('\n','-'*20, f'MENU PRODUTO', '-'*20)
    print('[1] CADASTRAR')
    print('[2] LISTAR')
    print('[3] INCLUIR ESTOQUE')
    print('[0] VOLTAR')
    print()



def input_nome_produto():
    return input("Informe nome do produto: ")



def input_quantidade():

    return int(input("Informe quantidade: "))



def nome_produto():

    return input('Informe nome do produto: ')



def nova_quantidade():

    return int(input('Informe quantidade adicional: '))



def produto_nao_encontrado():

    print('Produto não encontrado!')



def carrinho_titulo():

    print('\n-------Carrinho--------\n')



def lista_vazia():

    print('     (Lista Vazia)\n')



def nome_quantidade_carrinho(i):

    print(f'nome: {i['nome']} | quantidade: {i['quantidade']}\n')



def mensagem_produto_excluido(produto_excluir):

    print(f'\nProduto {produto_excluir}, foi removido do carrinho!\n')



