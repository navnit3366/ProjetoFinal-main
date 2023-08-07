def createSale(saleList, productList):
    tempSaleList = list(saleList)
    tempProductList = list(productList)

    sale = {
        "id" : len(saleList), # Campo unico, por ser o tamanho da lista consequentemente já é o index
        "product": -1, # Id do produto
        "quant": 0,
        "total": 0
    }

    print("Selecione um produto da lista: ")
    print("")
    
    for product in tempProductList:
        print("ID: "+str(product["id"])+" Produto: "+product["name"])
        print("")

    optionSelected = -1 
    idExist = False

    while idExist == False:
        optionSelected = int(input('ID do produto: '))
        
        for product in tempProductList:
            if (optionSelected == product["id"]):
                idExist = True

    sale["product"] = optionSelected
    
    tempQuant = 0;
    
    while tempQuant <= 0 or tempQuant > tempProductList[optionSelected]["quant"]:
        tempQuant = int(input('Quantidade: '))

        if (tempQuant > tempProductList[optionSelected]["quant"]):
            print("Quantidade indisponível em estoque")
        
    sale["quant"] = tempQuant
    sale["total"] = tempQuant * tempProductList[optionSelected]["price"]

    tempProductList[optionSelected]["quant"] = tempProductList[optionSelected]["quant"] - tempQuant

    tempSaleList.append(sale)
    
    return {
        "saleList": tempSaleList,
        "productList": tempProductList
    }