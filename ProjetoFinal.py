from procedures.menu import menu
from products.create import createProduct
from products.update import updateProduct
from reports.generate import generateReportMenu;
from sales.create import createSale;
from validators.validateMenuOption import validateMenuOption;

optionSelected = 0
productList = []
saleList = []
isOptionValidated = False

# Enquanto a opção selecionada for diferente de sair(5)
while optionSelected != 5:

    # Função que printa o menu
    menu()

    # Enquanto a opção for inválida
    while isOptionValidated == False:
        optionSelected = int(input('Opção desejada: '))
        isOptionValidated = validateMenuOption(optionSelected)

    print("")
    print("")
    print("")
    
    # Cadastro
    if (optionSelected == 1):    
        productList = createProduct(productList)
    
    # Atualização
    if (optionSelected == 2):
        productList = updateProduct(productList)

    # Realizar Venda
    if (optionSelected == 3):
        response = createSale(saleList, productList)
        saleList = response["saleList"]
        productList = response["productList"]

    # Relatório
    if (optionSelected == 4):
        generateReportMenu(productList, saleList)
         
    # sair
    if (optionSelected == 5):
        exit(); 
    
    optionSelected = 0
    isOptionValidated = False


