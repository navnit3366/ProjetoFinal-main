def productsReport(productList):
    print("Relatório de Produtos")
    print("")
    for product in productList:
        print("=====================================")
        print("Produto: ")
        print("ID: " + str(product["id"]))
        print("Nome: " + product["name"])
        print("Tipo: " + product["type"])
        print("Preço: " + str(product["price"]))
        print("Quantidade: " + str(product["quant"]))
        print("=====================================")