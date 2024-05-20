# Example for using break statement

av = 5
x = int(input("How many candies you want?"))

i=1
while i <= x:
    if i > av:
        print("Out of stock")
        break
    print("candy")
    i += 1

print("Thank you")

#Ex continue statement for skipping specific value

for i in range(1, 101):
    if i%3 and i%5 == 0:
        continue
    print(i)

print("Bye")


#Pass statement

for i in range(1, 101):

    if( i%2 != 0):
        pass
    else:
        print(i)

print("Bye")