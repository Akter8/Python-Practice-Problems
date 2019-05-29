from pymongo import MongoClient
import pandas as pd

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["CreditCardCLI"]

for x in mydb.users.find():
    print(x)

for x in mydb.info.find():
    print(x)