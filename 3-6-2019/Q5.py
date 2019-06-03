import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv("company_sales_data.csv")

monthlist = df["month_number"].tolist()
facecream = df["facecream"].tolist()
facewash = df["facewash"].tolist()

plt.bar([x-0.25 for x in monthlist],facecream,label="facecream data",align="center",width=0.25)
plt.bar([x for x in monthlist],facewash,label="facewash data",align="center",width=0.25)
plt.title("facewash and facecream data")
plt.legend(loc="upper left")
plt.xticks(monthlist)
plt.xlabel("Month number")
plt.ylabel("Sales data")
plt.grid(b=True,linestyle="--")
plt.show()