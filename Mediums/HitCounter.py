"""
Plan: For a hit, update hits list, and add the hit to list. For GetHits update hit list, and return the length of the list as that's the count of valid hits 
Time: Amortized O(1) per call , each call with a timestamp
Space: O(number of hitsi n the last 300seconds) , these are held in the queue
"""

from collections import deque

class HitCounter:
    def __init__(self):
        self.fivemins = 300 #seconds which is 5 minutes
        self.hits = deque() #a queue that stores all hits in range
        
    #internal/private helper method, that drops every hit outside windoow
    def _evict(self, timestamp):
        
        #set the left side of the window
        left = timestamp - self.fivemins
        
        #hit counts if it's greather than the left side of the window
        #self.hits is checked to see if it's not empty first before any value is being accessed
        while self.hits and self.hits[0] <= left:
            
            self.hits.popleft() #O(1) time removal
            
    def hit(self, timestamp):
        self._evict(timestamp)
        self.hits.append(timestamp) #only way to append a time to the list
        
        
    def getHits(self, timestamp):
        self._evict(timestamp)
        return len(self.hits)