

"""

https://leetcode.com/problems/design-hit-counter/

"""

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hit_record=[]
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hit_record.append(timestamp)
        #while self.hit_record[-1]-self.hit_record[0]>=300:
        #    self.hit_record.pop(0)
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        
        In this approach, if a million hits are recorded before a single getHits call, then while loop will be called millions of times.
        
        How to optimize it?
        
        Don't fuck with the data itself. Use a better data structure 
        https://leetcode.com/problems/design-hit-counter/solution/842468
        
        """
        if self.hit_record==[]:
            return 0
        
        #print(self.hit_record)
        
        while timestamp-self.hit_record[0]>=300:
            self.hit_record.pop(0)
            if self.hit_record==[]:
                return 0
            
        return len(self.hit_record)
