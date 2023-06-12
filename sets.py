#sets are unordered, unchangeable*, and unindexed.

set1={1,2,3,55,33}
print(set1)

#duplicates not allowed

set2={33,4,5,6,7,5,6,99}
print(set2)

#true and 1 considered as same value

set3={True,1,2,3,"yes"}
print(set3)

#access set items
set4={"raju","deepu","vishu"}

for i in set4:
    print(i)

#add items to current set using another set using update
set5={1,2,3,4}
set6={5,6,7,8}
set5.update(set6)
print(set5)

#we can also add list, tuple and set to the current set
set={"ganesh","anand","aditya"}
list=["akshay","abhi"]
set.update(list)
print(set)

#remove set item
set7={"ganesh","anand","aditya"}
set7.remove("ganesh")
print(set7)

#we can also use discard method to remove an item. if item is not present, this will not rise an error

#remove random element using pop
s1={"white","black","blue","green"}
s1.pop()
print(s1)

#use clear method to remove all the elements from the set
s1.clear()
print(s1)
#del s1 # to delete whole set



