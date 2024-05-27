# f = open("Data.txt",'r')
# print(f)


# open('Data.txt', 'r')
# # print(f.read())
# print(f.readline(),end="")
# print(f.readline(2),end="") #2 nd line
# print(f.readline())

# f1 = open('abc','w')  # it wil create new file
# f1.write("new file")

# #To append data
# f2 = open('abc', 'a')
# f2.write(" is added")

#copy all the data

f = open("Data.txt",'r')

f1 = open('abc','w')

for data in f:
    f1.write(data)

#for binary 
f = open('mumbai.jpg','rb')

f1 = open('Mumbaii.jpg','wb')

for i in f:
    f1.write(i)