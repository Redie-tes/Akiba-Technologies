i = 0
num = 10
total = 0
large = None
small = None
even = 0
odd = 0
while i< num:
    numbers = int(input(f"Enter the number {i+1}: "))
    i += 1
    total += numbers
    if large is None or numbers > large:
        large = numbers
    if small is None or numbers < small:
        small = numbers
    avg = total/10
    if numbers % 2 == 0:
        even += 1
    else:
        odd += 1

print("The largest number: ", large)
print("The smallest number: ", small)
print("The total sum: ",total )
print("The average: ", avg)
print("Even NUmbers: ", even)
print("Odd numbers: ", odd)
 

    





    
