import time 
import numpy as np

l1 = [i for i in range(1000000)]
l2 = [i for i in range(1000000)]
t1 = time.time()
print(t1) # 1776253928.5398326

# operation
l = [l2[i] - l1[i] for i in range(len(l1))] # subtract two lists
t2 = time.time()
print(t2-t1) # 0.12896490097045898

# numpy time analysis

n1 = np.arange(1000000)
n2 = np.arange(1000000)
t1 = time.time()
print(t1) # 1776253973.1437035

n = n2-n1 # we can directly add or subtract elements of numpy array
t2 = time.time()
print(t2-t1) # 0.0040438175201416016

# clearly numpy is the winner