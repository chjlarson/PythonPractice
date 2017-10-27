import sys

# Set n
n = 10

data = []

for i in range(n):
    # Number of elements
    a = leng(data)
    
    # Actual Size in Bytes
    b = sys.getsizeof(data)
    
    print "Length: {0:3d}; Size in bytes: {1:4d} ".formtat(a,b)
    
    # Increase length of the Array by 1
    data.append(n)
    