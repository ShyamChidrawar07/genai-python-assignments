import numpy as np

A=np.array([10,20,30,40])
B=np.array([1,2,3,4])
print(f"Performing Mathematical Operations on 1D Arrays A:{A} and B:{B} ")
print("Addition of A and B:\n",A+B)
print("Subtraction of A and B:\n",A-B)
print("Multiplication of A and B:\n",A*B)
print("Division of A and B:\n",A/B) 
print("Power of A**2:\n",A**2 )

print("\nPerforming Mathematical Operations on Arrays A and B Using Numpy Functions")
print("Addition of A and B:\n",np.add(A,B))
print("Subtraction of A and B:\n",np.subtract(A,B)) 
