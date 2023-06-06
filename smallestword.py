#Program to display smallest word from the string
str=input("Enter any string: ")
L=str.split()
min=50
b=""
for i in L:
    if len(i)<min:
        b=i
        min=len(i)
print("smallest word is :",b)