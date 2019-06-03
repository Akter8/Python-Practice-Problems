import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv("company_sales_data.csv")

fig = df.plot(kind="line",y="total_profit",x="month_number",title="Company Profit per month")
fig.set_xlabel("Month Number")
fig.set_ylabel("Profit in INR")
plt.show()
