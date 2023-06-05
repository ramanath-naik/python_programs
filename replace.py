str=input("Enter any string :")
str1=""
for i in str:
    if i.isspace():
        str1=str1+'#'
    else:
        str1=str1+i
print("Output string is :",str1)



