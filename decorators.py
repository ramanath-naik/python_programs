def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()



def add_one_decorator(func):
    def add_one():
        value = func()
        return value + 1
    return add_one

def example_function():
    return 1
    
final_value = add_one_decorator(example_function)
print("final value",final_value())



# def div(a,b):
#     return a/b

# div(2,4)

def div(a, b):
    print(a / b)

def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

div = smart_div(div) #decorator

div(2, 4) 
