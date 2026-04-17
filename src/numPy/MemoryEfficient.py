import numpy as np # aliasing => np is an alias for numpy
import sys # for size of list 

l = [i for i in range(100)]
print(l)
itemsize = sys.getsizeof(l[0])
print(itemsize) # one integer element size = 28
print(itemsize*len(l)) # 2800

arr = np.arange(100) 
print(arr)
print(arr.itemsize) # size of each element in numpy array # 8 byte
print(arr.size)  # total elements => 100
print(arr.itemsize*arr.size) # 800

# it is clearly visible that numpy array is memory efficient.