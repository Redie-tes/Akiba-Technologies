num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 > num2:
    if num1 > num3:
        print(num1,"is the largest.")
    elif num1 < num3:
        print(num3, "is the largest.")
    else:
        print(num1, "and", num3, "are equal and the largest")
elif num2 > num1:
    if num2 > num3:
        print(num2, "is the largest.")
    elif num2 < num3:
        print(num3, "is the largest.")
    else:
        print(num2, "and", num3 , "are equal and the greatest.")
elif num1 == num2:
    if num1 == num3:
        print("all three of the numbers are equal")
    elif num1 > num3:
        print(num1, "and", num2,"are equal and the greatest.")
    else:
        print(num3,"is the greatest.")
