import numpy as np 
import pandas as pd 

#Q1
df = pd.read_csv("Salaries.csv")
#df.set_index("Id",inplace=True)

#Q2
col = df.shape[1]
row = df.shape[0]

#Q3
df["BasePay"] = df["BasePay"].replace("\w+|\s+",float(0),regex=True)
avg = df["BasePay"].mean()
print("3. Average BasePay is:",avg)

#Q4
maxp = df["BasePay"].max()
print("4. Maximum BasePay is:",maxp)

#Q5
print("The unique values of Job titles with their counts are:")
print((df["JobTitle"].str.lower().unique()))

#Q6
x = df.sort_values(by="BasePay",ascending=False)
print(x.head())

#Q7
print(df[df["EmployeeName"].str.lower()=="david sullivan"][["EmployeeName","BasePay"]])

#Q8
print(len(df[df["JobTitle"].str.lower()=="captain, fire suppression"][["EmployeeName", "JobTitle","BasePay"]]))

#Q9
print(df[df["JobTitle"].str.lower().str.contains("chief")==True])

#Q10
print(df[df["TotalPay"]==df["TotalPay"].min()])

#Q11
df = df[df["EmployeeName"]!="Not provided"]
print(df[ (df["TotalPay"]<=0) ])

#Q12
print(df.groupby("Year").mean()["TotalPay"])

#Q13
print(df["JobTitle"].str.lower().value_counts().head(5))

#Q14
print(df[(df["EmployeeName"].str.startswith("R")==True ) & (df["EmployeeName"].str.endswith("n")==True)])
print(df[df["EmployeeName"].str.contains("^R(\w*\s*)*n$",regex=True)==True])