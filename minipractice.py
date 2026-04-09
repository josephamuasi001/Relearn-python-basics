# Write a program that:

# Asks for your name
# Asks for your age
# Prints:
# My name is ___ and I am ___ years old


# name = input("Enter your name here: ")
# age = int(input("Enter your age here: "))

# print(f"My name is {name} and I am {age} years old")


number = int(input("Enter a number here: "))

if number > 100:
    print("Too big")
else:
    print("Okay")



#Conditions AND/OR

age1 = int(input("Enter your age here: "))

if 18 <= age <= 60:
    print("Working Class")
else:
    print("Not working class")


#Joined conditions 
age = int(input("Enter your age here: "))

permission = input("Do you have a special permission? (yes/no) ")
if 18 <= age <= 60 or permission == "yes":
    print("Allowed")
else:
    print("Not allowed")



#Loops - While Loop

