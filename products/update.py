def updateProduct(productList):
    tempProductList = list(productList)

    print("Selecione um produto da lista: ")
    print("")
    
    for product in productList:
        print("ID: "+str(product["id"])+" Produto: "+product["name"])
        print("")

    # int(optionSelected) in options

    optionSelected = -1
    idExist = False

    while idExist == False:
        optionSelected = int(input('ID do produto: '))
        
        for product in productList:
            if (optionSelected == product["id"]):
                idExist = True

    product = {
        "id" : optionSelected,
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
        product["quant"] = int(input('Estoque: '))

        if (product["quant"] <= 0):
            print("Quantidade inválida")
    

    opcaoSelecionada = input('Deseja alterar este produto? S/N: ').upper()
    
    if (opcaoSelecionada == "S"):
        tempProductList[optionSelected] = product
        print("Produto alterado com sucesso!!!")
        
    return tempProductList 

   



