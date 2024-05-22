
def greet():
    print("Hello")
    print("Good Morning")

greet()

def add(x , y):
    c = x+y
    return c

result = add(2,5);
print(result)

def add_sub(x , y):
    c = x+y
    d = x-y
    return c, d

result1, result2 = add_sub(5, 1);
print(result1)
print(result2)


#passing args

def update(x):
    x = 8


def person(name, age):
    print(name)
    print(age)

# person('ramu',25)
# person(25, 'ramu')//wrong
person(age=25, name='ramu')

#with default value
def person(name, age=20):
    print(name)
    print(age)

#if i pass the person('ramu',25) value it will take passed value
person( name='ramu')

def sum(a, *b):
    # c = a+b
    print(a)
    print(b)#here the b become tuple with value of 6, 34, 78
    # print(c)
    #to solve this 
    c = a
    for i in b:
        c =c+i
    print(c)

sum(5,6,34,78)

#when there is no 'a' parameter
def sum(*b):
    print(b)#here the b become tuple with value of 6, 34, 78
    c = 0
    for i in b:
        c =c+i
    print(c)

sum(5,6,34,78)

#variable length argument
#multiple data with keyword using '**'
def pers(name, **data):
    print(name)
    print(data)
    #for loop to print key and value pair
    for i, j in data.items():  #where items is inbuilt function
        print(i,j)

pers('navin', age= 28, city = 'mumbai', mob= 9778577837)

