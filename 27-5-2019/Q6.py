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

count = 0
for order in orders.find():
    for ordetails in order_details.find():
        if order["OrderID"] == ordetails["OrderID"]:
            for product in products.find():
                if ordetails["ProductID"] == product["ProductID"]:
                    print(order["OrderID"],product["ProductID"],product["ProductName"],ordetails["UnitPrice"],ordetails["Quantity"],ordetails["Discount"])
                    count += 1
print(count)