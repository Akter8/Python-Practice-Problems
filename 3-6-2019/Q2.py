import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv("company_sales_data.csv")
monthlist = df["month_number"].tolist()
fig = df.plot(x="month_number",y="total_units",kind="line",title="Company sales data last year",xticks=monthlist,yticks=[10000, 20000, 30000, 40000, 50000],label="Units sold last year",style="ro--",linewidth=3,markerfacecolor="k")
fig.set_xlabel("Month Number")
fig.set_ylabel("Units sold")
fig.legend(loc=4)
plt.show()