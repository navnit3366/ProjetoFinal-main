from products.generateReport import productsReport
from sales.generateReport import generateReportsSales

def generateReportMenu(productList, saleList):
    print("Selecione uma opção: ")
    print("")
    print("1 - Relatório de produtos")
    print("2 - Relatório de vendas")
    print("")

    optionSelected = 0
    optionSelectedIsValid = False

    while optionSelectedIsValid == False:
        optionSelected = int(input('Opção desejada: '))

        if optionSelected == 1:
            productsReport(productList)
            optionSelectedIsValid = True
        else:
            generateReportsSales(saleList)
            
            optionSelectedIsValid = True
    
            
     