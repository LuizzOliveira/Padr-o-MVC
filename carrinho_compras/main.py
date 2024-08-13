import controller.cliente_controller as cliente_controller
import controller.produto_controller as produto_controller
import view



def menu_carrinho():
    op_carrinho = -1

    while True:

        view.exibir_menu_carrinho()

        op_carrinho = view.receber_opcao()


        match op_carrinho:

            case 1:

                cliente_controller.adicionar_ao_carrinho()

            case 2:

                cliente_controller.ver_carrinho()

            case 3:

                cliente_controller.excluir_produto()

            case 0:

                break
         



def menu_cliente():

    op_cliente = -1

    while True:

        view.exibir_menu_cliente()

        op_cliente = view.receber_opcao()

    
        match op_cliente:
            case 1:
                cliente_controller.cadastrar()

            case 2:
                cliente_controller.listar()

            case 3:
                cliente_controller.editar()

            case 4:
                cliente_controller.excluir()

            case 5:
                menu_carrinho()
            # case 5:
            #     cliente_controller.ver_carrinho()

            # case 6:
            #     cliente_controller.adicionar_ao_carrinho()

            # case 7:
            #     cliente_controller.excluir_produto()

            case 0:
                break
         



def menu_produto():
     
    op_produto = -1

    while True:

        view.exibir_menu_produto()

        op_produto = view.receber_opcao()

        match op_produto:

            case 1:
                produto_controller.cadastrar()

            case 2:
                produto_controller.listar()

            case 3:
                produto_controller.incluir_estoque()

            case 0:
                break




def menu_principal():
    op = -1

    while True:

        view.exibir_menu_principal()

        op = view.receber_opcao()

    
        match op:

            case 1:
                menu_cliente()

            case 2:
                menu_produto()
        
            case 0:
                view.mensagem_encerrar_programa()
                break

menu_principal()