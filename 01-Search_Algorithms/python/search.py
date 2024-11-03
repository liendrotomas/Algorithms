from src.Search_Class import *
import time
import random
import sys

data = np.arange(0,100000,2)
target = random.randint(data[0],data[-1])

search_tool = LinearSearch()
t0 = time.time()
index = search_tool.search(data, target)
t1 = time.time()
print(f"LinearSearch - Elapsed time:",(t1-t0),". Result: Found in",index)

search_tool = BinarySearch()
t0 = time.time()
index = search_tool.search(data, target)
t1 = time.time()
print(f"BinarySearch - Elapsed time:",(t1-t0),". Result: Found in",index)

search_tool = TernarySearch()
t0 = time.time()
index = search_tool.search(data, target)
t1 = time.time()
print(f"TernarySearch - Elapsed time:",(t1-t0),". Result: Found in",index)

search_tool = ExponentialSearch()
t0 = time.time()
index = search_tool.search(data, target)
t1 = time.time()
print(f"ExponentialSearch - Elapsed time:",(t1-t0),". Result: Found in",index)

search_tool = JumpSearch()
t0 = time.time()
index = search_tool.search(data, target)
t1 = time.time()
print(f"JumpSearch - Elapsed time:",(t1-t0),". Result: Found in",index)

search_tool = InterpolationSearch()
t0 = time.time()
index = search_tool.search(data, target)
t1 = time.time()
print(f"InterpolationSearch - Elapsed time:",(t1-t0),". Result: Found in",index)



if index == -1:
    print(f"Element",target,"is not in array")    
else:
    print(f"Value",target,"is in index",index ,":",data[index])
