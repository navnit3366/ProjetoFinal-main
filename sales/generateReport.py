def generateReportsSales(salesList):
    print("Relatório de vendas")
    print("")
    
    for sale in salesList:
        print("=====================================")
        print("Venda: ")
        print("Venda ID: " + str(sale["id"]))
        print("Produto ID: " + str(sale["product"]))
        print("Quantidade comprada: " + str(sale["quant"]))
        print("Total: R$ " + str(sale["total"]))
        print("=====================================")