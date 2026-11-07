import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])
print("Marks: ", marks)
print("Marks in Sorted Order: ", np.sort(marks))
print("\n25th Percentile: ", np.percentile(marks, 25))
print("\n50th Percentile (Median): ", np.percentile(marks, 50))
print("\n75th Percentile: ", np.percentile(marks, 75))
print("\nNumber of Students scored above average marks: ", np.sum(marks > np.mean(marks)))