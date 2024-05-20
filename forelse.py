#case1
nums = [12,15,18,21,26]

for num in nums:
    if num%5 == 0:
        print(num)


#case2
nums = [12,10,18,20,26]

for num in nums:
    if num%5 == 0:
        print(num)
        

#case3. if we use break, we get only one number in output which is divisible by 5 
nums = [12,10,18,20,26]

for num in nums:
    if num%5 == 0:
        print(num)
        break

#using for else
nums = [12,30,18,22,26]

for num in nums:
    if num%5 == 0:
        print(num)
        break  #if we remove break, this will print not found also so break statement is compulsory 
else:
    print("Not found")