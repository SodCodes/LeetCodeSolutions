"""
Questions:
Value: Can the numbers given be negative? What is the range of numbers that can be given?
Edge Cases: Can the input be empty? How large can the list of numbers be?
Output: What should be returned if any number in a given list appears more than once?
Input? Is the list of numbers sorted?
"""


"""
PLAN:  For each integer in array nums, I will store the integer in a set. If an integer is already in set I will return false if not return True
TIME:  O(n) because worst case if every element in input is unique we will have to look at every element onc .
SPACE: O(n) because the set can only be as large as the input array nums if worst case every element in nums is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        seen = set() #create an empty set called seen that stores each number that has been seen in array nums


        #Test Case: [1,2,5,1]

        for num in nums: 
            
            #check first if number is in set if not add number to set
            if num in seen: #this condition checks the current number in the given integer array if it has been seen
                return True #if the number has been seen return True as this is a duplicate number. 
            else:
                seen.add(num)

        return False #if all elements in list has been looked at to see if a duplicate is in set seen
        