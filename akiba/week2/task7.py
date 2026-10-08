# Instead of doing challenge 1 and 2 separately I used if condition 
#to do both of them in one code 
choice = int(input('''which game do you want to play:
1. Guess until you find the correct number or
2. Trying to find the correct number within only 5 attempts ?'''))
secretnum = 8
if choice == 1:
    guess = int(input("Enter your guess: "))
    countofguess = 1
    while guess != secretnum:
        guess = int(input("Enter your guess: "))
        countofguess +=1 

    print("Congratualtions!")
    print("You guessed the number in",countofguess, "attempts.")
elif choice == 2:
    attempts = 5
    for i in range(attempts):
        guess = int(input("Enter your Guess: "))
        if guess == secretnum:
            print("Congratulations!")
            print("You guessed the number in ",i+1,"attempts.")
            break
    else:
        print("Game Over!")
else: 
    print("ONLY 1 OR 2!!!")




        