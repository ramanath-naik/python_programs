#dictionary ordered,changeable, no duplicates

dict={"brand":"ford",
      "model":"mustang",
      "year":1999
      }
print(dict)

# access the dictionary value using key
print(dict["model"])

#using get method

print(dict.get("model"))

#listing all the keys in dictionary

print(dict.keys())

#change values
dict["year"]=2000
print(dict)

#using update method
dict.update({"year":2023})
print("after update",dict)

#adding value
dict["color"]="red"
print(dict)

#The pop() method removes the item with the specified key name
dict.pop("model")
print(dict)

#The popitem() method removes the last inserted item
dict.popitem()
print(dict)

#The del keyword removes the item with the specified key name
#del dict["model"]

#del deletes the whole dictionary
#del dict

#clear() method empties the dictionary
dict.clear()

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






