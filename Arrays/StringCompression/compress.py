# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to 
# become 'A4B4C5D2E4'. For this problem, you can falsely 
# "compress" strings of single or double letters. For instance, it 
# is okay for 'AAB' to return 'A2B1' even though this technically 
# takes more space.
# The function should also be case sensitive, so that a string 
# 'AAAaaa' returns 'A3a3'.

# Run length compression algorithm
def compress(string):
    
    run = ""
    length = len(string)
    
    # Edge Case check
    if length == 0:
        return ""
    
    if length == 1:
        return string+"1"
    
    last = string[0]
    count = 1
    i = 1
    
    # Check if the value currently being indexed is the same as
    # the previous iterated value
    # if so, increment count
    # if not, store the run and start a new count 
    while i < length:
        if string[i] = string[i -1]:
            count += 1
        else:
            run = run + string[i - 1] + str(count)
            count = 1
            
        i += 1
        
    run = run + string[i - 1] + str(count)
    
    return run
    