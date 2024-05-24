from functools import reduce

#normal function
# def is_even(n):
#     return n%2 == 0

nums = [3,2,6,8,4,6,2,9]

def update(n):
    return n*2

def add_all(a, b):
    return a+b

#FILTER
# evens = list(filter(is_even, nums))
evens = list(filter(lambda n: n%2 == 0, nums)) #using lambda function

#MAP
doubles = list(map(update, evens))

#REDUCE
sum = reduce(add_all, doubles)


print(evens)
print(doubles)
print(sum)