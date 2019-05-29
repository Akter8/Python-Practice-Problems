from pymongo import MongoClient
import pandas as pd

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["CreditCardCLI"]
mydb.users.drop()
mydb.info.drop()
print(mydb.list_collection_names())


users = mydb["users"]
df = pd.read_excel("C:/Users/akhil/Documents/PS-1/28-5-2019/user.xlsx")
records = df.to_dict(orient="records")
results = mydb.users.insert_many(records)

info = mydb["info"]
df = pd.read_excel("C:/Users/akhil/Documents/PS-1/28-5-2019/info.xlsx")
records = df.to_dict(orient="records")
results = mydb.info.insert_many(records)

print(mydb.list_collection_names())

for x in users.find():
    print(x)