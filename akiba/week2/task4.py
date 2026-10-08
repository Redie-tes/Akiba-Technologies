pal = input("Enter the word: ")
pal.lower()
name = ""
name = pal[::-1]
if pal.lower() == name.lower():
    print("The word is a palindrome")
else:    
    print("The word isnot palindrome.")