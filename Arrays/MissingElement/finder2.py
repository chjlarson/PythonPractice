// Consider an array of non-negaive integers. A second array is
// formed by schuffling the elements of the first array and
// removing a random element.

def finder2(arr1, arr2):
    
    // importing a defualt dictionary with a defualt key to 
    // prevent an error
    dict = collections.defaultdict(int)
    
    // Count each time an element shows up in the dictionary.
    // Because the defualt key is already created, we do not need 
    // to verify that num is in the dictionary.
    for num in arr2:
        dict[num] += 1
        
    // Return the element whos count is equal to 0.
    for num in arr1:
        if dict[num] == 0:
            return num
        else:
            dict[num] -= 1