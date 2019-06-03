import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv("company_sales_data.csv")

monthlist = df["month_number"].tolist()
facecream = df["facecream"].tolist()
facewash = df["facewash"].tolist()
toothpaste = df["toothpaste"].tolist()
bathingsoap = df["bathingsoap"].tolist()
shampoo = df["shampoo"].tolist()
moistutizer = df["moisturizer"].tolist()

plt.plot(monthlist,facecream,marker='o',label='face cream sale data')
plt.plot(monthlist,facewash,marker='o',label='face wash sale data')
plt.plot(monthlist,toothpaste,marker='o',label='tooth paste sale data')
plt.plot(monthlist,bathingsoap,marker='o',label='bathing soap sale data')
plt.plot(monthlist,shampoo,marker='o',label='shampoo sale data')
plt.plot(monthlist,moistutizer,marker='o',label='moisturizer sale data')
plt.legend(loc="upper left")
plt.xticks(monthlist)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title("Sales Data")
plt.show()