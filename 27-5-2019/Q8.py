from pymongo import MongoClient

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


for category in categories.find():
    print("The category is:",category["CategoryName"])
    price = 0
    for product in products.find():
        if product["CategoryID"] == category["CategoryID"]:
            price = price + product["UnitsOnOrder"] * product["UnitPrice"]
    print(price)