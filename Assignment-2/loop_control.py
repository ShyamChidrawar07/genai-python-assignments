daily=[200,150,0,400,50,-1,300]
total_sales=0
for day in daily:
    if day == -1:
        print("Currepted Data")
        break
    elif day == 0:
        print("No sale")
        continue
    else:
        total_sales += day
        print("Running Total",total_sales)

print("Final Total = ",total_sales)
