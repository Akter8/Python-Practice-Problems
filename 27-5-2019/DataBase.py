from pymongo import MongoClient
import pandas as pd

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]

print(mydb.list_collection_names())
mydb.customers.drop()
mydb.categories.drop()
mydb.employees.drop()
mydb.employee_territories.drop()
mydb.northwind.drop()
mydb.order_details.drop()
mydb.orders.drop()
mydb.products.drop()
mydb.regions.drop()
mydb.shippers.drop()
mydb.suppliers.drop()
mydb.territories.drop()


categories = mydb["categories"]
df = pd.read_bson("C:/Users/akhil/Documents/PS-1/27-5-2019/categories.bson",engine='python')
records = df.to_dict(orient="records")
results = mydb.categories.insert_many(records)

customers = mydb["customers"]
df = pd.read_csv("C:/Users/akhil/Documents/PS-1/27-5-2019/customers.csv",error_bad_lines=False)
records = df.to_dict(orient="records")
results = mydb.customers.insert_many(records)

employees = mydb["employees"]
df = pd.read_csv("C:/Users/akhil/Documents/PS-1/27-5-2019/employees.csv",error_bad_lines=False,engine="python")
records = df.to_dict(orient="records")
result = mydb.employees.insert_many(records)

employee_territories = mydb["employee_territories"]
df = pd.read_csv("C:/Users/akhil/Documents/PS-1/27-5-2019/employee-territories.csv")
records = df.to_dict(orient="records")
result = mydb.employee_territories.insert_many(records)


northwind = mydb["northwind"]
df = pd.read_csv("C:/Users/akhil/Documents/PS-1/27-5-2019/northwind.csv",error_bad_lines=False,engine="python")
records = df.to_dict(orient="records")
result = mydb.northwind.insert_many(records)

order_details = mydb["order_details"]
df = pd.read_csv("C:/Users/akhil/Documents/PS-1/27-5-2019/order-details.csv")
records = df.to_dict(orient="records")
results = mydb.order_details.insert_many(records)


orders = mydb["orders"]
df = pd.read_csv("C:/Users/akhil/Documents/PS-1/27-5-2019/orders.csv",error_bad_lines=False)
records = df.to_dict(orient="records")
results = mydb.orders.insert_many(records)


products = mydb["products"]
df = pd.read_csv("C:/Users/akhil/Documents/PS-1/27-5-2019/products.csv")
records = df.to_dict(orient="records")
results = mydb.products.insert_many(records)


regions = mydb["regions"]
df = pd.read_csv("C:/Users/akhil/Documents/PS-1/27-5-2019/regions.csv")
records = df.to_dict(orient="records")
results = mydb.regions.insert_many(records)


shippers = mydb["shippers"]
df = pd.read_csv("C:/Users/akhil/Documents/PS-1/27-5-2019/shippers.csv")
records = df.to_dict(orient="records")
results = mydb.shippers.insert_many(records)

suppliers = mydb["suppliers"]
df = pd.read_csv("C:/Users/akhil/Documents/PS-1/27-5-2019/suppliers.csv",error_bad_lines=False)
records = df.to_dict(orient="records")
results = mydb.suppliers.insert_many(records)

territories = mydb["territories"]
df = pd.read_csv("C:/Users/akhil/Documents/PS-1/27-5-2019/territories.csv")
records = df.to_dict(orient="records")
results = mydb.territories.insert_many(records)

print(mydb.list_collection_names())

