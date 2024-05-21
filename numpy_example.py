
import numpy as np

# # np.array()
# arr1 = np.array([1, 2, 3, 4, 5])
# print("array:", arr1)

# # np.arange()
# arr2 = np.arange(1, 10, 2)
# print("arange:", arr2)

# # np.linspace()
# arr3 = np.linspace(0, 1, 5)
# print("linspace:", arr3)

# # np.zeros()
# arr4 = np.zeros((2, 3))
# print("zeros:")
# print(arr4)

# # np.ones()
# arr5 = np.ones((2, 3))
# print("ones:")
# print(arr5)

# # np.eye()
# arr6 = np.eye(3)
# print("eye:")
# print(arr6)

# # np.random.random()
# arr7 = np.random.random((2, 3))
# print("random:")
# print(arr7)

# # np.full()
# arr8 = np.full((2, 3), 7)
# print("full:")
# print(arr8)

# # np.reshape()
# arr9 = np.array([1, 2, 3, 4, 5, 6]).reshape((2, 3))
# print("reshape:")
# print(arr9)

# # np.flatten()
# arr10 = np.array([[1, 2, 3], [4, 5, 6]]).flatten()
# print("flatten:", arr10)


ar = np.array([1,2,3,4,5])
ar2 = np.array([6,7,8,9,10])
ar3 = ar + ar2
print(ar3)

print(np.sin(ar))
print(np.cos(ar))
print(np.log(ar))
print(np.sqrt(ar))
print(np.sum(ar))

#shallow copy
#A shallow copy means that the new array refers to the same data as the original array. 
#Modifying the data in the new array will affect the original array and vice versa. 
#In NumPy, a shallow copy is created using the view() method.

original_array = np.array([1, 2, 3, 4, 5])

# Create a shallow copy using view()
shallow_copy = original_array.view()

# Modify the shallow copy
shallow_copy[0] = 10

print("Original array:", original_array) 
print("Shallow copy:", shallow_copy)


#A deep copy means that the new array is a completely separate copy of the original array with its own independent data
# Modifying the data in the new array will not affect the original array. 
#In NumPy, a deep copy is created using the copy() method.

original_array = np.array([1, 2, 3, 4, 5])

# Create a deep copy using copy()
deep_copy = original_array.copy()

# Modify the deep copy
deep_copy[0] = 10

print("Original array:", original_array) 
print("Deep copy:", deep_copy) 