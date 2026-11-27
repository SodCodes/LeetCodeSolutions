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
    Time Complexity: O(n), because we iteriate through each input once. n = code1 , iterate once to create hashmap and m = code 2 iterate each element in string to modify hashmap. After n equal m, then complexity is O(n) as the input is the same
    Spcae Complexity: O(1), because the character set remains a constant of only all capital letters and only numbers.
    """
    
    char_count = {} #create hashmap to store count for each character
    if len(code1) == len(code2): #if the length of both codes are the same continue to solve
        
        for ch in code1:
            char_count[ch] = char_count.get(ch, 0) + 1 #create hashmap based off code1, if character exist add 1 to count value if not create key of character and set value to 1
        
        
        #for each character in code2
        for ch in code2: #1st pass: B, 3
            if ch in char_count:
                if char_count[ch] == 0: #Multiple Characters For One Code For Same Length Code
                    return False
                char_count[ch] -= 1 #Decrement the count by 1
            else:
                return False #the character in code2 is not in code1 so this is not scrambled with the same characters although same count
  
        list_of_values = char_count.values()
        # Check to see if the values of each character in hashmap are equal to 0, if they are return True
        for value in list_of_values:
            if value > 0:
                return False
        return True
            
        
    return False #the length is not the same 


"""
Polished Approach:
def is_rearrangement(code1, code2):
    # GUARD CLAUSE: if the lengths differ, they can't be rearrangements.
    # Returning early means the rest of the function doesn't need to sit inside an if.
    if len(code1) != len(code2):
        return False

    # STEP 1: build the "bank" — how many of each character code1 has.
    char_count = {}
    for ch in code1:
        # .get(ch, 0) = "current count, or 0 if ch isn't a key yet"; then +1 and store it back
        char_count[ch] = char_count.get(ch, 0) + 1

    # STEP 2: spend from the bank, one code2 character at a time.
    for ch in code2:
        # .get(ch, 0) == 0 catches BOTH ways to fail in one check:
        #   (a) ch never appeared in code1 -> not a key -> .get returns 0
        #   (b) ch appeared, but code2 already used up every copy
        if char_count.get(ch, 0) == 0:
            return False
        char_count[ch] -= 1          # take one from the bank

    # STEP 3: same length + never overdrew = every count is exactly 0.
    return True"""

print(is_rearrangement("A7B3", "B3A7"))