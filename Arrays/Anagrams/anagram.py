# This program accepts two strings and determines if the strings
# are anagrams of each other, or that the same characters can be
# used to create both strings.
# This will not worry about capitalization or whitespace.

def anagram(s1, s2)
    
    # Remove whitespaces from the strings
    # Alter Capital characters to lowercase characters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    
    # Edge case to check whether both strings share the same 
    # number of characters.
    # Return False if condition is not true.
    if len(s1) != len(s2)
        return False
    
    # Create a dictionary to count the number of times a character
    # appears in the strings.
    count = {}
    
    # Count the frequency of each character in s1
    for letters in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
        
    # Decrement Count everytime a character is in both strings
    # Otherwise, count the frequency of each character in s2
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    # Evaluate the Count dictionary. 
    # If Count of each character is not equal to 0, return false
    for k in count:
        if count[k] != 0:
            return False