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


class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, name, age):
        student = self.Student(name, age)  # Creating an instance of the inner class
        self.students.append(student)

    class Student:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def display_info(self):
            print(f"Name: {self.name}, Age: {self.age}")
            # print("Name: {}, Age: {}".format(self.name, self.age))#another way of printing using placeholder with format


# Creating an instance of the University class
university = University("ABC University")

# Adding students to the university
university.add_student("Alice", 20)
university.add_student("Bob", 22)
university.add_student("Charlie", 21)

# Displaying information about each student
for student in university.students:
    student.display_info()

