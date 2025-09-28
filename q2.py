'''
Zeros:
 [[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
Ones:
 [[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
Range: [0 2 4 6 8]
Linspace: [0.   0.25 0.5  0.75 1.  ]
Identity Matrix:
 [[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
'''
import numpy as np
# Array of zeros
zeros = np.zeros((3, 4))   # 3 rows, 4 columns
print("Zeros:\n", zeros)

# Array of ones
ones = np.ones((2, 5))     # 2 rows, 5 columns
print("Ones:\n", ones)

# Array with a range of numbers
arr_range = np.arange(0, 10, 2)  # start=0, stop=10, step=2
print("Range:", arr_range)

# Array with evenly spaced numbers
lin_arr = np.linspace(0, 1, 5)   # 5 values between 0 and 1
print("Linspace:", lin_arr)

# Identity matrix (square matrix with diagonal=1)
identity = np.eye(4)  # 4x4
print("Identity Matrix:\n", identity)


