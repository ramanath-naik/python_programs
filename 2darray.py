import numpy as np

arr1 = np.array([
    [1,2,3,4,5,6],
    [4,5,6,7,8,9]
])

print(arr1)
print("Dimension:",arr1.ndim)
print(arr1.shape)
print(arr1.size)

#convert into single dimension array
arr2 = arr1.flatten()
print(arr2)

#Convert into 3 dimensional array
arr3 = arr1.reshape(2,2,3)

#convert into 2d array
# arr3 = arr1.reshape(3,4)

print(arr3)


#matrix
m1 = np.matrix(arr1)
print("matrix \n",m1)

#another way declaring matrix
m2 = np.matrix('1 2; 3 4; 5 6; 7 8')
print(m2)

print(np.diagonal(m2))

m3 = np.matrix('1 2; 3 4')
m4 = np.matrix('5 6; 7 8')

m5 = m3 + m4
print("addition",m5)