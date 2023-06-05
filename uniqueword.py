str=input("Enter a string")
l=str.split()
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
str=""
for i in l1:
    str=str+" "+i
print("String with unique words are :",str)
