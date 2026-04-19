# print("Hello from lesson 10")

# import random

# number = random.randint(1,15)
# userans = int(input("pick a number between 1 and 15. "))
# if number == userans:
#     print("That's it!")

# num = int(input("give me a number. "))
# if num > 0:
#     print(num , "is positive.")
# else:
#     print(num , "is negative.")

# age = int(input("how old are you? "))
# if age < 13:
#     print("child")
# else:
#     if age <= 19:
#         print("teen")
#     else:
#         print("adult")

# temp = int(input("what temp is it outside? "))

# if temp > 30:
#     print("it's way to hot GO SWIMMING!!!")
# elif temp >= 25:
#     print("it's normal temp play basket ball.")
# elif temp >= 20:
#     print("go cycling")
# else:
#     print("it's too cold outside go read indoors.")

score = int(input("what mark did you get? "))

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F go study!")