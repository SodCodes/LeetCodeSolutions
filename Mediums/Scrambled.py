"""
Part of our warehouse system receives product codes, and some codes come in scrambled.
Problem: Codes come in scrambled. 

Input: Combination of Capital Letters and Numbers represented as a string. "An example: A7B3"
Output: Return True if scrambled, Return False is both codes are unique
Edge Case: A code can be empty. If 2 empty codes are given return True
"""

"""
Plan: Sort both codes, compare both codes if not the same sorted list return False else return True
Time Complexity: O(n log n + m log m) , because two sorts on two different inputs and compare each sorted list
Space Complexity: 0
"""
#The function should be able to take in 2 codes and tell if it has the same characters but scrambled of another
"""
def is_rearrangement(code1, code2):
    #edge case
    
    if code1 == "" and code2 == "": #edge case for if both code inputs are empty return True
        return True
        
    if code1 == "" or code2 == "":
        return False #this is towards edge cases of empty code for one code or both codes are empty
    
    if sorted(code1) == sorted(code2): #after sort if both list are the same then characters are scrambeled
        return True
    else:
        return False
            
"""

def is_rearrangement(code1, code2):
    
    """
    Plan: Check if both inputs are of the same length first. If not return False. If so, create hashmap of code1, iteriate through code1 to create hashmap. While code1 in code2 decremenet hashmap count else return False.
    Time Complexity: O(n + m), because we iteriate through each input once. n = code1 , iterate once to create hashmap and m = code 2 iterate each element in string to modify hashmap.
    Spcae Complexity: O(n), because create only one hashmap for an input.
    """
    char_count = {} #create hashmap to store count for each character
    if len(code1) == len(code2): #if the length of both codes are the same continue to solve
        
        for ch in code1:
            char_count[ch].get(ch, 1) + 1 #create hashmap based off code1, if character exist add 1 to count value if not create key of character and set value to 1
        print(char_count)   
        #for each character in code2
        for ch in code2:
            if ch in char_count:
                if char_count[ch] == 0: #Multiple Characters For One Code For Same Length Code
                    return False
                char_count[ch] -= 1 #Decrement the count by 1
        # Check to see if the values of each character in hashmap are equal to 0, if they are return True
        
    return False #the length is not the same 
    
is_rearrangement("A7B3", "B3A7")   
    
    
"""
    - Don't forget Sod, include IBM feedback in next response
    - Include Maata email
    - and report time log
    """