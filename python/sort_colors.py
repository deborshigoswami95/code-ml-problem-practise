# https://leetcode.com/problems/sort-colors/

from typing import List

class Solution:
    def sortColors(self,nums:List[int])->None:
        col_map={
            0:0,
            1:0,
            2:0
        }

        while len(nums):
            col_map[nums[0]]+=1
            nums.pop(0)
        
        for k in col_map.keys():
            nums+=[k]*col_map[k]

        #print(nums)

        return
    
class OnePassSolution:
    # This solution is courtesy of dijkstra
    def sortColors(self,nums:List[int])->None:
        p0=0
        p2=len(nums)-1
        curr=0

        while curr<=p2:
            if nums[curr]==0:
                nums[p0],nums[curr]=nums[curr],nums[p0]
                curr+=1
                p0+=1
            elif nums[curr]==2:
                nums[p2],nums[curr]=nums[curr],nums[p2]
                p2-=1
            elif nums[curr]==1:
                curr+=1


        

if __name__=="__main__":
    Solution().sortColors([2,2,0,1,0,2,2])
