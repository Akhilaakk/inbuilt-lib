import numpy as np
import matplotlib.pyplot as plt

plt.figure()
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [12000, 15000, 17000, 16000, 18000]
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Growth")
plt.xlabel("Month")
plt.ylabel("Sales")
 

plt.figure()
categories = ["Electronics", "Clothing", "Home"]
performance = [30000, 20000, 15000]
plt.bar(categories, performance, color=['blue', 'green', 'orange'])
plt.title("Product Category Performance")

plt.figure()
regions = ["North", "South", "East", "West"]
distribution = [25, 30, 20, 25]
plt.pie(distribution, labels=regions)
plt.title("Regional Sales Distribution")
