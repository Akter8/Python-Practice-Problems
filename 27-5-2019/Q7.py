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

seafood = []
beverage = []

for category in categories.find():
    if category["CategoryName"] == "Seafood" or category["CategoryName"] == "Beverages":
        for product in products.find():
            if category["CategoryID"] == product["CategoryID"]:
                for ordetails in order_details.find():
                    if ordetails["ProductID"] == product["ProductID"]:
                        for order in orders.find():
                            if order["OrderID"] == ordetails["OrderID"]:
                                if category["CategoryName"] == "Seafood":
                                    seafood.append(order["CustomerID"])
                                else:
                                    beverage.append(order["CustomerID"])
x = list(set(seafood) & set(beverage))
print(x)
count = 0
for i in x:
    for customer in customers.find():
        if customer["CustomerID"] == i:
            count += 1
print(count)