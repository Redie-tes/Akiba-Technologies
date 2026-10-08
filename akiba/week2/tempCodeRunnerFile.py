num = int(input("Enter the number: "))
sum = 0
for i in range(2,num):
    if num % i == 0:
        sum=+1
    else:
        continue
if sum >= 1:
    print("the number isnot a prime number.")
else:
    print("The number is a prime ")
