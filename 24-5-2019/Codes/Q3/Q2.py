import csv

dic = {}
with open('C:/Users/akhil/Documents/PS-1/24-5-2019/orders.csv','rt') as orders:
    orders_data = csv.reader(orders)
    for orders_row in orders_data:
        if orders_row[1] in dic:
            dic[orders_row[1]] += 1
        else:
            dic.update({orders_row[1]:0})

maxi = 0

for cust in dic:
    if dic[cust] > maxi:
        c = cust
        maxi = dic[cust]

with open('C:/Users/akhil/Documents/PS-1/24-5-2019/customers.csv','rt') as custormers:
    customers_data = csv.reader(custormers)
    for customer_row in customers_data:
        if c == customer_row[0]:
            print(customer_row)
            print(maxi)
            break

