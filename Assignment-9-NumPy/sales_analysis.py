import numpy as np
sales = np.array([1200,1500,900,2000,1800,1700,1600])
print("Sales: ",sales)
print("\nTotal Weekly Sales: ",np,sum(sales))
print("\nAverage daily sales: ",np.mean(sales))
print(f"\nHighest Sale: {np.max(sales)}, Lowest Sale: {np.min(sales)}")
print("\nStandard Deviation of sales: ",np.std(sales))
print("\nDays when sales were above average: ",)
mean_sales = np.mean(sales)
for i in range(len(sales)):
    if sales[i] > mean_sales:
        print(sales[i],end=" ")