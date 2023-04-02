# https://leetcode.com/problems/path-crossing/

# tuple is hashable to can be added to list

from typing import Tuple

class Solution:
    def isPathCrossing(self,path:str)->bool:
        if path=='' or not path:
            return True
        locations={(0,0)}
        current=(0,0)
        for p in path:
            current=self.move(current,p)
            if current in locations:
                return True
            else:
                locations.add(current)
        return False
            
    def move(self,curr:Tuple,direction:str)->Tuple:
        if direction=='N':
            return (curr[0]+1,curr[1])
        elif direction=='E':
            return (curr[0],curr[1]+1)
        elif direction=='S':
            return (curr[0]-1,curr[1])
        elif direction=='W':
            return (curr[0],curr[1]-1)

