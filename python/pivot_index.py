# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        len_nums=len(nums)
        index = 0
        l_sum=0
        r_sum=sum(nums[1:])
        
        while index<len_nums and l_sum!=r_sum:
            if index+1==len_nums:
                return -1
            l_sum+=nums[index]
            r_sum-=nums[index+1]
            index+=1
            
        return index
