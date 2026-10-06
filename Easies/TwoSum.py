class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        n = len(nums)

        seen = {} # A hashmap that will store the index and values of the list

        for i in range(n): #loop through every element in list one at a time

            target_num = target - nums[i] # target_num would be the number to be looked at in the hashmap
            if target_num in seen: #if there's the target_num matches with the index of seen which would be the value in the list of num
                return [seen[target_num], i] #return the index of that number in the hashmap along with the index of the number that is currently being sitted on in the list, which is i

            seen[nums[i]] = i # if not continue to populate the hashmap to help check for the next iteriation
            #{3: 0  }
        return seen