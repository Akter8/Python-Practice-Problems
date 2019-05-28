import csv


count = 0
with open('C:/Users/akhil/Documents/PS-1/24-5-2019/shippers.csv','rt') as shippers:
    shippers_data = csv.reader(shippers)
    for shippers_row in shippers_data:
        if shippers_row[1] == 'Speedy Express':
            with open('C:/Users/akhil/Documents/PS-1/24-5-2019/orders.csv','rt') as orders:
                orders_data = csv.reader(orders)
                for orders_row in orders_data:
                    if orders_row[6] == shippers_row[0]:
                        with open('C:/Users/akhil/Documents/PS-1/24-5-2019/order-details.csv','rt') as ordetails:
                            ordetails_data = csv.reader(ordetails)
                            for ordetails_row in ordetails_data:
                                if ordetails_row[0] == orders_row[0]:
                                    print(ordetails_row)
                                    count += 1

print(count)

