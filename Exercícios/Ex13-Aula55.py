import os
print("""
    ------ Lista de Compras ------
    [ 1 ] -> Inserir item
    [ 2 ] -> Remover item
    [ 3 ] -> Listar
""")

escolha_convertido_para_int = 0
checando_novo_produto_is_numero = 0
remover_item_da_lista = 0
remover_item_da_lista_int = 0

escolha_manter_item = ''

escolha_valida = None
indice_para_remover_item_valido = None

lista_de_compras = []


while True:
    print("[ 1 ] -> Inserir item [ 2 ] -> Remover item [ 3 ] -> Listar")
    escolha = input("Informe sua escolha: ")
    tem_numero_in_novo_item = None
    sucesso_remover_item = None

    if len(escolha) > 1:
        os.system("cls")
        print("Informe apenas um valor")
        continue
    
    try:
        escolha_convertido_para_int = int(escolha)
        escolha_valida = True
    except:
        escolha_valida = None
    
    if escolha_valida is None:
        os.system("cls")
        print("Informe um valor válido!")
        continue

    if escolha_convertido_para_int == 1:
        novo_item = input("Informe o item a ser inserido: ").capitalize()   
        
        for numero in novo_item:
            try:
                checando_novo_produto_is_numero = numero.isdigit()
                if checando_novo_produto_is_numero:
                    tem_numero_in_novo_item = True
            except:
                tem_numero_in_novo_item = None

        if tem_numero_in_novo_item is True:
            os.system("cls")
            print("Informe um produto válido!!")
            continue
        elif novo_item in lista_de_compras:
            print("Este item já tem na lista de compras!")
            escolha_manter_item = input("Você quer manter o item (s/n)?").lower()
            if escolha_manter_item.startswith('s'):
                lista_de_compras.append(novo_item)
            else:
                continue
        else:
            lista_de_compras.append(novo_item)
            os.system("cls")
    
    elif escolha_convertido_para_int == 2:
        os.system("cls")
        print("O primeiro item da lista começa em 0!!")
        remover_item_da_lista = input("Informe qual indice da lista você quer remover: ")

        try:
            remover_item_da_lista_int = int(remover_item_da_lista)
            indice_para_remover_item_valido = True
        except:
            indice_para_remover_item_valido = None

        if indice_para_remover_item_valido is None:
            os.system("cls")
            print("Informe o NÚMERO do índice!")
            continue
        
        if indice_para_remover_item_valido is True:
            if remover_item_da_lista_int > len(lista_de_compras):
                os.system("cls")
                print("Não é possível remover este índice!")
                continue
            elif len(lista_de_compras) == 0:
                os.system("cls")
                print("Lista está vazia! Não é possível remover itens")
                continue

            try:
                lista_de_compras.pop(remover_item_da_lista_int)
                sucesso_remover_item = True
            except:
                sucesso_remover_item = None

            if sucesso_remover_item == True:
                continue
            else:
                os.system("cls")
                print("O índice informado é inválido!")
                continue
    
    elif escolha_convertido_para_int == 3:
        if len(lista_de_compras) == 0:
            os.system("cls")
            print("A ATUAL LISTA ESTÁ VAZIA!")
        else:
            os.system("cls")
            print("ITENS ATUAL")
            for indice, itens in enumerate(lista_de_compras):
                print(indice, itens)
    else:
        os.system("cls")
        print("OPÇÃO INVÁLIDA!")
        print("PROGRAMA ENCERRADO!")
        if len(lista_de_compras) == 0:
            print("A LISTA ENCERROU VAZIA!")
        else:
            print("LISTA ATUAL:")
            for indice, itens in enumerate(lista_de_compras):
                print(indice, itens)
        break