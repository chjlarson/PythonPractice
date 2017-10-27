# Given an integer array, output all the unique pairs that sum up to a specific value K.

def pairSum(arr, k):
    
    # Return if the length of the array is less than 2
    # Edge case
    if len(arr) < 2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()
    
    for num in arr:
        
        # Looking for this value
        target = k - num
        
        # If the target isn't in the seen set, add it
        # Otherwse, return the lowest value(num or target) and the
        # highest value(num or target)
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target)), (max(num, target)))
            
        # Map the list of the output to strings
        print '\n'.join(map(str, list(output)))
        