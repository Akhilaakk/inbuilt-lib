import pandas as pd

a=pd.read_csv("sales_data.csv")
b=pd.DataFrame(a)
data = b.dropna()
c = b.groupby("product_category").sum()
