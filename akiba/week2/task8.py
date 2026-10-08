num = int(input("Enter positive number: "))
even = 0
odd = 0
sum = 0
for i in range(1,num + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
    sum +=i
print(f'''Even numbers: {even}
odd numbers: {odd}
sum: {sum}''')
    
