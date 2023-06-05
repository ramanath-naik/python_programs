def sympal(string):
    if string==string[::-1]:
        print("String is palindrome")
    else:
        print("string is not palindrome")

    size=len(string)
    if size%2==0:
        half=size//2
        if string[0:half]==string[half:size]:
            print("This is symmetric")
        else:
            print(" string is not symmetrical")

    else:
        print("string is not symmetrical")

sympal("amaama")
