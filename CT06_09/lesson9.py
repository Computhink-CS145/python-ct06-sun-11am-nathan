# print("Hello from lesson 9")

# import random

# num1 = random.randint(1,6)
# num2 = random.randint(1,6)
# num3 = random.randint(1,6)
# print("num1 is ", num1)
# print("num2 is ", num2)
# print("num3 is ", num3)
# even_odd = (num1 % 2) == (num2 % 2) == (num3 % 2)
# print("all is even / odd ", even_odd)


apples = int(input("how many appples do you want to buy? "))
oranges = int(input("how many oranges do you want to buy? "))
if apples >= 5:
    apple_price = apples * 0.6 * 0.9
else:
    apple_price = apples * 0.6

if oranges >= 5:
    orange_price = oranges * 0.9 * 0.9
else:
    orange_price = oranges * 0.9
total = apple_price + orange_price
print("your total is $" ,total)