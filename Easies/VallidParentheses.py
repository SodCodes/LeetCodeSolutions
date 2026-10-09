""""
PLAN:  For each character, I will either push into the stack if it's an open bracket or if the character is a closing bracket, pop the stack and compare to see if the bracket is of the same order and compare it to the hashmap key to see if it's the same type.
EDGE CASES: If stack is empty and a closing character is hit, return False. If no closing character is reached then return False.
TIME:  O(n) because we are only reading the input variable s of bracket strings once, for each character we read once and make a decision in this algorithm.
SPACE: O(n) because the stack that is created can only store half of the given input string of brackets, aka variable s."""

class Solution:
    def isValid(self, s: str) -> bool:

        open_brackets = "([{" # store all open brackets in a var

        close_brackets = ")]}" #store all close brackets in a var

        stack = [] #initalize stack

        hashmap = {} #Create a hashmap that stores each unqiue closing character and the value must be the openening bracket that corresponds to that closing bracket

        hashmap[')'] = '('
        hashmap[']'] = '['
        hashmap['}'] = '{' #Create the hashmap that has the closing brakcets as the key and the open bracket as the value of that key

        #Create stack of just open brackets
        for i in s:  

            if i in open_brackets:
                stack.append(i) #create the stack from left to right with only the open brackets

            if i in close_brackets:
                if not stack:
                    return False #This condition is for if a closing character is reached before a open character. This is automatically a invalid parentheses pair
                
                #Check if open bracket is the same type of bracket as close in the hash map
                open_char = stack.pop()

                if hashmap[i] == open_char: #Pull the current closing bracket key in hashmap and compare the value of that key to see if it is of the same type as the open character that was just popped
                    continue
                else:
                    return False
                
        if not stack:
            return True  #if stack is empty that means we have worked through every pair with the open bracket
        else:
            return False
            
"""Polished Approach:
class Solution:
    def isValid(self, s: str) -> bool:
        # key = a closing bracket (what we'll have in hand),
        # value = the opening bracket it must match (what we need back)
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:                    # "ch" says what it holds; "i" suggests an index
            if ch in pairs:             # ch is a CLOSING bracket (it's a key in pairs)
                # Nothing to match against: a closer arrived before any opener.
                if not stack:
                    return False
                # The most recent unclosed opener must be this closer's partner.
                # Returning False right here replaces your if / continue / else.
                if stack.pop() != pairs[ch]:
                    return False
            else:                       # anything else is an OPENING bracket
                stack.append(ch)

        # Valid only if every opener got closed. "not stack" is already
        # True or False, so it replaces your four-line if/else.
        return not stack
"""

