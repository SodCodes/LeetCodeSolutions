# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:

    """
    Plan: For each level in order, add the nodes into queue. For each level, pop the queue check the node children add to queue and store values in a list. Append list of values to order and empty when done (level is cleared). Then return nested list
    Time Complexity: O(n), because we search entire tree and search each node along with it's connections.
    Space Complexity: O(n) because the returned list can only be as big as n amount of nodes
    """

    #polished solution


    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        
        order = [] #Nested list that will be returned
        
        #Handle edge case, empty root = empty listy
        if root == None:
            return order
        
        #create queue
        queue = deque()
        queue.append(root) #append the level of root to queue once, ensures queue isn't empty
        
        while queue: #while queue is not empty
            level = [] #create a fresh list for that level, appended as a innerlist in 'order'
            for _ in range(len(queue)): #the length of queue at that time, is the amount of nodes in the level
                    
                    node = queue.popleft() #take each node in level from queue
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
                    
                    level.append(node.val) #append the current value of the node to the list of the current level
            
            order.append(level) #append the full values of that level into 'order'
        
        return order #return a complete order of each level 
                
                
"""
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        

        
def levelOrder(root: TreeNode) -> list[list[int]]:
    
    order = [] #the order of the tree by levels, this will be returned
    
    if root == None:
        return order #return an empty list
    
    order.append([root.val]) #append the level or root
    
    #create a queue of the current levels nodes
    queue = deque() 
   
        
    for inner_list in order:
        
        level = [] #create a list for that level, appended later in 'order'
        
        queue.append(root) #each item in queue is of type TreeNode
        
        for _ in range(len(queue)): #group and iteriate through the number of nodes on that level in queue
            
            node = queue.popleft() #node is of type TreeNode
            
            if node.left != None: #add left child first
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
            
            level.append(node.val) #take the current node's value and append it into the list of the current level
        
        order.append(level)
    
    return order
"""

        
       
  




"""  
     Commented out code as I didn't like this approach anymore, it was confusing me lkie crazy and spent too much time on it. Kept for progress of learnign and though as I was solving the problem
        for num in a_level:
            #take the next node of that level and check it's children
            curr_val = a_level.popleft() 
            
            #Take node and set it as an argumnet for classTreeNode
            node = TreeNode(curr_val)
            
            #store the value of the right and left of the current node
            left_child  = node.left
            right_child = node.right
            
            #Create a flag, to check if the children of that node is None has no empty children
            isNone = False
            
            if left_child == None and right_child == None:
                isNone = True
            
            #check to see if left or right is none and if not add to queue
            if left_child != None:
                levels.append(left_child)
            if right_child != None:
                levels.append(right_child) #levels = deque([3, 9, 20])
            
"""        
            
            
        
