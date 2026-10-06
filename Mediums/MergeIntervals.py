"""
PLAN:  For each pair, the code will sort the given nested list (intervals). Then for each range, I compare it to the last range in my result.
TIME:  O(n log n) because there's a sort done on an input and then a pass for each element in sorted nested list.
SPACE: O(n) because the returned nested list can only be as big as the input worst case if there's no overlap.
"""


"""What overlap means?

1. If the end number of a pair is the same as the beginning number of the next
2. If the another pair of numbers in within the range of the previous pair
3. If the beginning number in the pair is less than the other end number of another pair
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        final_list = [] #This is a list that stores merged and non merged time ranges. This will be returned

        intervals.sort() #sort the given nested lists


        #Test case example: intervals = [[1,4],[4,5]]
        #1st pass, final_list = 0 , 2nd pass final_list is [1,4] and pair is sitting on 4,5
        for pair in intervals:

            if not final_list:
                final_list.append(pair) #if the list is empty we throw the 1st pair in the list
                continue #all we want for this part of the code is to create the 1st pair in list
            
            #compare the last element that we added in the final_list to be compared to the current sitting element
            if max(final_list[-1]) >= min(pair): #if the maximum of the last pair is greater than or equal to, then continue a merge
                if max(final_list[-1]) < max(pair): #if the max of the two are not equal , #the fix I made at 20 minutes after I pressed ran was this from "if max(final_list) < max(pair):" to if max(final_list[-1]) < max(pair):
                    end = pair[1] #the second number in the pair
                    #is now the last number in the final list pair
                    final_list[-1][1] = end
            else:
                final_list.append(pair) #append list as there's no overlap

        return final_list #return the final list

""" Polished Solution
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sort by start, so anything that overlaps ends up side by side.
        intervals.sort()

        final_list = []     # merged and unmerged ranges, in order

        for pair in intervals:
            # First range, OR a gap: this range starts after the last one ends.
            # final_list[-1][1] is "the end of the last range in my result".
            # It says the same thing as your max(final_list[-1]), more directly.

            # Instead of using max the comparsion now is directly comparing the 1st number in a pair to the last number in another pair.
            # this work since, in the pair the greater number is the second number in the pair. So instead of using pair[0] > max(final_list[-1])
            # I can use pair[0] > final_list[-1][1]

            if not final_list or pair[0] > final_list[-1][1]:
                final_list.append(pair)
            else:
                # Overlap: stretch the last range's end to whichever end is bigger.
                # This one line replaces your nested "if ... < ...:" block.
                # max() keeps [1,10] at 10 when [2,3] arrives. , in example intervals list = [[1,10],[2,3],[4,5]]
                final_list[-1][1] = max(final_list[-1][1], pair[1]) # so this pair would be [10,3] assuming final_list current has [1,10] and pair is [2,3]

        return final_list
"""
            


        
