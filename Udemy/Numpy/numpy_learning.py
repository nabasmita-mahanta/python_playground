import numpy as np

print(np.version)

my_list = [1, 2, 3]
arr = np.array(my_list)
print(arr)

my_mat = [[1,2,3], [4,5,6],[7,8,9]]
arr1 = np.array(my_mat)
print(arr1)

print(np.arange(0,11,2))
print(np.zeros(3))
print(np.zeros((2,3))) # two rows and three colomn
print(np.ones(4))
print(np.ones((3,4)))
print(np.linspace(0,5,100))
print(np.eye(4)) # same row and coloum, one in diagonal.
print(np.random.rand(5))
print(np.random.randn(4,4))
ranarr = np.random.randint(1,100,10)
print(ranarr)
print(ranarr.max())
print(ranarr.min())
# to find the index value of max
print(ranarr.argmax())
print(arr.shape) # dimension
print(arr.dtype) # for data type

