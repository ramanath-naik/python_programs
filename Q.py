Queue=[]
def enqueue():
    element=input("enter a element: ")
    Queue.append(element)
    print(element,"is added to queue")

def dequeue():
    if not Queue:
        print("Queue is empty")
    else:
        e=Queue.pop()
        print("removed element is :",e)

def display():
    print(Queue)

while True:
    print("Enter operation you want to perform 1.add 2.remove 3.show 4.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter correct operation")





