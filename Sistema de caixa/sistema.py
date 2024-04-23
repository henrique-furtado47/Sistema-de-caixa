# Sistema de caixa básico
#  Autor: Henrique Furtado

#  Criação das listas vazias 
produtos=[]
precos=[]
quantidades=[]
id=[]
total_estoque=0
total=0
# Início do loop principal
while True:
    print("\n Menu: ")
    print("1 - Acessar estoque")
    print("2 - Acessar carrinho")
    print("3 - Compra rápida (Utilize para teste ou realizar compra sem adicionar o produto ao estoque)")
    print("0 - Sair ")
    opcao=int(input("Digite a opção: "))
    # Opção 1: Acessar estoque
    if opcao==1:
        while True:
            print("\n Estoque: ")
            print("1 - Adicionar produto")
            print("2 - Remover produto")
            print("3 - Visualizar estoque")
            print("4 - Atualizar produto")
            print("5 - Limpar estoque")
            print("0 - Sair")
            opcao1=int(input("Digite a opção: "))
            # Opção 1 no estoque: Adicionar produto
            if opcao1==1:
                 while True:
                    produto=input("\n Digite o nome do produto (Digite '0' para sair): ")
                    #  Se o produto for repetido ou o id for repetido, o programa não aceita
                    if produto in produtos:
                        print("Produto já existente")
                        continue
                    if produto=="0":
                        break
                    # Definição do preço, quantidade e id do produto
                    else:
                        preco=float(input("Digite o preço do produto: "))
                        quantidade=int(input("Digite a quantidade de produtos: "))
                        ids= int(input("Digite o id do produto (maior que 0, não repetido): "))
                        if ids in id:
                            print("ID já existente")
                            continue
                        elif ids<=0:
                            print("ID inválido")
                            continue
                        else:
                            # Adição do produto, preço, quantidade e id nas listas
                            produtos.append(produto)
                            precos.append(preco)
                            quantidades.append(quantidade)
                            id.append(ids)
            # Opção 2 no estoque: Remover produto
            elif opcao1==2:
                while True:
                    remover=int(input("\nDigite o id do produto que deseja remover (Digite '0' para sair): "))
                    if remover==0:
                        break
                    # Se o produto não estiver no estoque, o programa não aceita
                    if remover not in id:
                        print("Produto não encontrado")
                        continue
                    else:
                        # Remoção do produto, preço, quantidade e id
                        index = id.index(remover)
                        produtos.pop(index)
                        precos.pop(index)
                        quantidades.pop(index)
                        id.pop(index)
                        print("Produto removido com sucesso")
            # Opção 3 no estoque: Visualizar estoque                
            elif opcao1==3:
                        #  Definindo que o total do estoque é 0 para que ele seja atualizado a cada vez que a opção 2 for escolhida
                        total_estoque=0
                        # Mostrando os produtos, preços, quantidades e id
                        print("\n Produtos | Preços | Quantidade | ID ")
                        for i in range(len(produtos)):
                            print(f"{produtos[i]} | {precos[i]} | {quantidades[i]} | {id[i]} ")
                            total_estoque+=precos[i]*quantidades[i]
                        print("\n Total: ", total_estoque)
            # Opção 4 no estoque: Atualizar produto           
            elif opcao1==4:
                    while True:
                        produto=int(input("\n Digite o ID do produto (Digite '0' para sair): "))
                        if produto==0:
                            break
                        # Se o produto não estiver no estoque, o programa não aceita
                        if produto not in id:
                            print("Produto não encontrado")
                            continue
                        else:
                            # Atualização do preço e quantidade do produto
                            preco=float(input("Digite o novo preço do produto: "))
                            quantidade=int(input("Digite a nova quantidade de produtos: "))
                            index = id.index(produto)
                            precos[index] = preco
                            quantidades[index] = quantidade
                            print("Dados do produto atualizados com sucesso!")
            #Opção 5 no estoque: Limpar estoque
            elif opcao1==5:
                # Limpando as listas
                produtos.clear()
                precos.clear()
                quantidades.clear()
                id.clear()
                total_estoque=0
                print("\n Estoque limpo")
            # Opção 0 no estoque: Sair                
            elif opcao1==0:
                    break
            # Opção inválida
            else:
                    print("\n Opção inválida")
    # Opção 2: Acessar carrinho            
    elif opcao==2:
        #  Definindo a lista de compras vazia
        compras=[]
        # Início do loop de compra
        while True:
            print("\n Carrinho: ")
            print("1 - Adicionar produto")
            print("2 - Remover produto")
            print("3 - Visualizar carrinho")
            print("4 - Finalizar compra")
            print("5 - Limpar carrinho")
            print("0 - Sair")
            opcao2=int(input("Digite a opção: "))
            # Opção 1 no carrinho: Adicionar produto
            if opcao2==1:
                while True:
                #  Definindo o id do produto que será comprado
                    compra=int(input("\nDigite o id do produto (Digite '0' para terminar de adicionar): "))
                    if compra==0:
                        break
                    # Se o produto não estiver no estoque, o programa não aceita
                    if compra not in id:
                        print("Produto não encontrado\n")
                        continue
                    else:
                        # Definindo a quantidade do produto que será comprado
                        quantidade=int(input("Digite a quantidade de produtos: "))
                        # Se a quantidade for maior que a quantidade disponível no estoque, o programa não aceita
                        if quantidade>quantidades[id.index(compra)]:
                            print("\nQuantidade insuficiente")
                            continue
                        else:
                            # Adicionando o produto e a quantidade comprada na lista de compras
                            compras.append([compra, quantidade])
                            # Calculando o total da compra
                            total+=quantidade*precos[id.index(compra)]
            # Opção 2 no carrinho: Remover produto
            elif opcao2==2:
                while True:
                    # Definindo o id do produto que será removido
                    remover=int(input("\nDigite o id do produto que deseja remover (Digite '0' para sair): "))
                    if remover==0:
                        break
                    # Se o produto não estiver no carrinho, o programa não aceita
                    if remover not in [compra[0] for compra in compras]:
                        print("Produto não encontrado no carrinho\n")
                        continue
                    else:
                        # Removendo o produto e a quantidade comprada da lista de compras
                        for compra in compras:
                            if compra[0] == remover:
                                quantidade = compra[1]
                                compras.remove(compra)
                                break
                        # Atualizando o total da compra
                        total -= quantidade * precos[id.index(remover)]
                        print("\n Produto removido com sucesso\n")
            elif opcao2==3:
                # Mostrando os produtos no carrinho
                print("\nNome | Quantidade | ID | Preço")
                for compra in compras:
                     print(f"{produtos[id.index(compra[0])]} | {compra[1]} | {compra[0]} | {precos[id.index(compra[0])]}")
                print("Total: ", total)
            #Opção 4 no carrinho: Finalizar compra
            elif opcao2==4:
                # Se o carrinho estiver vazio, o programa não aceita
                if len(compras)==0:
                    print("\n Carrinho vazio")
                    continue
                # Diminuindo a quantidade comprada do total do estoque
                for compra in compras:
                    quantidades[id.index(compra[0])]-=compra[1]    
                # Mostrando os produtos comprados           
                print("\nProdutos comprados: ")
                print("Nome | Quantidade | ID | Preço")
                for compra in compras:
                    print(f"{produtos[id.index(compra[0])]} | {compra[1]} | {compra[0]} | {precos[id.index(compra[0])]}")
                print("Total: ", total)
                # Definindo o valor pago e o troco
                pago=float(input("\nDigite o valor pago: "))
                troco=pago-total
                # Se o valor pago for menor que o total, o programa não aceita
                if troco < 0:
                        print("\nValor insuficiente")
                        while troco<0:
                            pago1=float(input("\nDigite o valor pago: "))
                            troco=pago1-total
                            if troco<0:
                                print("Valor insuficiente")
                            else:
                                break
                        continue
                    # Mostrando o troco
                print("Troco: ", troco)
                total=0
                # Limpando a lista de compras
                compras=[]
            # Opção 5 no carrinho: Limpar carrinho
            elif opcao2==5:
                # Limpando a lista de compras
                compras=[]
                total=0
                print("\n Carrinho limpo")
            # Opção 0 no carrinho: Sair
            elif opcao2==0:
                break  
            # Opção inválida
            else:
                print("\nOpção inválida")
    # Opção 3: Compra rápida
    elif opcao==3:
         # Definindo a lista de compra rápida vazia
         comprarapida=[]
         # Início do loop de compra rápida
         while True:
              produtorapido=input("\nDigite o nome do produto (Digite '0' para sair): ")
              if produtorapido=="0":
                  break
              # Definindo o preço do produto que será comprado
              precorapido=float(input("Digite o preço do produto: "))
              # Definindo a quantidade de produtos que será comprada
              quantidaderapida=int(input("Digite a quantidade de produtos: "))
              # Adicionando o produto, preço e quantidade na lista de compra rápida
              comprarapida.append([produtorapido, precorapido, quantidaderapida])
              # Calculando o total da compra
              total+=precorapido*quantidaderapida
              # Mostrando os produtos comprados
              print("\nProdutos comprados: ")
              print("Nome | Quantidade | Preço")
              for compra in comprarapida:
                  print(f"{compra[0]} | {compra[2]} | {compra[1]}")
              print("Total: ", total)
         # Definindo o valor pago e o troco
         pago=float(input("\n Digite o valor pago: "))
         troco=pago-total
         # Se o valor pago for menor que o total, o programa não aceita
         if troco < 0:
            print("\nValor insuficiente")
            while troco<0:
                pago1=float(input("\nDigite o valor pago: "))
                troco=pago1-total
                if troco<0:
                    print("Valor insuficiente")
                else:
                    break
            continue
         # Mostrando o troco
         print("Troco: ", troco)
         total=0
         # Limpando a lista de compra rápida
         comprarapida=[]
    # Opção 0: Sair
    elif opcao==0:
        break
    # Opção inválida
    else:
        print("\nOpção inválida")
# Fim do programa
print("Fim do programa")
