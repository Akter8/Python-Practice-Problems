import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv("company_sales_data.csv")

monthList  = df ['month_number'].tolist()
bathingsoapSalesData   = df ['bathingsoap'].tolist()
plt.bar(monthList, bathingsoapSalesData)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title(' Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('bathingsoap sales data')
plt.savefig('C:/Users/akhil/Documents/PS-1/3-6-2019/Matplotlib/sales_data_of_bathingsoap.png', dpi=150)
plt.show()