# if statement
print("If statement:")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
print("Thank you for voting.")

# if-else statement
print("If-else statement:")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
print("Thank you for voting.")

# if-elif-else statement
print("If-elif-else statement:")
age = int(input("Enter your age: "))
if age < 18:
    print("You are not eligible to vote.")
elif age >= 18 and age <= 60:
    print("You are eligible to vote.")
else:
    print("You are too old to vote.")
print("Thank you for voting.")

# nested if statement
print("Nested if statement:")
age = int(input("Enter your age: "))
if age >= 18:
    if age <= 60:
        print("You are eligible to vote.")
    else:
        print("You are too old to vote.")
else:
    print("You are not eligible to vote.")
print("Thank you for voting.")
