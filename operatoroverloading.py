class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

s1 = Student(58, 69)
s2 = Student(69, 65)

s3 = s1 + s2

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins") 

print(s2) 

print(s3.m1)
print(s3.m1,s3.m2)


class MyClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # Custom addition behavior
        return f"{self.value} plus {other.value}"

# Create instances
obj1 = MyClass(3)
obj2 = MyClass(4)

# Using the overloaded + operator
result = obj1 + obj2
print(result)  # Output: 3 plus 4
