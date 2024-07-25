# Array example 1

import numpy as np
"""
Create different arrays and manipulate them in different ways
"""
# Array created with 0 "zeros"
# ((3 "rows", 4 "columns"))
zero = np.zeros((3,4))
print(zero)

# Array created with certain parameters and 1 "ones"
# ((2 "arrays," 4 "rows", 2 "columns"))
q = np.ones((2,4,2))
print(q)

# We ask for a vector in the following way
# (range from zero to two, 0.2..... with 9 vectors)
t = np.linspace(0,2,9)
# Sends us a vector with 9 elements
print(t)
# Shows the number of elements of "t"
len(t)

# We create a 3x3 matrix of 10 values
f = np.full((3,3),10)
print(f)

# 3x3 identity matrix where the diagonal has 1 (ones)
g = np.eye(3,3)
print(g)

# Array with random numbers
h = np.random.random((10,3))
print(h)