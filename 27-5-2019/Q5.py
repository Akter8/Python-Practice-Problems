from pymongo import MongoClient
import pandas as pd

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]

categories = mydb["categories"]
customers = mydb["customers"]
employees = mydb["employees"]
employee_territories = mydb["employee-territories"]
northwind = mydb["northwind"]
order_details = mydb["order-details"]
orders = mydb["orders"]
products = mydb["products"]
regions = mydb["regions"]
shippers = mydb["shippers"]
suppliers = mydb["suppliers"]
territories = mydb["territories"]

#Shipper ID from Shipper
#to ShipVia from Orders
#to OrderID in orderdetails
count = 0
for shipper in shippers.find():
    if shipper["CompanyName"] == "Speedy Express":
        for order in orders.find():
            if shipper["ShipperID"] == order["ShipVia"]:
                for ordertail in order_details.find():
                    if order["OrderID"] == ordertail["OrderID"]:
                        print(ordertail) 
                        count += 1
print(count)