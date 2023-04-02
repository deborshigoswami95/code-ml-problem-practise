# https://leetcode.com/problems/house-robber/description/

from typing import Tuple, Union, List, Optional

from time import time

class recursiveTopDownSolution:
    """
    This solution, while correct will take too long for complex sequences because
    robery value for the same index will be computed multiple times. 

    Similar to the climbing chairs problem, we need to memoize the solution
    in order to make it efficient

    This is the first step in converting it to a dyanamic programming problem
    
    """

    def rob(self, nums: List[int]) -> int:
        self.nums=nums
        self.len = len(nums)-1
        self.num_computations=0

        def recursively_rob(i):
            if i > self.len:
                return 0
            else:
                self.num_computations+=1
                return max(self.nums[i] + recursively_rob(i+2), recursively_rob(i+1))
        return recursively_rob(0)
    
class recursiveMemoTopDownSolution:
    def rob(self,nums: List[int])-> int:
        self.nums=nums
        self.len = len(nums) - 1
        self.memo={}
        self.num_computations=0

        def recursively_rob(i:int)->int:
            if i in self.memo:
                return self.memo[i]
            elif i > self.len:
                return 0
            else:
                self.memo[i] = max(self.nums[i] + recursively_rob(i+2), recursively_rob(i+1))
                self.num_computations+=1
                return self.memo[i]
        return recursively_rob(0)

class iterativeMemoBottomUpSolution:
    def rob(self,nums:List[int])->int:
        self.num_computations=0
        memo={}
        memo[-1]=0
        memo[0]=nums[0]
        for i in range(1,len(nums)):
            memo[i]=max(nums[i]+memo[i-2], memo[i-1])
            self.num_computations+=1
        return memo[len(nums)-1]

class iterativeMemoBottomUpOptimizedSolution:
    def rob(self,nums:List[int])->int:
        memo1=0
        memo2=nums[0]
        self.num_computations=0
        for i in range(1,len(nums)):
            max_reward=max(nums[i]+memo1, memo2)
            self.num_computations+=1
            memo1=memo2
            memo2=max_reward
        return memo2

    

if __name__=='__main__':
    #print(recursiveTopDownSolution().rob([1,2,3,1]))
    test_cases = [
        [1,2,3,5,8,3,2,7],
        [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
    ]

    solutions = {
        #'baseline recursive':recursiveTopDownSolution,
        'memoized recursive':recursiveMemoTopDownSolution,
        'iterative memoized':iterativeMemoBottomUpSolution,
        'iterative memoized optimized':iterativeMemoBottomUpOptimizedSolution
    }

    print('\n\n')

    for test in test_cases:
        for method in solutions:
            print(method)
            print('{}... x{}'.format(test[:min(len(test),10)], len(test)))
            start=time()
            sol=solutions[method]()
            print(sol.rob(test))
            print('num computations --> {}'.format(sol.num_computations))
            print('Time -->  {}\n\n'.format(time()-start))
