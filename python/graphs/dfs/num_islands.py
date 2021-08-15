# https://leetcode.com/problems/number-of-islands/


class Solution:
    def explore(self,i,j):
        if i>=0 and i<self.nrow and j>=0 and j<self.ncol and self.grid[i][j]=='1' and (i,j) not in self.visited:
            self.visited.add((i,j))
            self.explore(i+1,j)
            self.explore(i-1,j)
            self.explore(i,j+1)
            self.explore(i,j-1)
        
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited=set()
        self.grid=grid
        self.nrow=len(grid)
        self.ncol=len(grid[0])
        ctr=0
        for i in range(self.nrow):
            for j in range(self.ncol):
                if (i,j) not in self.visited and self.grid[i][j]=='1':
                    self.explore(i,j)
                    ctr+=1
            
        return ctr
