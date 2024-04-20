# Import NumPy as np
import numpy as np
# Create an array of 10 zeros
arr = np.zeros(10)
print(arr)
# Create an array of 10 ones
print(np.ones(10))
# Create an array of 10 fives
print(np.ones(10)*5)

# Create an array of the integers from 10 to 50
print(np.arange(10,51))

# Create an array of all the even integers from 10 to 50
print(np.arange(10,51,2))

#Create a 3x3 matrix with values ranging from 0 to 8
print(np.arange(9).reshape(3,3))

# Create a 3x3 identity matrix
print(np.eye(3))

# Use NumPy to generate a random number between 0 and 1
print(np.random.rand(1))

# Use NumPy to generate an array of 25 random numbers
# sampled from a standard normal distribution.

print(np.random.randn(25))

# Create an array of 20 linearly spaced points between 0 and 1
print(np.linspace(0,1))












