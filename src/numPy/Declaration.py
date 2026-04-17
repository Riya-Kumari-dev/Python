import numpy as np

# From already given data 
# np.array(something like array)
l = [1,2,3,4]
n = np.array(l)
print(n) # [1 2 3 4]
print(type(n)) # <class 'numpy.ndarray'>

# same type
l = [1,2,5.6,3]
n = np.array(l)
print(n) # [1.  2.  5.6 3. ] => convert all the values to float type
n = np.array(l,dtype = int)
print(n)  # [1 2 5 3]

l = [3,2,"Ram"]
n1 = np.array(l)
print(n1) # ['3' '2' 'Ram'] => all are string type
 
# np.ones()
# all ones
n = np.ones(4)
print(n) # [1. 1. 1. 1.]
n= np.ones((2,3),dtype = int)
print(n)
# [[1 1 1]
#  [1 1 1]]

# np.zeros()
n = np.zeros(3)
print(n) # [0. 0. 0.]
n = np.zeros((2,3),dtype = int)
print(n)
# [[0 0 0]
#  [0 0 0]]

# np.full() 
# all elements same
n = np.full(5,6) # create a array with 5 elements each value = 6
print(n) # [6 6 6 6 6]
n = np.full((3,3),4) # 3*3 matrix each 4
print(n)
# [[4 4 4]
#  [4 4 4]
#  [4 4 4]]

# np.empty(elements number)
# random values ka array
n = np.empty(4,dtype = int)
print(n) # [4607182418800017408 4607182418800017408 4607182418800017408 4607182418800017408] # all same

# random.randin()
# print random values from 0 to 1
n = np.random.rand(4)
print(n) # [0.89857517 0.74473304 0.35150255 0.01470525]

# np.arange()
n = np.arange(4) # ele from [0,4) with step = 1
print(n)
n = np.arange(3,20,3) # [3,20) with step = 3
print(n) # [ 3  6  9 12 15 18]

# np.identity()
# print identity square matrix
n = np.identity(3)
print(n)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# np.eye()
# print identity m*n matrix
n = np.eye(3,4)
print(n)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]]