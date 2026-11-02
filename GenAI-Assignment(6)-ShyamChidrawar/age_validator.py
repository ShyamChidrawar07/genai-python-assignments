def check_age(age:int)-> bool:
    try:
        if not age >= 1 and age <= 120:
            raise ValueError("Age must be between 1 to 120 years")
        else:
            return True
    except (ValueError ) as e:
        print(f"Error : {e}")
        return False
age=int(input("Enter a valid age : "))
print(f"Is {age} is valid age : ",(check_age(age)))