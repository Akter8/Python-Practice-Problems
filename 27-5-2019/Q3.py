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

c = {}
for category in mydb.categories.find():
    c.update({category["CategoryID"]:category["CategoryName"]})

for category in c:
    print("The Category is:",c[category])
    for product in mydb.products.find():
        if product["CategoryID"] == category:
            print("\t",product["ProductName"])