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


dic = {}
for x in orders.find():
    if x["CustomerID"] in dic:
        dic[x["CustomerID"]] += 1
    else:
        dic.update({x["CustomerID"]:0})

maxi = 0
for x in dic:
    if dic[x]>maxi:
        y = x
        maxi = dic[x]
#print(dic)
myquery = {"CustomerID":y}
for z in customers.find(myquery):
    print(z["CompanyName"])
    break
print(maxi)