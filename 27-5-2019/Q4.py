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

# for territory in employee_territories.find():
#     print(territory)
for region in regions.find():
    print("The region is:",region["RegionDescription"])
    count = []
    for territory in territories.find():
        if territory["RegionID"] == region["RegionID"]:
            #print('R',region["RegionID"])
            for employee_territory in employee_territories.find():
                if employee_territory["TerritoryID"] == territory["TerritoryID"]:
                    #print('T',territory["TerritoryID"])
                    for employee in employees.find():
                        if str(employee_territory["EmployeeID"]) == str(employee["EmployeeID"]):
                            #print(employee["LastName"])
                            count.append(employee["EmployeeID"])
    print(len(set(count)))