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
    print("2 - Iniciar compra")
    print("3 - Sair ")
    opcao=int(input("Digite a opção: "))
    # Opção 1: Acessar estoque
    if opcao==1:
        while True:
            print("\n Estoque: ")
            print("1 - Adicionar produto")
            print("2 - Visualizar estoque")
            print("3 - Atualizar produto")
            print("4 - Sair")
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
            # Opção 2 no estoque: Visualizar estoque                
            elif opcao1==2:
                        #  Definindo que o total do estoque é 0 para que ele seja atualizado a cada vez que a opção 2 for escolhida
                        total_estoque=0
                        # Mostrando os produtos, preços, quantidades e id
                        print("\n Produtos | Preços | Quantidade | ID ")
                        for i in range(len(produtos)):
                            print(f"{produtos[i]} | {precos[i]} | {quantidades[i]} | {id[i]} ")
                            total_estoque+=precos[i]*quantidades[i]
                        print("\n Total: ", total_estoque)
            # Opção 3 no estoque: Atualizar produto           
            elif opcao1==3:
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
            # Opção 4 no estoque: Sair                
            elif opcao1==4:
                    break
            # Opção inválida
            else:
                    print("\n Opção inválida")
    # Opção 2: Iniciar compra                
    elif opcao==2:
        #  Definindo a lista de compras vazia
        compras=[]
        # Início do loop de compra
        while True:
            #  Definindo o id do produto que será comprado
            compra=int(input("Digite o id do produto (Digite '0' para finalizar a compra): "))
            if compra==0:
                break
            # Se o produto não estiver no estoque, o programa não aceita
            if compra not in id:
                print("Produto não encontrado\n")
                continue
            else:
                # Definindo a quantidade do produto que será comprado
                quantidade=int(input("\n Digite a quantidade de produtos: "))
                # Se a quantidade for maior que a quantidade disponível no estoque, o programa não aceita
                if quantidade>quantidades[id.index(compra)]:
                    print("\n Quantidade insuficiente")
                    continue
                else:
                    # Subtraindo a quantidade comprada da quantidade disponível no estoque
                    quantidades[id.index(compra)]-=quantidade
                    # Adicionando o produto e a quantidade comprada na lista de compras
                    compras.append([compra, quantidade])
                    # Calculando o total da compra
                    total+=quantidade*precos[id.index(compra)]
                    # Mostrando os produtos no carrinho
                    print("Nome | Quantidade | ID | Preço")
                    for compra in compras:
                      print(f"{produtos[id.index(compra[0])]} | {compra[1]} | {compra[0]} | {precos[id.index(compra[0])]}")
                    print("Total: ", total)
        # Mostrando os produtos comprados           
        print("\n Produtos comprados: ")
        print("Nome | Quantidade | ID | Preço")
        for compra in compras:
            print(f"{produtos[id.index(compra[0])]} | {compra[1]} | {compra[0]} | {precos[id.index(compra[0])]}")
        print("Total: ", total)
         # Definindo o valor pago e o troco
        pago=float(input("\n Digite o valor pago: "))
        troco=pago-total
         # Se o valor pago for menor que o total, o programa não aceita
        if troco < 0:
                print("\n Valor insuficiente")
                while troco<0:
                    pago1=float(input("\n Digite o valor pago: "))
                    troco=pago1-total
                    if troco<0:
                        print("Valor insuficiente")
                    else:
                        break
                continue
            # Mostrando o troco
        print("Troco: ", troco)
        total=0
    # Opção 3: Sair
    elif opcao==3:
        break
    # Opção inválida
    else:
        print("\n Opção inválida")
# Fim do programa
print("Fim do programa")
