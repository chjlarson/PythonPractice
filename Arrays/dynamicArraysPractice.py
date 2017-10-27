import ctypes

class DynameArray(object):
    
    #Actual count of the Array
    #Capacity of the Array
    #Set A to an array with the capacity set in the previous step.
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
    
    #Return the count of the array
    def __len__(self):
        
        return slef.n
    
    #Return the idex of an elemnt if the element is present
    def __getItem__(self, k):
        if not 0 <= k <= self.n:
            return IndexError('K is out of bounds')
        return self.A[k]
    
    #Append to an array if there is space
    #Otherwise, double the size of the Array
    def append(self, ele):
        
        if self.m == self.capacity:
            self._resize(2*self.capacity) #2x the capacity
            
        self.A[self.n] = ele
        self.n += 1
        
    #Double the size of the Array
    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        
        for k in range(self.n):
            B[k] = self.A[k]
            
        self.A = B
        self.capacity = new_cap
        
    #Create an Array with the capacity of new_cap
    def make_array(sef, new_cap):
        return (new_cap * ctypes.py_object)()