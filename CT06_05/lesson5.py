# print("Hello from lesson 5")

# name = input("What is the persons name? ")
# age = input("How old is the person? ")
# message = input("make a personal message for the person you're sending to. ")

# print(f"Happy {age}th Birthday {name}! {message}.")

# for count in range(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
#     print(67)

# for something in range(100):
#     print("I like chicken rice.")

# for count in range(9999999999999999999999999999):
#     print("I like cake,")
#     print(" give me more!")

# myword = "hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"
# for letter in myword:
#     print("Give me a " + letter)

# for count in range(0,60):
#     print(count)

# for count in range(1,6):
#     print(count)

# for count in range(51,101):
#     print(count)

# for count in range(18,30):
#     print(count)

# for count in range(2,25,2):
#      print(count)

# for count in range(8,97,8):
#     print(count)

n1 = int(input("give me a number: "))
n2 = int(input("give me a another number: "))
if n1 < n2:
    start = n2
    stop = n1
else:
    start = n1
    stop = n2

for count in range(start,stop):
    print(count)