num=int(input("Enter number : "))
temp=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if temp==rev:
    print("Number is palindrome")
else:
    print("number is not palindrome")

    