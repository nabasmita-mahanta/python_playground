import numpy as np

arr = np.arange(5,12)
print(arr)
print(arr[5])
print(arr[1:5])
arr[0:5] = 100
print(arr)
arr = np.arange(0,11)
print(arr)
slice_of_arr = arr[0:6]
print(slice_of_arr)

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)
print(arr_2d[0])
print(arr_2d[1][1])
print(arr_2d[1][2])
print(arr_2d[:2,1:])
print(arr_2d[:2])

# Conditional selection

arr = np.arange(1,11)
print(arr)
bool_arr = arr>5
print(bool_arr)
print(arr[bool_arr])
print(arr[arr<3])

arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)
print(arr_2d[1:3,3:5])
