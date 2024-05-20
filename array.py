from array import *

# vals = array('i',[5,9,8,4,2])

# print(vals)
# print(vals.buffer_info())
# print(vals.typecode)
# vals.reverse()
# print(vals)

# for i in range(len(vals)):
#     print(vals[i])

# print("works same")

# for i in vals:
#     print(i)

# newArr = array(vals.typecode, (a for a in vals))  #copying array
# for j in newArr:
#     print(j)


#inputting the array value
arr = array('i', [])

n = int(input("Enter the length of the array"))

for i in range(n):
    x = int(input("Enter the value"))
    arr.append(x)

print(arr)


#array check

val = int(input("Enter the value for the search"))

k = 0
for e in arr:
    if e == val:
        print(k)
        break

    k+=1

print(arr.index(val)) #using function to check