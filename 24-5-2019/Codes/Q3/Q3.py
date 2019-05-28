import csv

count = True
with open('C:/Users/akhil/Documents/PS-1/24-5-2019/categories.csv','rt') as categories:
    categories_data = csv.reader(categories)
    for categories_row in categories_data:
        if count == False:
            print("\nThe category is:",categories_row[1])
        with open('C:/Users/akhil/Documents/PS-1/24-5-2019/products.csv','rt') as products:
            products_data = csv.reader(products)
            for products_row in products_data:
                if categories_row[0] == products_row[3]:
                    if count == False:
                        print("\t",products_row[1])
                    else:
                        count = False



