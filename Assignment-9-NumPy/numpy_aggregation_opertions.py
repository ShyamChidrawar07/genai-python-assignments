import numpy as np

data=np.array([[10,20,30],[40,50,60],[70,80,90]])
print("Data:\n",data)
print("\nRow-wise sum:\n", np.sum(data, axis=1))
print("\nColumn-wise sum:\n", np.sum(data, axis=0))
print("\nMinimum values:\n", np.min(data))
print("\nMaximum values:\n", np.max(data))
print("\n Overall Mean:\n", np.mean(data))