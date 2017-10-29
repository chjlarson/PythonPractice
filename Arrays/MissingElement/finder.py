// Consider an array of non-negaive integers. A second array is
// formed by schuffling the elements of the first array and
// removing a random element.

def finder(arr1, arr2):
    
    // Sorting both arrays
    arr1.sort()
    arr2.sort()
    
    // Zip together lists into and returns a list of touples.
    // Return the number of the first array if the touples are not
    // the same.
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
        return arr[-1]