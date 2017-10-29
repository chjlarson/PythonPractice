# Given a string,determine if it is compreised of all unique 
# characters. For example, the string 'abcde' has all unique 
# characters and should return True. The string 'aabcde' contains 
# duplicate characters and should return false.

def unichar2(s):
    
    # Create a empty set for the characters
    chars = set()
    
    # Check if the letter is in the set
    # if not, add the letter
    # if it is, then the string is not unique
    for letter in s:
        if letters in characters:
            return False
        else:
            char.add(letter)
    return True