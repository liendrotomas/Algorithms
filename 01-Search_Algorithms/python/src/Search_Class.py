"""
Búsqueda Lineal (Linear Search)
Búsqueda Binaria (Binary Search)
Búsqueda Ternaria (Ternary Search)
Búsqueda Exponencial (Exponential Search)
Jump Search (para listas ordenadas)
Interpolación de Búsqueda (Interpolation Search)
"""
import numpy as np 

class SearchAlgorithm:
    def search(self, data, target):
        raise NotImplementedError("Subclasses should implement this!")

class LinearSearch(SearchAlgorithm):
    def search(self, data, target):
        for index, value in enumerate(data):
            if value == target:
                return index
        return -1

class BinarySearch(SearchAlgorithm):
    def search(self, data, target):
        print("Binary Search")
        min_val = 0
        max_val = len(data)-1
        index = max_val
        index_prev = min_val
        while 1:
            index_prev = index
            index = int(np.floor((max_val+min_val)/2))
            if index == index_prev:
                break
            if target == data[index]:
                return index
            elif target > data[index]:
                min_val = index+1
            else:
                max_val = index-1
        return -1
    
class TernarySearch(SearchAlgorithm):
    def search(self, data, target):
        print("Ternary Search")
        min_val = 0
        max_val = len(data)-1
        while 1:
            index1 = int(np.floor(min_val+(max_val-min_val)/3))
            index2 = int(np.floor(max_val-(max_val-min_val)/3))
            if index1 == index2:
                break
            if target == data[index1]:
                return index1
            elif target == data[index2]:
                return index2
            elif target < data[index1]:
                max_val = index1-1
            elif target > data[index2]:
                min_val = index2+1
            else:
                min_val = index1+1
                max_val = index2-1
        return -1
    
class ExponentialSearch(SearchAlgorithm):
    def search(self, data, target):
        print("Exponential Algorithm")
        if target == data[0]:
            return 0
        index = 1
        index_prev = index
        exp = 0
        while data[index] < target:
            if target == data[index]:
                return index
            else:
                index_prev = index
                index = index + 2**exp
                exp = exp + 1
                if index >= len(data) - 1:
                    index = len(data) - 1
        index_binary = BinarySearch().search(data[index_prev:index],target)
        if index_binary == -1:
            return -1
        return index_prev+index_binary

class JumpSearch(SearchAlgorithm):
    def search(self, data, target):
        step_size = int(np.sqrt(len(data)))
        index_prev = 0
        index = step_size
        while 1:
            if index >= len(data):
                index = len(data)-1
                res = LinearSearch().search(data[index_prev:index],target)
                if res == -1:
                    return res
                
                return index_prev+res

            if target < data[index]:
                res = LinearSearch().search(data[index_prev:index],target)
                if res == -1:
                    return res
                
                return index_prev+res
            
            index_prev = index
            index = index + step_size
            
class InterpolationSearch(SearchAlgorithm):
    def search(self, data, target):
        print("Interpolation Search")
        lo = 0
        hi = len(data) - 1

        while lo <= hi and target >= data[lo] and target <= data[hi]:
            # Check for division by zero
            if data[hi] == data[lo]:
                print("Error: data[lo] and data[hi] are the same, causing a potential divide by zero.")
                break
            
            numerator = (target - data[lo]) * (hi - lo)
            denominator = data[hi] - data[lo]
            index = int(lo + numerator / float(denominator))

            # Check if the target is found at the index
            if data[index] == target:
                return index
            elif data[index] < target:
                lo = index + 1
            else:
                hi = index - 1

        # Target was not found
        return -1

