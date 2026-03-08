# print("Hello from lesson 7")

# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"
# average_score = str(round(average_score,2))
# print("Average score for " + student_name + " is: " + average_score)

# for i in range(1,11):
# #     print(i)

# for i in range(2,21,2):
# #     print (i)

# for i in range(10,0,-1):
#     print(i)

# word = input("What word would you like to reapeat? ")
# num = int(input("how many times would you like to reapeat? "))

# for i in range(1,(num + 1)):
#   print(word)

# name = input("What is your name? ")
# num = int(input("How many times would you like to reapeat? "))

# for i in range(1,(num + 1)):
#     print(f"Nice to meet you, {name}")

# total = 0
# for i in range(1,6):
#     num = int(input("What is number #" + str(i) + "? "))
#     total = total + num
# print(total)

anum = int(input("Which times table? "))
for i in range(1,13):
    answer = anum * i
    print(anum,"x",i,"=",answer)