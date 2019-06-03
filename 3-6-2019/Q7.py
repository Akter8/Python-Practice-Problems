import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv("company_sales_data.csv")

profitList = df ['total_profit'].tolist()
labelsx = {1:'low', 2:'average', 3:'Good', 4:'Best'}
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(profitList, profit_range, label = 'Profit data')
plt.xlabel('profit range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.legend(loc='upper left')
plt.xticks(profit_range)
#plt.yticks(labelsx)
plt.title('Profit data')
plt.show()