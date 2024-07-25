# Array example 1

import numpy as np
"""
Create a program that creates an array and manipulates it
"""
# We create the array
a = np.array([1, 2, 3])

# We print the matrix
print(a)

# Number of rows
print(a.ndim)

# Array quantity
print(a.shape)

# We create 2D matrix
b = np.array([(1.5, 2, 3),(4, 5, 6)],dtype = float)

# We show the 2D matrix
print(b)
print(b.ndim)
print(b.shape)

# Create a 3D 2 row x 3 column array 
c = np.array([[(1.5, 4, 3),(4, 5, 6)],[(5, 5, 5),(6, 6, 6)]])

print(c)
print(c.ndim)
print(c.shape)