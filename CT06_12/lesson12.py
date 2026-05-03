# print("Hello from lesson 12")

# game_status = "active"
# if game_status == "active" or not (game_status == "paused"):
#     print("game in progress")
# else:
#     print("game is paused")

# visitor =  4
# while visitor < 25:
#     visitor += 1
#     print(visitor)

# counter = 1
# while True:
#     print(counter)
#     if counter == 30:
#         break
#     counter += 1

# order = ""
# user = ""
# add_on = ""
# while True:
#     add_on = input("what do you want to add on to your meal?")
#     if add_on == "end":
#         break
#     user = user + f"{add_on}, "
# print("this is your order: " + user)
# count = 10
# while count > 0:
#     print(count)
#     count -= 1
#     if count == 5:
#         break
# else:
#     print("happy new year")

import random
num1 = random.randint(1,10)
num2 = random.randint(1,10)
while True:
    userans = int(input(f"What is {num1} + {num2}? "))
    realans = num1 + num2
    if userans == realans:
        print("you are correct!")
        break
    else:
        print("You are wrong!!! Do again.")
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)