# creating list
numbers=[1,2,5]
print(numbers)

#list with mixed data
my_list=[1,"hello",4.4]
print(my_list)

#accessing list elements
languages=["python","csharp","reactjs","java"]
print(languages[1])
print(languages[3])
#negative indexing
print(languages[-1])
print(languages[-2])

#list slicing
mylist=['p','y','t','h','o','n','p','r','o','g','r','a','m']
#items from index 2 to 4
print(mylist[2:5])
# items from index 5 to end
print(mylist[5:])
# items beginning to end
print(mylist[:])

#add elements to list

numbers=[22,33,44,55,66]
print("before append: ",numbers)
numbers.append(77)
print("after append: ",numbers)

#extend
list1=[1,3,5]
list2=[2,4,6]
print("List1: ",list1)
print("List2: ",list2)
list1.extend(list2)
print("List after extend: ",list1)

#insert
vowel=['a','e','i','u']
vowel.insert(3,'o')
print("vowel: ",vowel)

#change list items
number=[1,3,4,6]
number[2]=22
print(number)

#Remove item from the list
num=[1,2,3,4]
#removing specified item
num.remove(1)
print(num)
#remove specified index
num.pop(2)
print(num)
#del num[3]

#delete the list completely
del num
#print(num)

#clear the list
#num.clear() #the list remains but elements are removed

#loop through a list
thislist=["apple","banana","orange"]
print("list items are")
for i in thislist:
    print(i)
#join two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#sort list
n=[23,450,33,567,555]
n.sort()

#copy list
m=["apple","banana","cherry"]
l=m.copy()
print(l)






