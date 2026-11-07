import numpy as np

arr1d=np.arange(1,11)
print("1D Array:\n",arr1d)
print("Shape of 1D Array:", arr1d.shape)
print("Data Type of 1D Array:", arr1d.dtype)

arr2dd=np.arange(1,10).reshape(3,3)
print("2D Array:\n", arr2dd)
print("Shape of 2D Array:", arr2dd.shape)
print("Data Type of 2D Array:", arr2dd.dtype)