#pass list to a function

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even +=1
        else:
            odd += 1
    return even, odd

lst = [12,3,54,65,79,22]

even, odd = count(lst)

print("{} Evens and {} Odds are there in a given list".format(even, odd))

names = ['ramu','anand']
print(names[0])
print(names[0][0])
print(len(names[0]))