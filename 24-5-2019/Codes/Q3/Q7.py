import csv

seafood = []
beverage = []

with open('C:/Users/akhil/Documents/PS-1/24-5-2019/categories.csv','rt') as categories:
    categories_data = csv.reader(categories)
    for categories_row in categories_data:
        if categories_row[1] == 'Beverages' or categories_row[1] == 'Seafood':
            #category ID
            with open('C:/Users/akhil/Documents/PS-1/24-5-2019/products.csv','rt') as products:
                products_data =  csv.reader(products)
                for products_rows in products_data:
                    #Product ID
                    if categories_row[0] == products_rows[3]:
                        with open('C:/Users/akhil/Documents/PS-1/24-5-2019/order-details.csv','rt') as ordetails:
                            ordetails_data = csv.reader(ordetails)
                            for ordetails_row in ordetails_data:
                                #Order ID
                                if ordetails_row[1] == products_rows[0]:
                                    with open('C:/Users/akhil/Documents/PS-1/24-5-2019/orders.csv','rt') as orders:
                                        orders_data = csv.reader(orders)
                                        for orders_row in orders_data:
                                            #Customer ID
                                            if orders_row[0] == ordetails_row[0]:
                                                with open('C:/Users/akhil/Documents/PS-1/24-5-2019/customers.csv','rt') as customers:
                                                    customers_data = csv.reader(customers)
                                                    for customer_row in customers_data:
                                                        if customer_row[0] == orders_row[1]:
                                                            if categories_row[1] == 'Beverages':
                                                                beverage.append(customer_row[0])
                                                            else:
                                                                seafood.append(customer_row[0])

x = set(seafood)
y = set(beverage)
y &= x

for ide in y:
    with open('C:/Users/akhil/Documents/PS-1/24-5-2019/customers.csv','rt') as customers:
        customers_data = csv.reader(customers)
        for customer_row in customers_data:
            if ide == customer_row[0]:
                print(customer_row)

print(len(y))