#Sistema de caixa básico
# Autor: Henrique Furtado
produtos=[]
precos=[]
quantidades=[]
id=[]
total=0
while True:
    print("1 - Adicionar Produto")
    print("2 - Listar Produtos")
    print("3 - Calcular Total")
    print("4 - Sair")
    print("5 - Iniciar compra")
    opcao=int(input("Digite a opção: "))
    if opcao==1:
        while True:
            produto=input("Digite o nome do produto (Digite '0' para sair): ")
            if produto=="0":
                break
            else:
                preco=float(input("Digite o preço do produto: "))
                quantidade=int(input("Digite a quantidade de produtos: "))
                ids= int(input("Digite o id do produto: "))
                produtos.append(produto)
                precos.append(preco)
                quantidades.append(quantidade)
                id.append(ids)
    elif opcao==2:
         print("Produtos | Preços | Quantidade | ID \n")
         for i in range(len(produtos)):
            print(f"{produtos[i]} | {precos[i]} | {quantidades[i]} | {id[i]}")
    elif opcao==3:
        for i in range(len(produtos)):
            total+=precos[i]*quantidades[i]
        print("Total: ", total)
    elif opcao==4:
        break
    elif opcao==5:
        compras=[]
        while True:
            compra=int(input("Digite o id do produto (Digite '0' para finalizar a compra): "))
            if compra==0:
                break
            if compra not in id:
                print("Produto não encontrado")
                continue
            else:
                quantidade=int(input("Digite a quantidade de produtos: "))
                indice=id.index(compra)
                if quantidades[indice]<quantidade:
                    print("Quantidade indisponível")
                    continue
                quantidades[indice]-=quantidade
                compras.append((compra, quantidade))
                total+=precos[indice]*quantidade
        print("Produtos comprados: ")
        print("ID | Quantidade")
        for compra in compras:
            print(f"{compra[0]} | {compra[1]}")
        if total>0:
            print("Total: ", total)
            pago=float(input("Digite o valor pago: "))
            troco=pago-total
            if troco < 0:
                print("Valor insuficiente")
                while troco<0:
                    pago=float(input("Digite o valor pago: "))
                    troco=pago-total
                    if troco<0:
                        print("Valor insuficiente")
                    else:
                        break
                continue
            print("Troco: ", troco)
            total=0
    else:
        print("Opção inválida")
print("Fim do programa")
