a = []
number = int(input("Enter the Total Elements : "))
print("Enter elements to be inserted")

for i in range(number):
    value = int(input(""))
    a.append(value)

for i in range(number -1):
    for j in range(number - i - 1):
        if(a[j] > a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp

print("The sorted list is  : ", a)
