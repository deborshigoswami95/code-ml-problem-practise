# https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

class naiveSolution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        # O(nlog_n + 3n)
        
        arr = sorted(arr) # n * log_n
        arr_sum = sum(arr) # n
        
        while arr_sum>5000: # n
            i = arr.pop(-1)
            arr_sum-=i
        
        return len(arr) # n 
