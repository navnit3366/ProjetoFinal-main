def createProduct(productList):
    tempProductList = list(productList)

    product = {
        "id" : len(productList), # Campo unico, por ser o tamanho da lista consequentemente já é o index
        "type": "",
        "name": "",
        "price": 0,
        "quant": 0
    }

    while product["name"] == "":
        product["name"] = input('Nome do produto: ')

        if (product["name"] == ""):
            print("Nome inválido")
    
    while product["type"] == "":
        product["type"] = input('Tipo de produto (Pão, Bolo, Salgado, Bebida, etc.): ')

        if (product["type"] == ""):
            print("Tipo inválido")

    while product["price"] <= 0 or product["price"] == "":
        product["price"] = int(input('Preço de venda: '))

        if (product["price"] <= 0):
            print("Preço inválido")
    
    while product["quant"] <= 0 or product["quant"] == "":
        product["quant"] = int(input('Estoque inicial: '))

        if (product["quant"] <= 0):
            print("Quantidade inválida")
    

    tempProductList.append(product)
    print("Cadastro realizado com sucesso!!!")

    return tempProductList 
