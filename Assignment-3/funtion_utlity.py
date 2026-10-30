def factorial(n):
    if n==1 or n==0:
        return 1
    elif n < 0:
        return 0
    else:
        return n*factorial(n-1)
    
n=int(input("Enter a Number : "))
fact=factorial(n)
if fact > 0 :
    print(f"Factorial of {n} is ", fact)
else:
    print("Enter a positive number.")