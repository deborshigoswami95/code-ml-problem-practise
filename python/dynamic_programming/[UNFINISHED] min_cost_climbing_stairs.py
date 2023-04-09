from typing import List

class memoizedRecursiveSolution:
    def minCostClimbingStairs(self,cost:List[int])->int:
        # Memo will contain the minimum cost of traversing N remaining steps
        self.min_cost_memo={}
        self.min_cost_memo[1]=cost[-1]
        self.min_cost_memo[2]=cost[-2]
        self.len=len(cost)
        self.cost=cost

        def recursive_climbing(remaining_steps:int)->int:
            if remaining_steps in self.min_cost_memo:
                return self.min_cost_memo[remaining_steps]
            
            self.min_cost_memo[remaining_steps] = self.cost[-remaining_steps] + \
                min(recursive_climbing(remaining_steps-1),recursive_climbing(remaining_steps-2))
            
            return self.min_cost_memo[remaining_steps]
        
        return min(self.cost[0] + recursive_climbing(self.len-1), self.cost[1] + recursive_climbing(self.len-2))

