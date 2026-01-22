print("Hello from lesson 4")
red = 1
blue = 2
green = 3

totalred =red * 3
totalblue = blue * 5
totalgreen = green * 4

total = totalred + totalblue + totalgreen
print(total)




# name = input("what is your name: ")
# food = input("what food do you like to eat: ")

# sentence = name + " likes to eat" + food
# print(sentence)


## Challenge 1: ask for hobby, then output {name} likes to {}
# hobby = input("what is your hobby: ")
# sentence2 = name + " likes to " + hobby
# print(sentence2)

## Challenge 2: ask for which is favourite country to go holiday, then output, {name} would like to go to {place}

# num1 = input("what is the first number?")
# num2 = input("what is the second number?")
# num3 =int(num1) + int(num2)
# print(num1 + " + " + num2 + " = " + str( num3 ))



# ## Task 3: Type conversion, math, and string concatenation

# **Task 3a**:
# 1. Ask the user for their current age using input(). Convert this
# to an integer.
# 2. Add 1 to their age and convert it back to a string.
# 3. Then print a message saying "Next year, you will be [age+1]
# years old."

# currentage = int(input("what is your current age? "))
# nextyear = currentage + 1
# print("next year you will be " + str(nextyear))

# **Task 3b**:
# 1. Use input() to ask the user for a number. Convert this number
# from a string to an integer.
# 2. Double the number and convert it back to a string.
# 3. Print "Double your number is [double the number]".

# number = input("pick a number ")
# double_the_number = int(number) * 2
# print(f"Double your number is {double_the_number}.")

# **Task 3c**:
# 1. Use input() to ask the user for the year they were born and
# convert it to an integer.
# 2. Subtract the birth year from the current year (assume the
# current year as an integer) to find their age.
# 3. Convert the age back to a string and print "You are [age]
# years old".

# bornyear = int(input("What year were you born in? "))
# currentyear = 2026
# age = currentyear - bornyear
# sentence = f"You are {age} years old"
# print(sentence)

# ---------------------------------------------------------------number



# create an email address for a person
# format is firstname.lastname2018@gmail.com
# ask for firstname, lastname and birth-year

# firstname = input("What is your first name? ")
# lastname = input("What is your last name? ")
# birthyear = input("what is your birth year? ")
# sentence =  f"Your email is {firstname}.{lastname}{birthyear}@gmail.com"
# print(sentence)

# Exercise 8: Area of a Circle width 
# Write a program to ask the user for the radius of a circle, convert it to
# a float, calculate the area using the formula (area = 3.14 * r^2), and
# display the result using . Example:
# Input: radius = 7
# Output: "The area of the circle is 153.86."

radius = int(input("what is the radius "))
circlearea = (radius ** 2) * 3.14
print(circlearea)