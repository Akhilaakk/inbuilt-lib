""" import pandas as pd

a=pd.read_csv("sales_data.csv")
b=pd.DataFrame(a)
print(a)
print(b)
data = b.dropna()
c = b.groupby("product_category").sum()
print(c)
 """

""" import numpy as np

sales=np.array([1000,2200,31234,4986,500,6000,1205])
print(np.mean(sales))
print(sales.sum())
sd=(sales-sales.min()/(sales.max()-sales.min()))
print(sd)
 """

import pandas as pd

""" months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [12000, 15000, 17000, 16000, 18000]
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Growth")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show() """


""" categories = ["Electronics", "Clothing", "Home"]
performance = [30000, 20000, 15000]
plt.bar(categories, performance, color=['blue', 'green', 'orange'])
plt.title("Product Category Performance")
plt.show() """

regions = ["North", "South", "East", "West"]
distribution = [25, 30, 20, 25]
plt.pie(distribution, labels=regions)
plt.title("Regional Sales Distribution")
plt.show()















