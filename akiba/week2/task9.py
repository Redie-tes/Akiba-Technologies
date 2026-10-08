correct_pin = 1234
attempt = 3
for i in range(1, attempt + 1):
    pin = int(input("Enter your PIN: "))
    if pin == correct_pin:
        print("PLEASE proceed to the next step.")
        break
    else:
        print("Incorrect PIN")
        print("Attempts remaining: ",attempt - i)
else:
    print("you have finished your attempts!")
