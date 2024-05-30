#Iterators
iter_list = iter(['Hello', 'Good', 'Morning'])

print(next(iter_list))
print(next(iter_list))
print(next(iter_list))


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# Using the iterator
my_iter = MyIterator([1, 2, 3, 4, 5])

for item in my_iter:
    print(item)

#Generators
def sq_numbers(n):
    for i in range(1, n+1):
        yield i*i

a = sq_numbers(3)

print("The square of numbers 1,2,3 are : ")
print(next(a))
print(next(a))
print(next(a))


def my_generator(data):
    for item in data:
        yield item

# Using the generator
gen = my_generator([1, 2, 3, 4, 5])

for item in gen:
    print(item)
