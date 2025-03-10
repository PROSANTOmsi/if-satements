# if-satements

#if satement 
age = int(input("enter your age for survey: "))

if age >= 20:
    print(f"your age which is {age} is applicable for the registration")
else:
    print(f"your age which is {age} is not applicable for the registration")

#elif
age = int(input("enter your age for survey: "))

if age >= 20:
    print(f"your age which is {age} is applicable for the registration")
elif age <= 0:
    print("you haven't even been born yet!!")
else:
    print(f"your age which is {age} is not applicable for the registration")
