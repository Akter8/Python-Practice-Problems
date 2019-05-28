import csv
lis = []

with open('products.csv','rt')as products:
    products_data = csv.reader(products)
    for products_row in products_data:
        if products_row[1] == 'Tofu' or products_row[1] == 'Konbu':
            with open('order-details.csv','rt')as ordetails:
                ordetails_data = csv.reader(ordetails)
                for ordetails_row in ordetails_data:
                    if ordetails_row[1] == products_row[0]:
                        with open('orders.csv','rt')as order:
                            order_data = csv.reader(order)
                            for order_row in order_data:
                                if order_row[0] == ordetails_row[0]:
                                    with open('customers.csv','rt') as customers:
                                        customers_data = csv.reader(customers)
                                        for customers_row in customers_data:
                                            if order_row[1] == customers_row[0]:
                                                lis.append(customers_row[1])
                                        

liss = sorted(set(lis))
print(liss)
print("The total count is",len(liss))