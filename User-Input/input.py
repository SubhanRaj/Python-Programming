# Input in Python

name = input("What is your name? ")
current_age = input("What is your current age? ")
print ("Hello " + name + "! You are " + current_age + " years old.") # This also demonstrates concatenation

# Convert string to other data types
future_age = input("After how many years do you want to know your age? ")

new_age = int(future_age) + int(current_age) # Convert string to integer
print("You'll be " + str(new_age) + " years old after " + future_age + " years.") # Convert integer to string


