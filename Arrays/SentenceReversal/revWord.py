// Given a strings of words, reverse all the words and remove all 
// leading and trailing whitespaces.

def revWord(wordString):
    
    
    // Setup the variables
    words = []
    temp =[]
    length = len(wordString)
    spaces = [' ']
    i = 0
    
    while i < length:
        // find the beginning of the word
        if wordString[i] not in spaces:
            wordStart = i
            
            while i < length and wordString[i] not in spaces:
                // Count how many characters the word is
                i += 1
            // Add the word to the list of words    
            words.append(wordString[wordStart:i])
            
        // Iterate to the next value    
        i += i
        
    // Reverse the order of the list and
    // join them together in a string
    for i in range(len(words)/2):
        temp[i] = words[i]
        words[i] = words[(length -1) - i]
        words[(length - 1) - i] = temp
    
    return " ".join(words)