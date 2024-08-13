import view
from model.produto import Produto



produtos = []


def cadastrar():
    produto = view.input_nome_produto()

    quantidade = view.input_quantidade()

    produto = Produto(produto, quantidade)
    
    produtos.append(produto)



def listar():

    view.exibir_lista_produtos(produtos)



def incluir_estoque():
    
    if not produtos:
        view.lista_vazia()

    else:    
        nome_produto = view.nome_produto()

        for produto in produtos: 
            
            if nome_produto == produto.get_nome():

                nova_quantidade = view.nova_quantidade()

                quantidade = produto.get_quantidade()
              
                quantidade += nova_quantidade
                produto.atribuir_quantidade(quantidade)
                return

                
            
        view.produto_nao_encontrado()