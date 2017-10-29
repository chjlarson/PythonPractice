// Consider an array of non-negaive integers. A second array is
// formed by schuffling the elements of the first array and
// removing a random element.

def finder3(arr1, arr2):
    result = 0
    
    # Perform an XOR between the numbers in the arrays
    for num in arr1 + arr2:
        result ^=num
        print result
        
    return result