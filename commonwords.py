str1=input("Enter first string :")
str2=input("Enter second string :")
l1=str1.split()
l2=str2.split()
for i in l1:
    if i in l2:
        print(i)