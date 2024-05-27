class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()  #instance inside outer class

    def show(self):
        print(self.name , self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = "Hp"
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)


s1 = Student('Navin',2)
s2 = Student('Jenny',3)

s1.show()

# lap1 = Student.Laptop()  #direct creating instance

# lap1 = s1.lap
# lap2 = s2.lap

# print(id(lap1))
# print(id(lap2))


class OuterClass:
    class InnerClass:
        def __init__(self, name):
            self.name = name
        
        def display(self):
            print(f"Hello, {self.name}!")

    def __init__(self, inner_name):
        self.inner_instance = self.InnerClass(inner_name)

    def show_inner(self):
        self.inner_instance.display()

# Creating an instance of OuterClass
outer = OuterClass("Nested")
# Accessing the method of the inner class through the outer class
outer.show_inner()

# Directly creating an instance of InnerClass
inner = OuterClass.InnerClass("Direct Access")
inner.display()
