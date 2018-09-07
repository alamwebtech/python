age = input("How old are you!! : ")
if age:
    age = int(age)
    if age >= 18 and age < 21:
        print(f"You are {age} years old and you can enter but can not drink")
    elif age >=21:
        print(f"you are {age} years old and you can enter and drink")
    else:
        print(f"You are {age} years old and you are too young to enter here!!")
else:
    print("Please enter a number")