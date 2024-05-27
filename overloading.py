# Python does not support method overloading by default but we can achieve these like feature

#using default argument
class Demo:
    def add(self, a,b,c=0):
        return a+b+c
    
d = Demo()
print(d.add(2,3))
print(d.add(2,3,4))


#using args
print("using args")

class Demo2:
    def add(self, *args):
        total = 0
        for i in args:
            total = total+i
        return total
    
d1 = Demo2()

print(d1.add(3,2,6,7,5,43,22))