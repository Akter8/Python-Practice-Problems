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



prodid = []
myquery = {"ProductName":{"$regex":"Tofu|Konbu"}}
for x in products.find(myquery):
    prodid.append(x["ProductID"])
print(prodid)

orderid = []
for x in prodid:
    myquery = {"ProductID":x}
    for y in order_details.find(myquery):
        orderid.append(y["OrderID"])

cid = []
for y in orderid:
    myquery = {"OrderID":y}
    for z in orders.find(myquery):
        cid.append(z["CustomerID"]) 
        
cname = []
for z in cid:
    myquery = {"CustomerID":z}
    for a in customers.find(myquery):
        cname.append(a["CompanyName"])

print(sorted(set(cname)))
print(len(set(cname)))
#ProductID to OrderID to CustomerID to CustomerName