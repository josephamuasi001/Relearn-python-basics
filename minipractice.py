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

if 18 <= age1 <= 60:
    print("Working Class")
else:
    print("Not working class")


#Joined conditions 
age = int(input("Enter your age here: "))

permission = input("Do you have a special permission? (yes/no) ")
if (18 <= age <= 60) or (permission == "yes"):
    print("Allowed")
else:
    print("Not allowed")



# #Loops - While Loop
# Write a program that:

# Starts at 1
# Prints numbers 1 to 10 using a while loop

count = 1

while count <= 10:
    print(count)
    count += 1


#forloop

for i in range(2,21):
    print(i)



#What I have learnt soo far

num = int(input("Enter a number here: "))

while num != -1:
    print(f"You entered: {num}")
    num = int(input("Enter a number here: "))

print("Program ended")



#List

numbers = [5, 10, 15, 20]

#Modifying list 
numbers[0] = 50
numbers[2] = 150

for number in numbers:
    print(number * 2)


#List Task

my_numbers = [1, 2, 3, 4, 5]

for my_num in my_numbers: 
    updated = my_num + 5
    print(updated)

