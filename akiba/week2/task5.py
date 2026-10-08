num = int(input("enter a number with 2 and more digits: "))
sum = 0
while num % 10 != 0:
    reminder = num % 10
    sum += reminder
    num = num // 10
print(sum)
