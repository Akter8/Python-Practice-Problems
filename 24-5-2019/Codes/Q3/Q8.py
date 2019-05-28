import csv


check = False
with open('C:/Users/akhil/Documents/PS-1/24-5-2019/categories.csv','rt') as categories:
    categories_data = csv.reader(categories)
    for categories_row in categories_data:
        price = 0
        #Category ID
        if check == True:
            print("Category is",categories_row[1])
        with open('C:/Users/akhil/Documents/PS-1/24-5-2019/products.csv','rt') as products:
            products_data = csv.reader(products)
            for products_row in products_data:
                #Product ID
                if products_row[3] == categories_row[0]:
                    if check == True:
                        price += float(products_row[5])*float(products_row[7])

        if check == True:
            print('\tRs.',price)
        else:
            check = True
                    
                    

