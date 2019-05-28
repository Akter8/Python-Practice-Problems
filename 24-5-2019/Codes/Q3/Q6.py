import csv
x = 0
count = False
with open('C:/Users/akhil/Documents/PS-1/24-5-2019/orders.csv','rt') as orders:
    orders_data = csv.reader(orders)
    for orders_row in orders_data:
        with open('C:/Users/akhil/Documents/PS-1/24-5-2019/order-details.csv','rt') as ordetails:
            ordetails_data = csv.reader(ordetails)
            for ordetails_row in ordetails_data:
                if orders_row[0] == ordetails_row[0]:
                    with open('C:/Users/akhil/Documents/PS-1/24-5-2019/products.csv','rt') as products:
                        products_data = csv.reader(products)
                        for products_row in products_data:
                            if ordetails_row[1] == products_row[0]:
                                if count == True:
                                    print(str(orders_row[0]),end=' ')
                                    print(str(products_row[0]),end=' ')
                                    print(str(products_row[1]),end=' ')
                                    print(str(products_row[5]),end=' ')
                                    print(str(ordetails_row[3]),end=' ')
                                    print(str(ordetails_row[4]),end=' ')
                                    print(str(float(ordetails_row[3])*(float(ordetails_row[2])-float(ordetails_row[4]))))
                                    x += 1
                                else:
                                    count = True

print(x)