str=input("Enter a string:")
str=str.casefold()
rev_str=reversed(str)
if list(str)== list(rev_str):
    print("The string is a Palindrome")
else:
    print("The string is not palindrome")