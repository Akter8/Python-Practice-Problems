import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv("company_sales_data.csv")

monthlist = df["month_number"].tolist()
toothpaste = df["toothpaste"].tolist()

plt.scatter(monthlist,toothpaste,label="Toothpaste sales data")
plt.title("Toothpaste Data")
plt.grid(b=True)
plt.legend(loc="upper left")
plt.xticks(monthlist)
plt.yticks(np.arange(4500,8001,500))
plt.xlabel("Month number")
plt.ylabel("Sales data")
plt.show()