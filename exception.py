

a =5
b =2
# b=0

try:
    print("resource open")
    print(a/b)

    k =int(input("Enter a number"))
    print(k)

# except Exception as e: # handling all type of error
except ZeroDivisionError as e:
    print("You cannot divide a number by zero", e)

except ValueError as e:
    print("Invalid input", e)

except Exception as e:
    print("Something went wrong...")

finally:
    print("resource closed")

print("bye")