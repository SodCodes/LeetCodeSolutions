#Optimal Soltuion
"""
Plan: For each string, sort the string, store it as a key and create a list for the key. Store the word in that list and return a list of all lists in hashmap.
Time Complexity: O(n x k log k) , because we itierate through every word and run a sort on the length of that word
Space Complexity: O(n x k) , a list is made from each sorted word and hashmap can only every be as the amount of strings given worst case scenario
"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {} #create hashmap to store sorted word keys and group words

        for word in strs: #iteriate through every word in given list of strings
            key = "".join(sorted(word)) #create var 'key' that is a flag check against hashmap
            if not key in groups:
                groups[key] = [] #if the key is not in hashmap create a key, value pair
            groups[key].append(word) #use append to add to the list of the key  
        
        return list(groups.values()) #return a nested list, using list()

"""
Plan: Given each string in input list, sort the string, compare the string to first string in each inner list, if there's a match insert string into inner list if not create new one.
Let n = number of words and k = length of the longest word.
Time: for each of the n words, you loop over up to n groups, and every comparison sorts group[0], which costs k log k. That’s O(n² · k log k).
Space: O(n · k), because the groups end up holding every character of every word.
"""
"""
    #Polished Solution
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = []                          # list of inner lists (the groups)
        for word in strs:
            sorted_word = sorted(word)       # e.g. "tea" -> ['a','e','t'] (a list)
            found = False                    # FLAG: reset for EVERY word
            for group in groups:             # `group` IS the inner list itself
                if sorted_word == sorted(group[0]):
                    group.append(word)       # add straight into the matching group
                    found = True
                    break                    # stop looking, we found its home
            if not found:                    # decide only AFTER checking every group
                groups.append([word])        # no home anywhere -> start a new group
        return groups
"""
"""
    Brute Force Attempt
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        groups = [] #this will be nested list that will be returned
        
        
        for word in strs: #look at value not index 
            
            
            if not groups:
                groups.append([word]) #take the current word and append to groups
                continue
            
            
            sorted_word = sorted(word) 
            

            found = False
            count = 0 #a pointer to each inner list in outer list, groups , 2nd pass count is 1
            for group in groups: 
                if sorted_word == sorted(group[0]):
                    found = True #take the current word and append it to the current group in groups.
                    break
                else:
                    count += 1

            if found: #take the current word and insert the word into the group
                groups[count].append(word) #insert the word into group
            else:
                groups.append([word]) #create group with word


        return groups
"""