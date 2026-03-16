import numpy as np

sales = np.array([1000, 2200, 31234, 4986, 500, 6000, 1205])
sd = (sales - sales.min()) / (sales.max() - sales.min())

