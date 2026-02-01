print("Hello from lesson 3")

seafood = 100
sidedish = 20
bowlofrice = 2.50

total = (seafood * 5) + (sidedish * 8) + (bowlofrice * 20)
total1 = total + (total * (10/100))
total2 = total1 + (total1 * (9/100))

print(round(total2,1))