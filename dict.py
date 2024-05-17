#dictionary ordered,changeable, no duplicates

dict1={"brand":"ford",
      "model":"mustang",
      "year":1999
      }
print(dict1)

# access the dictionary value using key
print(dict1["model"])

#using get method

print(dict1.get("model"))

#listing all the keys in dictionary

print(dict1.keys())

#change values
dict1["year"]=2000
print(dict1)

#using update method
dict1.update({"year":2023})
print("after update",dict1)

#adding value
dict1["color"]="red"
print(dict1)

#The pop() method removes the item with the specified key name
dict1.pop("model")
print(dict1)

#The popitem() method removes the last inserted item
dict1.popitem()
print(dict1)

#The del keyword removes the item with the specified key name
#del dict["model"]

#del deletes the whole dictionary
#del dict

#clear() method empties the dictionary
dict1.clear()

#looping dictionary
#print all the key names in the dictionary, one by one
dict2={"brand":"ford",
      "model":"mustang",
      "year":1999
      }
for i in dict2:
    print(i)

#print all the values in the dictionary
for i in dict2:
    print(dict2[i])

#using values method
for i in dict2.values():
    print(i)

#Loop through both keys and values, by using the items() method:
for i,j in dict2.items():
    print(i,j)

#Make a copy of a dictionary with the copy() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)



data = {1:'navin', 2:'kiran', 4:'harsh'}

print(data)

print(data.get(1))
print(data.get(1,'Not Found'))
print(data.get(3,'Not Found'))

keys = ['Navin', 'kiran', 'Harsh']

values = ['Python', 'Java', 'JS']

#adding 2 lists as key value pair to make dictionary
data = dict(zip(keys, values))  

print(data)

del data['Harsh']

data['Ajay'] = "CS"

print(data);

prod = {'JS':'Atom', 'cs':'vs', 'python':['pycharm', 'sublime'], 'Java':{'JSE':'Netbeans', 'JEE':'Eclipse'}, 'tuple':(2,4,6), 'set':{"one", "two"}}

print(prod)

print(prod['python'])
print(prod['tuple'])
print(prod['set'])
print(prod['Java']['JEE'])