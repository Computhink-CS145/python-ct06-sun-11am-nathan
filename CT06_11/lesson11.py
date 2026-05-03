# # print("Hello from lesson 11")

# price = int(input("what is the price of the item? "))
# if price <= 5:
#     print("Sounds good")
# elif price <= 50:
#     print("Are you sure you need this?")
# elif price <= 500:
#     print("Where are you getting this money from?!")
# else:
#     print("Don't even think about it!!!!!!!!!!")

# r1 = 125
# r2 = 150
# if r1 and r2 > 120:
#     print("You are allowed to ride!")

# num1 = int(input("give me a number "))
# divby3 = num1 % 3 == 0
# divby7 = num1 % 7 == 0
# if divby3 and divby7 == True:
#     print("Your number is divisible by 3 and 7.")

# rider1 = 25
# rider2 = 6

# if (rider1 >= 18) or (rider2 >= 18):
#     print("you can go in")

# age = int(input("What is your age? "))
# if (age < 12) or (age > 65):
#     print("You get a discount!")
# else:
#     print("you get no discount")

# colour = input("Give me a colour(no capital letters)")
# isgreen = colour =="green"
# if not isgreen:
#     print("try again")
# else:
#     print("correct!")

day = input("what day of the week is it? ")
saturday = day == "saturday"
sunday = day == "sunday"
if not (saturday or sunday):
    print("it's not the weekends")
else:
    print("Weekends!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")