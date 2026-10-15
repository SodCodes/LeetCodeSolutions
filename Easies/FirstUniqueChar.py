class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {} # a hashmapp that keep track of each character and it's count

        for ch in s:

            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1 #if the character exist add 1 if not create it and add a 1
                #this creates the hashmap for the stirng s
        
        for i in range(len(s)):
            ch = s[i] #variable ch now represents a character value of s at the index of i
            #test case = "abac"
            if ch in count:
                if count[ch] == 1:
                    return i #return index of the character
        
        return -1 # if we've looked through the complete length of the string and found no no repeating character
