
# https://leetcode.com/problems/climbing-stairs/

class badSolution:
    """
    Why is this a bad solution even though it gives the accurate result?

    It only does recursion without using dynamic programming

    That is because in essense the recursion forms a decision tree. in which case it is
    inefficient to compute a sub-problem that has already been computed in a different part
    of the tree, which is what this algorithm. 

    It attacks each sub problem as if it is a new problem.

    What do we mean by this? 

    Let us say we are computing the subproblem of 'how many ways can we take 6 steps?'

    In this sub problem we will have to compute the 4 step subproblem at some point,
    which may occur in multiple parts of the 6 step problem. such as,
    a. taking 2 steps to get from 6 to 4
    b. taking 1 step from 6 to 5 and 1 more to get from 5 to 4

    If we compute 4-step subproblem in a. why compute it again in b.?

    this algorithm does not make that distinction.

    Hence, we need dynamic programming where we remember the 4-step computation for repeated use
    across the algotihm
    """

    def __init__(self):
        self.num_ways=0

    def climbStairs(self, n: int) -> int:

        def recursive_climbing(remaining_steps:int)->int:
            if remaining_steps==2:
                self.num_ways += 2
                return
            elif remaining_steps==1:
                self.num_ways += 1
                return
            else:
                # take 1 step and recurse
                recursive_climbing(remaining_steps-1)

                # take 2 steps and recurse
                recursive_climbing(remaining_steps-2)

        recursive_climbing(n)

        return self.num_ways
    

class Solution:
    """
    In DP, we use the concept of memoization to store previously computed subprobplems.

    In this case we will store the computed values in a dict
    
    """
    def climbStairs(self,n:int)->int:
        self.memo={}
        self.memo[1]=1
        self.memo[2]=2
        #self.num_ways=0

        def recursive_climbing(remaining_steps:int)->int:
            if remaining_steps in self.memo:
                return self.memo[remaining_steps]
            
            self.memo[remaining_steps]= recursive_climbing(remaining_steps-1) + recursive_climbing(remaining_steps-2)
            return self.memo[remaining_steps]

        recursive_climbing(n)

        return self.memo[n]
    
class BestSolution:
    """
    Turns out there is an even better solution than the 
    above where we don't even need to use recursion.

    It seems clear that the above sequence is just a fibonacci sequence

    For 
    N = 0, solution is 1
    N = 1, solution is 1
    N = 2, solution is 2
    N = 3, solution is 3
    N = 4, solution is 5

    For each N, the solution to how many ways of climbing steps in sets of 1 or 2 steps
    is the sum of the solutions for N-1 and N-2 steps.

    Then we can formulate the DP problem in a very simple way. It is the same concept as 
    the program for Fibonacci sequence

    HOWEVER, if we are trying to think about dynamic programic approaches then a 
    beginner should probably not try to formulate this solution for every DP problem.

    WHY?

    It happens to be the case that the pattern here was easy to figure out. The problem complexity
    is not that high. This may not be the case for all DP problems. 

    If we think that the problem requires dynamic programming and recursion. then we should
    try the previous approach first and then figure out if we can optimize it in this way.

    NOTICE, how Fibonacci series problem also requires dynamic programing and memoization for optimal
    performance
    
    """
    def climbStairs(self,n:int) -> int:
        # this solution is formulated by NeetCode: https://www.youtube.com/watch?v=_i4Yxeh5ceQ
        one,two=1,1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
    

if __name__=="__main__":

    print(Solution().climbStairs(10))
    print(Solution().climbStairs(4))
    print(Solution().climbStairs(5))
    print(Solution().climbStairs(6))
