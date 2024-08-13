from model.cliente import Cliente
from model.carrinho import Carrinho
import controller.produto_controller as pc

import view


clientes = [Cliente('thiago')]


def cadastrar():

    # usuário informa o nome pelo teclado
    nome = view.input_nome_cliente()

    # criar a instância do cliente
    novo_cliente = Cliente(nome)

    # salvar na lista clientes
    clientes.append(novo_cliente)



def listar():

    view.exibir_lista_clientes(clientes)



def editar():

    indice_cliente = _selecionar_cliente()
    
    if indice_cliente is not None:

        # recebe o novo nome
        novo_nome = view.input_novo_nome()

        # atualizar
        cliente = clientes[indice_cliente]

        cliente.nome = novo_nome




def excluir():

    # lógica para excluir cliente (por nome)                
    indice_cliente = _selecionar_cliente()

    if indice_cliente is not None:

        clientes.pop(indice_cliente) # remove da lista pelo indice



# retorna o indice do cliente
def _selecionar_cliente():

    # recebe o nome do cliente
    nome = view.input_nome_cliente()

    # econtrar o cliente na lista
    for cliente in clientes:
        
        if cliente.nome == nome:

            view.mensagem_cliente_encontrado()

            return clientes.index(cliente)
        
    view.mensagem_cliente_nao_encontrado()
    return None



carrinho = []


def adicionar_ao_carrinho():

    produto_escolhido = view.input_nome_produto()

    for produto in pc.produtos:

        if produto_escolhido == produto.get_nome():

            quantidade_produto = view.input_quantidade()

            produto_ = {
                'nome': produto_escolhido,
                'quantidade': quantidade_produto
            }

            carrinho.append(produto_)



def ver_carrinho():
    view.carrinho_titulo()
    if not carrinho:
        view.lista_vazia()

    else:
        for i in carrinho:

            view.nome_quantidade_carrinho(i)



def excluir_produto():
    
    produto_excluir = view.input_nome_produto()

    for produto in carrinho:

        if produto_excluir == produto['nome']:
            carrinho.remove(produto)
            view.mensagem_produto_excluido(produto_excluir)
        
        else:
            view.produto_nao_encontrado()
