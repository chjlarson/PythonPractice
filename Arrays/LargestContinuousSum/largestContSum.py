# Given an array of integers ranging from negative to positive, 
# find the largest continuous sum.


# If the array is all positive, just add each element.
# Check sequences if there are negative values within .
def largestContSum(arr):
    
    # Edge case check
    if len(arr) == 0:
        return 0
    
    # Set a max and current value to the first element in the 
    # array.
    maxSum = arr[0]
    currentSum = arr[0]
    
    for num in arr[1:]:
        
        # Set the currentSum to the largest between the the
        # currentSum added to the current array iteration, 
        # or just the current array iteration
        currentSum = max(currentSum + num, num)
        
        # Set the maxSum to the largest value between the 
        # currentSum or the current maxSum.
        maxSum = max(currentSum, maxSum)
                                                                                         
    return maxSum